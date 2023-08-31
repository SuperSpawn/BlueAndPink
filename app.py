import os
import time
from dotenv import load_dotenv
import streamlit as st

from reset import reset
from llm import create_episode

# config API stuff
try:
    load_dotenv('.env')
    api_key = os.getenv("OPENAI_API_KEY")

    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    else:
        print("API key not found in environment variable or .env file.")
except FileNotFoundError:
    api_key = os.getenv("OPENAI_API_KEY")

    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    else:
        print("API key not found in environment variable or .env file.")

reset()

st.title("Blue & Pink")

with st.form("create episode"):
    user_request = st.text_area("Special Request:")
    if st.form_submit_button("Create episode"):
        create_episode(user_request)

st.divider()

if st.button("Play Episode", disabled=st.session_state['playing']):
    st.session_state['playing'] = True
    st.session_state['index'] = 0

if st.session_state['playing']:
    scene = st.session_state['script'][st.session_state['index']]
    if "B" in scene['character']:
        st.image('./assets/blue.jpg')
    if "P" in scene['character']:
        st.image('./assets/pink.jpg')
    st.write(scene['text'])

    time.sleep(scene['length'])
    st.session_state['index'] += 1
    if st.session_state['index'] >= len(st.session_state['script']):
        st.session_state['playing'] = False
    st.experimental_rerun()
