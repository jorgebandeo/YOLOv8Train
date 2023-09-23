from ultralytics import YOLO
import keyboard
import winsound
def beep():
    frequency = 2500  # Frequência do apito em Hz
    duration = 1000  # Duração do apito em milissegundos
    winsound.Beep(frequency, duration)
# Load a model
model = YOLO('yolov8n-cls.yaml')  # build a new model from YAML


# Train the model
model.train(device = "cpu", data='C:/Users/jorge/Desktop/traiIA/root',name='ar_100_320_18x07', epochs=20, imgsz=510)

print("Pressione a tecla 't' para parar o apito.")
while True:
        beep()

        if keyboard.is_pressed('t'):
            break

print("Apito parado.")

