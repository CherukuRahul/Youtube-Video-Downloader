import streamlit as st
import yt_dlp
import Format
import Ytdownloader

st.title("YouTube Video Downloader :rocket: ")

tab1, tab2, tab3 = st.tabs(["Home", "About", "Help"])

with tab1 :
    st.markdown(''' Welcome to the easiest and fastest YouTube Downloader! Whether you want to save your favorite music videos, tutorials, or entertainment clips, we’ve got you covered.

:blue-background[With our tool, you can:]

 :fish_cake: Download videos in high quality.
                
 :fish_cake: Choose from multiple formats, including MP4, MP3, and more.
                
 :fish_cake: Enjoy lightning-fast downloads without any delays
                 ''')
    url = st.text_input("Enter the Youtbe Link :link:")
    
    left, right, bottom = st.columns(3)
    if right.button("Fetch", use_container_width=True) :
        video = Ytdownloader.Ytdownloader(url)
        imglink = video.thumbnail
        if imglink:
            st.image(imglink,use_column_width=True)
        else:
            st.info("No image available.")
        
        left1, right1, bottom1 = st.columns(3)
        with right1:
            st.image(r'C:\Users\cherur\Desktop\Yt_downloader\Video.png', caption='Video Format Links', use_column_width=True)
        res = video.video_format
        listCount = len(res)
        row1 = st.columns(4)
        row2 = st.columns(4)
        row3 = st.columns(4)
        row4 = st.columns(4)
        count = 0 
        for col in row1 + row2 + row3 + row4 :

            if count >= listCount :
                break

            tile = col.container(height= 200)


            if count < listCount :
                reso = res[count].get('format_note')
                link = res[count].get('url')
                tile.subheader(f':violet[{reso}] resolution',anchor= False )
                tile.html(
                    f"""
                    <a href="{link}" style="
                        display: inline-block;
                        padding: 10px 20px;
                        background-color: #007BFF;
                        color: white;
                        text-decoration: none;
                        border-radius: 5px;
                        font-size: 16px;
                        text-align: center;
                        border: none;
                        cursor: pointer;
                    ">Download</a>
                                """
                        )

            count = count+1 

        left2, right2, bottom2 = st.columns(3)
        with right2:
            st.image(r'C:\Users\cherur\Desktop\Yt_downloader\Audio.png', caption='Audio Format Links', use_column_width=True)
        res = video.audio_format
        listCount = len(res)
        row1 = st.columns(4)
        row2 = st.columns(4)
        row3 = st.columns(4)
        row4 = st.columns(4)
        count = 0 
        for col in row1 + row2 + row3 + row4 :

            if count >= listCount :
                break

            tile = col.container(height= 200)


            if count < listCount :
                reso = res[count].get('format_note')
                link = res[count].get('url')
                tile.subheader(f':violet[{reso}] resolution',anchor= False )
                tile.html(
                    f"""
                    <a href="{link}" style="
                        display: inline-block;
                        padding: 10px 20px;
                        background-color: #007BFF;
                        color: white;
                        text-decoration: none;
                        border-radius: 5px;
                        font-size: 16px;
                        text-align: center;
                        border: none;
                        cursor: pointer;
                    ">Download</a>
                                """
                        )

            count = count+1 
        st.success("Click on Download button over the respective resolution to download")


    
