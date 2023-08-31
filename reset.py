import streamlit as st
import pyttsx3


def reset():
    if 'script' not in st.session_state:
        st.session_state['script'] = {}
    if 'playing' not in st.session_state:
        st.session_state['playing'] = False
    if 'scene_index' not in st.session_state:
        st.session_state['scene_index'] = 0
    if 'text_speech' not in st.session_state:
        text_speech = pyttsx3.init()


__all__ = ['reset']
