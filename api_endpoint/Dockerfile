# PyTorch ön yüklü imaj (CUDA destekli, CPU'da da çalışır)
FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime

# Gerekli sistem kütüphanelerini kur
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0

# Uygulama dosyalarını kopyala
COPY . /app
WORKDIR /app

# Kalan bağımlılıkları kur
RUN pip install --upgrade pip && pip install -r requirements.txt

# API'yi başlat
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
