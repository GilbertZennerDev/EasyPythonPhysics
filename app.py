import streamlit as st
import subprocess as sp
import re
import random
import zipfile
import io

st.markdown(
    """
    <style>
    .stApp {
        color: #01257D;
        background: linear-gradient(to bottom right, #111439, #00FFFF, #BFA181);
    }
    /* Style the actual Streamlit button */
    .stButton > button {
        background: linear-gradient(to bottom right, #111439, #178582, #BFA181);
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5em 2em;
        font-size: 1.1em;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton > button:hover {
        filter: brightness(1.1);
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)

stage = []
for i in range(1, 5, 1):
    with open(f"5_Stages/stage{i}.py", "r") as file:
    stage.append(file.read())
    
# Provide separate download buttons for each .py file
st.download_button(
    label="Download stage1.py",
    data=stage1,
    file_name="stage1.py",
    mime="text/x-python"
)

st.download_button(
    label="Download file2.py",
    data=file2content,
    file_name="file2.py",
    mime="text/x-python"
)