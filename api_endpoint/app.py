import base64
import os
import shutil
from pathlib import Path
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from ultralytics import YOLO

# FastAPI uygulaması
app = FastAPI()

# Jinja2 için şablon dizini
templates = Jinja2Templates(directory="api_endpoint/pages")

# Görsellerin yükleneceği klasör
uploads_folder = Path("api_endpoint/input_images")

# Ana sayfa (GET)
@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Obje tanıma (POST)
@app.post("/detect/")
async def detect_objects(request: Request, image: UploadFile = File(...)):

    # Formdan label parametresini al
    form_data = await request.form()
    label_value = form_data.get("label", None)

    # Görsel var mı kontrolü
    if not image:
        return JSONResponse(status_code=400, content={"error": "No image uploaded"})

    # Görseli klasöre kaydet
    uploads_folder.mkdir(parents=True, exist_ok=True)
    file_path = uploads_folder / image.filename
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    # YOLOv8 ONNX modeli varsa yükle, yoksa dışa aktar
    onnx_model_path = 'yolov8n.onnx'
    if not os.path.exists(onnx_model_path):
        model = YOLO('yolov8n.pt')
        model.export(format='onnx')

    # Modeli yükle ve tahmin yap
    onnx_model = YOLO(onnx_model_path, task='detect')
    result = onnx_model(str(file_path), save=True, save_conf=True)

    # Tahmin sonuçlarını işle
    output = []
    for r in result:
        for box, cls, conf in zip(r.boxes.xywh, r.boxes.cls, r.boxes.conf):
            label = r.names[int(cls)]
            x, y, w, h = map(int, box.tolist())
            confidence = round(conf.item(), 2)
            output.append({
                "label": label,
                "x": x,
                "y": y,
                "width": w,
                "height": h,
                "confidence": confidence
            })

    # Label parametresi varsa filtre uygula
    if label_value:
        output = [obj for obj in output if obj['label'] == label_value]

    # Tahminli görselin yolu (varsayılan)
    predicted_image_path = f"runs/detect/predict/{image.filename}"

    # Base64 kodlama
    with open(predicted_image_path, "rb") as f:
        encoded_image = base64.b64encode(f.read()).decode("utf-8")

    # JSON çıktısı
    return {
        "image": encoded_image,
        "objects": output,
        "count": len(output)
    }
