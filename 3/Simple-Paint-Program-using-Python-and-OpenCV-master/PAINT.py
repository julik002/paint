# Импортируем необходимые библиотеки OpenCV и NumPy
import cv2
import numpy as np

# Название окна для рисования
windowName = 'PAINT'
# Создаем черное изображение размером 512x1024 пикселей с тремя цветовыми каналами (RGB)
img = np.zeros((512, 1024, 3), np.uint8)
# Создаем окно с указанным названием
cv2.namedWindow(windowName)

# Флаг, который показывает, нажата ли мышь (True - нажата, False - отпущена)
mousePressed = False
# Флаг, определяющий текущий режим рисования (True - рисуем прямоугольник, False - круги)
isRectangle = True
# Цвет по умолчанию (черный)
color = (0, 0, 0)


# Пустая функция для использования в трекбарах (заглушка)
def emptyFunc():
    pass


# Функция обратного вызова для обработки событий мыши
def draw_shape(event, x, y, flags, param):
    # Используем глобальные переменные
    global ix, iy, drawing, isRectangle, color

    # Если нажата левая кнопка мыши, начинаем рисовать
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        # Запоминаем начальные координаты
        (ix, iy) = x, y
    # Если мышь перемещается, проверяем, рисуем ли сейчас
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if isRectangle:
                # Рисуем прямоугольник
                cv2.rectangle(img, (ix, iy), (x, y), color, -1)
            else:
                # Рисуем круги (симуляция кисти)
                cv2.circle(img, (x, y), 3, color, -1)
    # Если левая кнопка мыши отпущена, заканчиваем рисование
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if isRectangle:
            # Завершаем рисование прямоугольника
            cv2.rectangle(img, (ix, iy), (x, y), color, -1)
        else:
            # Завершаем рисование круга
            cv2.circle(img, (x, y), 3, color, -1)


# Назначаем функцию обратного вызова на окно
cv2.setMouseCallback(windowName, draw_shape)

# Создаем три трекбара для выбора значений RGB
cv2.createTrackbar('Blue', windowName, 0, 255, emptyFunc)
cv2.createTrackbar('Green', windowName, 0, 255, emptyFunc)
cv2.createTrackbar('Red', windowName, 0, 255, emptyFunc)


# Основная функция программы
def main():
    global isRectangle
    global color
    while (True):
        # Отображаем изображение в окне
        cv2.imshow(windowName, img)
        if isRectangle:
            # Если режим прямоугольников активен
            text1 = " Drawing Rectangles."
            text2 = " Press 'M' to switch to PaintBrush."
        else:
            # Если активен режим кисти
            text1 = " Drawing with PaintBrush."
            text2 = " Press 'M' to draw Rectangles."

        # Отображаем текстовые инструкции на изображении
        cv2.rectangle(img, (0, 0), (512, 100), (0, 0, 0), -1)  # Черный фон для текста
        cv2.rectangle(img, (800, 25), (850, 75), color, -1)  # Отображаем текущий цвет
        cv2.putText(img, text1, (25, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
        cv2.putText(img, text2, (25, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))

        # Обрабатываем нажатие клавиш
        k = cv2.waitKey(1)
        if k == ord('m') or k == ord('M'):
            # Переключаем режим между прямоугольником и кистью
            isRectangle = not isRectangle
        elif k == 27:  # Нажатие 'Esc' для выхода
            break

        # Получаем значения цвета с трекбаров
        blue = cv2.getTrackbarPos('Blue', windowName)
        red = cv2.getTrackbarPos('Red', windowName)
        green = cv2.getTrackbarPos('Green', windowName)
        color = (blue, green, red)  # Устанавливаем текущий цвет

    # Закрываем все окна
    cv2.destroyAllWindows()


# Проверяем, запущена ли программа напрямую
if __name__ == '__main__':
    main()
