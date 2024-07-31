import streamlit as st
import pandas as pd
st.subheader('Loading the CSV File')

df = st.file_uploader("Upload the CSV file : ", type = ['csv','xlsx'])

df = pd.read_csv('Products.csv')
st.table(df.head())

st.subheader('Dealing with images')
st.image('img.png')


st.subheader('Working with Images')
img_file = st.file_uploader("Upload the image file: ", type = ['png','jpeg'])
if img_file is not None:
    st.image(img_file)
    
    

st.subheader('Working with Videos')
video_file = st.file_uploader("Upload the Videos file: ", type = ['mkv','mp4'])
if video_file is not None:
    st.video(video_file)
    
st.subheader('Working with Audio')
audio_file = st.file_uploader("Upload the Audio file: ", type = ['mp3'])
if audio_file is not None:
    st.audio(audio_file)
