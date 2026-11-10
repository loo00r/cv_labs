# Імпорт бібліотеки OpenCV
import cv2
# Читання зображення
img = cv2.imread('animals1.jpg')

# font
font = cv2.FONT_HERSHEY_PLAIN

# org
org = (50, 70)

# fontScale
fontScale = 2

# Чорний колір
color = (200, 0, 200)

# Товщина лінії 2 пікселів
thickness = 2

# Пишемо текст товщиною лінії 2 px
result = cv2.putText(img, 'AI MASTER', org, font,
 fontScale, color, thickness, cv2.LINE_AA)

# Відображення картинки
cv2.imshow('Ellipse', result)
# Чекаємо, поки користувач натисне будь-яку клавішу
# (це необхідно, щоб уникнути збою ядра Python)
cv2.waitKey(0)

# Закриваємо всі відкриті вікна
cv2.destroyAllWindows()