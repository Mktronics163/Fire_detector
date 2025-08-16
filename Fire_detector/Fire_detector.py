import cv2
import streamlit as st
import numpy as np
st.title("Fire detector")
fire_cascade = cv2.CascadeClassifier("fire_cascade.xml")
uploaded_file = st.file_uploader("Upload an image or Video",type=["jpg","jpeg","png","mp4"])
if uploaded_file is not None:
    if uploaded_file.type.startswith("image"):
        file_bytes = np.asarray(bytearray(uploaded_file.read()),dtype=np.uint8)
        img = cv2.imdecode(file_bytes,1)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        fire = fire_cascade.detectMultiScale(gray, 1.1, 5)
        for (x, y, w, h) in fire:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
        st.image(img,channels="BGR",caption="Detected Fire")
    elif uploaded_file.type.endswith("mp4"):
        tfile = open("temp_video.mp4","wb")
        tfile.write(uploaded_file.read())
        cap = cv2.VideoCapture("temp_video.mp4")
        stframe = st.empty()
        while True:
            _, frame = cap.read()
            if not _:
                break
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            fire = fire_cascade.detectMultiScale(gray,1.1,5)
            for (x, y, w, h) in fire:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
            stframe.image(frame,channels="BGR")

