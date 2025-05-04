# PyTorch base image (CUDA supported, works on CPU as well)
FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime

# Install required system libraries
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0

# Copy application files
COPY . /app
WORKDIR /app

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Start the API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

