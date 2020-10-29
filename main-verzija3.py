import cv2
import numpy as np
import dlib
import winsound
import random
import datetime
import keyboard
import time
import csv
import matplotlib.pyplot as plt


cap = cv2.VideoCapture(0)  ##---change6

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
t = datetime.datetime.now()
open('dump.txt', 'w').close()  ####################################Timestamp fajl

entry1 = 1
entry2 = 1
start = 0.0
sekunde=""
nepaznja=""


while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    isItFace = len(faces)
    voiceNum = random.randint(1, 7)  # random broj od 1-7 radi biranja random glasovnog fajla.

    #####################################PROVERAVA DA LI JE LICE U VIEWFIELDU, AKO NIJE, BROJI VREME###################
    if isItFace == 0 and entry1 == 1:
        entry1 = 0
        start = time.time()
        print('ne prati')

    if isItFace == 1:
        fa = open("nepaznja.txt", "a")
        fa.write("0" + "\n")
        ###################################################################################################################

    if isItFace == 1:
        start = time.time()

    for face in faces:

        ####################################NALAZI LICE POMOCU DLIB-a###################################################
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        ###############################################################################################################
        landmarks = predictor(gray, face)

        ##########Pracenje FaceMap vrednosti, koja je dostupna na gitu u svrhu odrednjivanja polozaja lica#############
        # position-33
        xposCrit33 = landmarks.part(33).x
        yposCrit33 = landmarks.part(33).y
        # position-1
        xposCrit1 = landmarks.part(1).x
        yposCrit1 = landmarks.part(1).y
        # position-15
        xposCrit15 = landmarks.part(15).x
        yposCrit15 = landmarks.part(15).y
        # position-2
        xposCrit2 = landmarks.part(2).x
        yposCrit2 = landmarks.part(2).y
        # position-14
        xposCrit14 = landmarks.part(14).x
        yposCrit14 = landmarks.part(14).y
        ##############################################################################################################

        ############################PROVERAVA VREDNOSTI I POKLAPANJE KRITICNIH TACAKA LICA############################
        if (xposCrit33 == xposCrit1) or \
                (xposCrit33 == xposCrit15) or \
                (xposCrit33 == xposCrit2 and yposCrit33 == yposCrit2) or \
                (xposCrit33 == xposCrit14 and yposCrit33 == yposCrit14):
            winsound.PlaySound('glas' + voiceNum.__str__() + '.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
            t1 = datetime.datetime.now()
            d = t1 - t
            f = open("dump.txt", "a")
            ###
            fa = open("nepaznja.txt", "a")
            fa.write("10" + "\n")
            f.write(str(d) + "\n")
            f.close()
        else:
            fa = open("nepaznja.txt", "a")
            fa.write("0" + "\n")

        ###############################################################################################################
        print(face)
        ##############################################68 landmarks na licu, fajl FaceMap.png##########################
        for i in range(0, 68):
            x = landmarks.part(i).x
            y = landmarks.part(i).y
            cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)

    cv2.imshow("Frame 1", frame)

    #######################################PROVERAVA VREME PROVEDENO VAN VIEWFIELDA####################################
    if time.time() - start > 3:  ##CHANGE!
        winsound.PlaySound('glas' + voiceNum.__str__() + '.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        t1 = datetime.datetime.now()
        d = t1 - t
        f = open("dump.txt", "a")
        fa = open("nepaznja.txt", "a")
        fa.write("10" + "\n")
        f.write(str(d) + "\n")
        f.close()
        entry1 = 1

    ####################################################################################################################

    key = cv2.waitKey(1)
    if key == 27:
        break
    if keyboard.is_pressed('esc'):
        break
fan = open('dump.txt', 'r')
sines = fan.readlines()

for line in sines:
    sekunde = line.strip()

fan2 = open('nepaznja.txt', 'r')
sin = fan2.readlines()

for li in sin:
    nepaznja = li.strip()



plt.plot(sekunde, nepaznja, color='green', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='blue', markersize=12)
plt.xlabel('sekunde')
plt.ylabel('nepaznja')
plt.show()



