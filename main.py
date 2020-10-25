import cv2
import numpy as np
import dlib
import winsound
import random
import datetime
import keyboard

cap = cv2.VideoCapture('test1.mp4') ##---change

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
noAttentionFrameNum = 0
t=datetime.datetime.now()
open('dump.txt', 'w').close()

while True:
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = detector(gray)
        isItFace= len(faces)

        ##Proverava da li se na ekranu nalazi lice, ukoliko ne, puni counter koji nam
        if isItFace == 0:
                noAttentionFrameNum+=1

        for face in faces:

                x1 = face.left()
                y1 = face.top()
                x2 = face.right()
                y2 = face.bottom()

                landmarks = predictor(gray, face)

                ##Pracenje FaceMap vrednosti, koja je dostupna na gitu u svrhu odrednjivanja polozaja lica
                #position-33
                xposCrit33= landmarks.part(33).x
                yposCrit33 = landmarks.part(33).y
                #position-1
                xposCrit1 = landmarks.part(1).x
                yposCrit1 = landmarks.part(1).y
                #position-15
                xposCrit15 = landmarks.part(15).x
                yposCrit15 = landmarks.part(15).y

                if(xposCrit33==xposCrit1 or yposCrit33==yposCrit1 or xposCrit33==xposCrit15 or yposCrit33==yposCrit15):
                        winsound.PlaySound('glas' + voiceNum.__str__() + '.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)

                print(face)
                
                for i in range(0,68):
                        x = landmarks.part(i).x
                        y = landmarks.part(i).y
                        cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)

        cv2.imshow("Frame 1", frame)

        voiceNum = random.randint(1, 7) #random broj od 1-7 radi biranja random glasovnog fajla.
        if(noAttentionFrameNum>12):
                winsound.PlaySound('glas' + voiceNum.__str__() + '.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
                t1=datetime.datetime.now()
                d=t1-t
                f = open("dump.txt", "a")
                f.write(str(d)+"\n")
                f.close()
                noAttentionFrameNum=0

        key = cv2.waitKey(1)
        if key == 27:
                break
        if keyboard.is_pressed('esc'):
                break
