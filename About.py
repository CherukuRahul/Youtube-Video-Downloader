import streamlit as st
import sys

sys.stdout.reconfigure(encoding='utf-8') 

def display():
    st.markdown("""
## Welcome to Youtube Video Downloader!

Our mission is to provide you with a simple, fast, and reliable way to download your favorite YouTube videos effortlessly. Whether you're saving videos for offline viewing, archiving educational content, or creating playlists for on-the-go access, our tool is designed to meet your needs with just a few clicks.

With a focus on user experience, security, and versatility, [Your Application Name] supports a wide range of formats and resolutions, ensuring that you can download videos in the way that works best for you.

Start exploring today and make your video downloading experience seamless and hassle-free!
""")
    left, right, bottom = st.columns(3)
    right.image("Youtube.png", caption="Youtube Video Downloader")
    st.subheader("Features:")
    st.write("""
    - Easy-to-use interface for data exploration.
    - Interactive plots for data visualization.
    - Supports custom machine learning models.
    - Real-time updates and performance tracking.
        """)
    st.subheader("Developer Information:")
    st.write("""
    This app was developed by Cheruku Rahul.
    Contact: cherukurahul01@gmail.com
    """)
    left, right, bottom = st.columns(3)
    right.image("Developer.png", caption="Developer")
    
 


    