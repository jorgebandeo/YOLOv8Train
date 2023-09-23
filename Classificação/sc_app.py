from skimage.transform import resize
import numpy as np
import cv2
import pickle
from skimage.io import imread
EMPTY = True
NOT_EMPTY = False

MODEL = pickle.load(open("model.p", "rb"))


#imagem = cv2.imread("archive/fall_dataset/labels/train/fall002.txt")
from skimage.transform import resize
imagem  = imread('archive/fall_dataset/images/val/Nfall/not fallen038.png')
imagem_redimensionada = resize(imagem, (15, 15))
imagem_array = np.array(imagem_redimensionada)
previsao = MODEL.predict(imagem_array.reshape(1, -1))
if previsao == EMPTY:
    print("queda")
else:
    print("Nqueda")