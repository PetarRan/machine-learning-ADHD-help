import cv2
import numpy as np
import dlib
import winsound
import random
import datetime
import keyboard
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

with open('attention_time_file.cvs', 'w') as fa:
    writer = csv.writer(fa)
    writer.writerow(["Time[min]"])

cap = cv2.VideoCapture(0)  ##---change

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
t = datetime.datetime.now()

  ####################################Timestamp fajl
entry1 = 1
entry2 = 1
start = 0.0

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
        ###################################################################################################################

    if isItFace==1:
        start=time.time()


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
        # position-1
        xposCrit1 = landmarks.part(1).x
        # position-15
        xposCrit15 = landmarks.part(15).x
        # position-2
        xposCrit2 = landmarks.part(2).x
        # position-14
        xposCrit14 = landmarks.part(14).x
        # postion-3
        xposCrit3 = landmarks.part(3).x
        # position-13
        xposCrit13 = landmarks.part(13).x
        ##############################################################################################################

        #################### Pracenje Facemap Vrednosti za preklapanje tacaka na ocima ################################
        yposCrit37 = landmarks.part(37).y
        yposCrit38 = landmarks.part(38).y
        yposCrit40 = landmarks.part(40).y
        yposCrit41 = landmarks.part(41).y
        yposCrit43 = landmarks.part(43).y
        yposCrit44 = landmarks.part(44).y
        yposCrit46 = landmarks.part(46).y
        yposCrit47 = landmarks.part(47).y
        ###############################################################################################################

        ############################PROVERAVA VREDNOSTI I POKLAPANJE KRITICNIH TACAKA LICA############################
        if (xposCrit33 == xposCrit1) or (xposCrit33 == xposCrit3) or (xposCrit33 == xposCrit2) or \
                (xposCrit33 == xposCrit15) or (xposCrit33 == xposCrit14) or (xposCrit33 == xposCrit13) or \
                (yposCrit37 == yposCrit41) or (yposCrit38 == yposCrit40) or \
                (yposCrit43 == yposCrit47) or (yposCrit44 == yposCrit46):
            winsound.PlaySound('glas' + voiceNum.__str__() + '.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
            t1 = datetime.datetime.now()
            delta_time = t1 - t
            sec = delta_time.seconds
            sec=sec/60

            with open('attention_time_file.cvs', 'a') as fa:
                writer = csv.writer(fa)
                writer.writerow([int(sec)])




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
        delta_time = t1 - t
        entry1 = 1
        sec = delta_time.seconds
        sec=sec/60

        with open('attention_time_file.cvs', 'a') as fa:
            writer = csv.writer(fa)
            writer.writerow([int(sec)])

    ####################################################################################################################
    key = cv2.waitKey(1)
    if key == 27:
        break
    if keyboard.is_pressed('esc'):
        break


df = pd.read_csv('attention_time_file.cvs', usecols=["Time[min]"])


secon = df["Time[min]"]
range = (0, 45)
bins = 15

plt.hist(secon, bins, range, color='green',
         histtype='bar', rwidth=0.8)

plt.xlabel('Time in minutes')
plt.ylabel('No. of no attention')
plt.title('Attention histogram')
plt.show()
