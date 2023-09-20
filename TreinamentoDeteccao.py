from ultralytics import YOLO 


# Load the model.
model = YOLO('yolov8n.pt')
model.to('cpu')
# Training.
results = model.train(
      data='custom_data.yaml',
      imgsz= 480,
      epochs=1000,
      patience = 30,
      save_period = 1,
      batch=8,
      name='treinamento 3108',
      project = "pessoas",
      workers = 12,
      seed = 1,
      profile = True
   )