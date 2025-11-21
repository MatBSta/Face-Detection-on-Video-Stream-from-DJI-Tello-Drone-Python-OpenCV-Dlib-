# Zaimportowanie potrzebnych bibliotek
import cv2
import numpy as np
import dlib
import time

# Pobranie wprowadzanych danych od użytkownika 
cap = cv2.VideoCapture('test.mp4')

# Wywołanie funkcji służącej do detekcji twarzy
hogFaceDetector = dlib.get_frontal_face_detector()

# Zmienna zliczająca zdjęcia 
countPhoto=0
# Ustalenie typu czcionki
font = cv2.FONT_HERSHEY_PLAIN
starting_time = time.time()
frame_id = 0

# Główna pętla programu
while True:

# Pobranie danych w formie klatek filmu
    _, frame = cap.read()
    frame_id += 1
# Konwersja kolorów
    frameDlibHog=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# Wprowadzenie obrazku do detektora twarzy, drugi argument '0'
# stanowi zmienną odwołującą się do ilości powitórzeń skanowania obrazu
    faces = hogFaceDetector(frameDlibHog,0)

# Wyznaczenie z wykrytych twarzy ich pozycji w układzie x,y
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

# Wpisanie wykrytych twarzy w kwadrat
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
        print('[ {} left , {} top ] , [ {} right, {} bottom]'.format(x1,y1,x2,y2))   
    elapsed_time = time.time() - starting_time
    fps = frame_id / elapsed_time
    cv2.putText(frame, "HOG, FPS: " + str(round(fps, 2)), (10, 20), font, 1, (0, 0, 255), 2)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)

    if key==27:
        break
    elif key==32:
        screenShot="Zrzut_z_ekranu_{}_nr_{}.png".format(cap,countPhoto)
        cv2.imwrite(screenShot,frame)
        print("{} Zapisano".format(screenShot))
        countPhoto+=1
# Zakończenie pracy algorytmu  
cap.release()
# Zamknięcie wykorzystywanych okien
cv2.destroyAllWindows()