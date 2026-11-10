import cv2
import numpy as np
frame = cv2.imread('franko.jpg')
# Усі точки мають формат [стовпці, рядки]
pts1 = np.float32([[8, 97], [262, 5], [301, 485], [580, 311]])
pts2 = np.float32([[0, 0], [400, 0], [0, 600], [400, 600]])
# Матриця трансляції
matrix = cv2.getPerspectiveTransform(pts1, pts2)
# Перетворення трансформація перспективи
result = cv2.warpPerspective(frame, matrix, (400, 600))
# Відображення зсунутого фото
cv2.imshow('result', result)
# Чекаємо, поки користувач натисне будь-яку клавішу
# (це необхідно, щоб уникнути збою ядра Python)
cv2.waitKey(0)
# Закриваємо всі відкриті вікна
cv2.destroyAllWindows()