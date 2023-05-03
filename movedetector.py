import random
import cv2


capture = cv2.VideoCapture(0)
# счетчик с начальным значением
count = 0
# рандомные заготовки для снимков и кадров
f = random.randint(0, 240)
f_1 = random.randint(0, 320)
# для сохранения видео
frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (frame_width, frame_height)
# output = cv2.VideoWriter(
#     'two.avi', cv2.VideoWriter_fourcc(*'XVID'), 20, size)

while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        # создаем счетчик, по которому будет делаться фото с камеры,
        # для сравнения с кадрами фотопотока
        center_img = frame[120:360, 160:480]
        if count == 0 or count % 2 == 0:
            screen = cv2.imwrite('one.jpg', center_img)
        count += 1
        # подгружаем ранее созданный снимок и выставляем область интереса
        img = cv2.imread('one.jpg')
        # для снимка - будем отслеживать пиксели по зеленому цвету(G)
        now_img = (img[0][f_1])[1]
        now_img_2 = (img[1][f_1])[1]

        # выставляем область интереса для кадра
        gray_1 = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        gray = cv2.cvtColor(gray_1, cv2.COLOR_GRAY2RGB)
        center = gray[120:360, 160:480]
        # для кадра - будем отслеживать пиксели по зеленому цвету(G)
        now = (center[0][f])[1]
        now_2 = (center[1][f_1])[1]

        # выставляем границы для зеленого цвета(G),
        # при выходе за которые будет срабатывать "датчик"
        if now in range(now_img - 20, now_img + 20):
            if now_2 in range(now_2 - 20, now_2 + 20):
                print(f'OK')
        else:
            frame[120:360, 160:480] = center
            cv2.rectangle(frame, (160, 120), (480, 360), (0, 255, 255), 2)

        # вызов видеопотока
        cv2.imshow('Look', frame)
        # экстренная кнопка остановки и кнопка "фото экрана"(просто для интереса)
        key = cv2.waitKey(20)
        if key == ord('q') or key == 27:
            break
        elif key == ord('p'):
            img = cv2.imwrite('filename.jpg', frame)
            print("You just took a picture: ", img)
    else:
        break

capture.release()
# output.release()
cv2.destroyAllWindows()
