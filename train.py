from ultralytics import YOLO

# Load a model
model = YOLO('/content/drive/MyDrive/yolov8/yolov8n.pt')  # load a pretrained model (recommended for training)

# Train the model with 2 GPUs
results = model.train(data='/content/drive/MyDrive/yolov8-Vehicle-Detection/config/data.yaml', epochs=100, imgsz=640, save_period=10)
model.val()