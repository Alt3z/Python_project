import cv2

cap = cv2.VideoCapture(0)  # Подключаемся к камере
count = 0
end = True

while end != False:
    ret, frame = cap.read()  # Считываем кадр с камеры
    if ret:  # Если кадр прочитан
        cv2.imwrite('frame%d.jpg' % count, frame)  # Сохраняем кадр на диск
        count += 1
        if count == 10:
            end = False
    else:
        break


fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Определяем кодек для записи видео
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    key = cv2.waitKey(1)  # Ожидаем нажатия клавиши
    if key & 0xFF == ord('o'):
        break
    ret, frame = cap.read()  # Считываем кадр с камеры
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cv2.CascadeClassifier('C:/Program Files/Python311/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
        faces = faces.detectMultiScale(gray, 1.3, 5)  # Обнаруживаем лица в кадре
        for (x, y, w, h) in faces:  # Для каждого обнаруженного лица
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Рисуем прямоугольник вокруг лица
        out.write(frame)

    cv2.imshow('Video', frame)  # Отображение текущего кадра

out.release()