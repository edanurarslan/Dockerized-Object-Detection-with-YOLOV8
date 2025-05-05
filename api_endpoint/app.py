import base64
import os
import shutil
from pathlib import Path
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from ultralytics import YOLO

# FastAPI application
app = FastAPI()

# Template directory for Jinja2
templates = Jinja2Templates(directory="pages")

# Folder to store uploaded images
uploads_folder = Path("api_endpoint/input_images")

# Homepage (GET request)
@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Object detection endpoint (POST request)
@app.post("/detect/")
async def detect_objects(request: Request, image: UploadFile = File(...)):

    # Get "label" parameter from the form
    form_data = await request.form()
    label_value = form_data.get("label", None)

    # Check if image was uploaded
    if not image:
        return JSONResponse(status_code=400, content={"error": "No image uploaded"})

    # Save the uploaded image to folder
    uploads_folder.mkdir(parents=True, exist_ok=True)
    file_path = uploads_folder / image.filename
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    # If YOLOv8 ONNX model doesn't exist, export it
    onnx_model_path = 'yolov8n.onnx'
    if not os.path.exists(onnx_model_path):
        model = YOLO('yolov8n.pt')
        model.export(format='onnx')

    # Load ONNX model and perform prediction
    onnx_model = YOLO(onnx_model_path, task='detect')
    result = onnx_model(str(file_path), save=True, save_conf=True)

    # Process prediction results
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

    # Apply label filter if provided
    if label_value:
        output = [obj for obj in output if obj['label'] == label_value]

    # Path to predicted image (default path used by YOLO)
    predicted_image_path = f"runs/detect/predict/{image.filename}"

    # Encode image to Base64
    with open(predicted_image_path, "rb") as f:
        encoded_image = base64.b64encode(f.read()).decode("utf-8")

    # Return JSON response
    return {
        "image": encoded_image,
        "objects": output,
        "count": len(output)
    }
