import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Não foi possível abrir a câmera")
    exit()

ret, frame = cap.read()

# Diretório onde a foto será salva
diretorio = "/caminho/completo/do/diretorio/"

# Obtém a data e hora atual
data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Concatena a data e hora ao nome do arquivo
nome_arquivo = f"foto_{data_hora}.jpg"

# Concatena o diretório e o nome do arquivo
caminho_arquivo = diretorio + nome_arquivo

cv2.imwrite(caminho_arquivo, frame)

cap.release()
