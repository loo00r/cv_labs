import cv2
import numpy as np

img = cv2.imread('franko.jpg')

# Усі точки мають формат [стовпці, рядки]
pts1 = np.float32([[8, 97], [262, 5], [301, 485], [580, 311]])
pts2 = np.float32([[0, 0], [400, 0], [0, 600], [400, 600]])
# Матриця трансляції
matrix = cv2.getPerspectiveTransform(pts1, pts2)
# Перетворення трансформація перспективи
result = cv2.warpPerspective(img, matrix, (400, 600))
# Відображення зсунутого
cv2.imshow('Output', result)

rows,cols = result.shape[:2]
# # Масиви точок перетворення
pts1 = np.float32([[0,0], [cols-1,0], [0,rows-1]])
pts2 = np.float32([[cols-1,0], [0,0], [cols-1,rows-1]])
# Матриця трансляції
M = cv2.getAffineTransform(pts1, pts2)
# Зсув фото
dst = cv2.warpAffine(result, M,(cols, rows))
# # Відображення зсунутого фото
cv2.imshow('Output', dst)



# Чекаємо, поки користувач натисне будь-яку клавішу
# (це необхідно, щоб уникнути збою ядра Python)
cv2.waitKey(0)
# Закриваємо всі відкриті в