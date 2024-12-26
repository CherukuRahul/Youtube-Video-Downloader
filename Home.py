import streamlit as st
import yt_dlp
import  About, Advanced
import Ytdownloader
import random

# Helper Function for Displaying Formats
def display_formats(formats, type):
    list_count = len(formats)
    rows = [st.columns(4) for _ in range(4)]  # Create grid rows
    count = 0

    for row in rows:
        for col in row:
            if count >= list_count:
                break

            format_info = formats[count]
            resolution = format_info.get('format_note', 'Unknown')
            link = format_info.get('url', '#')

            with col.container(height=180):
                st.subheader(f':violet[{resolution}] resolution', anchor=False)
                st.link_button('Download', link)

            count += 1


# App Title
st.title("YouTube Video Downloader :rocket:")

# Tabs for navigation
tab2, tab1, tab3, = st.tabs(["About", "Downloads","Advanced Info"])

# Home Tab
with tab1:
    st.markdown(''' 
    Welcome to the easiest and fastest YouTube Downloader! Whether you want to save your favorite music videos, 
    tutorials, or entertainment clips, we’ve got you covered.

    :blue_background[With our tool, you can:]

    - :fish_cake: Download videos in high quality.
    - :fish_cake: Choose from multiple formats, including MP4, MP3, and more.
    - :fish_cake: Enjoy lightning-fast downloads without any delays.
    ''')
    
    url = st.text_input("Enter the YouTube Link :link:")
    
    left, right, bottom = st.columns(3)
    if right.button("Fetch", use_container_width=True):

        if url == '':
            st.write("Please fill the url to fetch the details")
        else :
        # Fetch video details
            video = Ytdownloader.Ytdownloader(url)
            imglink = video.thumbnail
        
        # Display thumbnail
            if imglink:
                st.image(imglink, use_column_width=True)
            else:
                st.info("No image available.")
        
        # Video Formats Section
            st.subheader("Video Format Links :clapper:")
            res = video.video_format
            display_formats(res, "Video")
        
        # Audio Formats Section
            st.subheader("Audio Format Links :notes:")
            res = video.audio_format
            display_formats(res, "Audio")

        # Audio and Video Formats Section
            st.subheader("Audio and Video Format Links :carousel_horse:")
            res = video.both
            display_formats(res,'AudionVideo')

            st.success("Click on the Download button for the respective resolution to download.")

with tab2:
    About.display()

with tab3:
    tab_link = st.text_input("Enter the url of your video :link:")
    
    left, right, bottom = st.columns(3)
    if right.button("Enter", use_container_width=True):

        if tab_link == '':
            st.write("Please fill the url to fetch the details")
        else :
            video = Ytdownloader.Ytdownloader(tab_link)
            Advanced.display(vido=video)
    
