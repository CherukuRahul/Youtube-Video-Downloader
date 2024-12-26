import streamlit as st

def display(vido):
    st.subheader("Title of the Video")
    st.write(vido.info.get('title'))
    st.subheader("Tags that are associate to the video")
    st.write(vido.tags)
    st.subheader("Thumbnail url of the video")
    st.write(vido.thumbnail)

    
