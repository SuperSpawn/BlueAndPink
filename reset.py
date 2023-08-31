import streamlit as st


def reset():
    if 'script' not in st.session_state:
        st.session_state['script'] = {}
    if 'playing' not in st.session_state:
        st.session_state['playing'] = False
    if 'scene_index' not in st.session_state:
        st.session_state['scene_index'] = 0


__all__ = ['reset']
