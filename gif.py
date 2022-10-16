import os
import streamlit as st
import cv2
from PIL import Image
import imageio
import base64

st.title('')
ops=['Make Gif','See Gif']
choice=st.sidebar.selectbox('Select an option',ops)
if choice==ops[0]:
    filename = st.text_input('Enter a file name')
    btn = st.button('Open Camera')
    st.markdown('''
    Press A to start capturing frame \n
    Press Q for exit
    ''')
    if btn and filename:
        
        cap = cv2.VideoCapture(0)
        frames =[]
        image_count = 0

        while True:
            ret,frame = cap.read()
            cv2.imshow("frame", frame)

            Key = cv2.waitKey(0)
            if Key ==ord("a"):
                image_count += 1
                frames.append(frame)
            elif Key ==ord("q"):
                break
        print("Images added", len(frames))
        #2 save gif 
        print("Saving GIF file")
        with imageio.get_writer(f"{filename}.gif", mode='I') as writer:
            for idx, frame in enumerate(frames):
                print("Adding frame to GIF file:", idx+1)
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                writer.append_data(rgb_frame)

elif choice==ops[1]:
    files = os.listdir()
    gifs = [file for file in files if file.endswith('gif')]
    for gif in gifs:
        
        #st.markdown(f'''
        # <a href=f"{gif}"target="_main">f"{gif}"</a>
        # ''', unsafe_allow_html=True)
        #st.markdown(f'<img src=f"{gif}" alt="google"/></a>', unsafe_allow_html=True)

        file_=open(f"{gif}","rb")
        contents = file_.read()
        data_url= base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(f'<img src="data:image/gif;base64,{data_url}"/><pre>{gif}</pre>',
        unsafe_allow_html=True)