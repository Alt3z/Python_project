import cv2

cap = cv2.VideoCapture(0)  # подключаемся к камере
count = 0
end = True

while end != False:
    ret, frame = cap.read()  # считываем кадр с камеры
    if ret:  # если кадр прочитан
        cv2.imwrite('frame%d.jpg' % count, frame)  # сохраняем кадр на диск
        count += 1
        if count == 10:
            end = False
    else:
        break

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # определяем кодек для записи видео
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    key = cv2.waitKey(1)  # ожидаем нажатия клавиши
    if key & 0xFF == ord('o'):
        break
    ret, frame = cap.read()  # считываем кадр с камеры
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cv2.CascadeClassifier('C:/Program Files/Python311/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml') # здесь нужно указать путь, где зранится файл haarcascade_frontalface_default.xml
        faces = faces.detectMultiScale(gray, 1.3, 5)  # обнаруживаем лица в кадре
        for (x, y, w, h) in faces:  # для каждого обнаруженного лица
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # рисуем прямоугольник вокруг лица
        out.write(frame)
    cv2.imshow('Video', frame)  # отображение текущего кадра

out.release()
