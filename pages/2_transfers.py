import streamlit as st
import os

st.set_page_config(
    page_title="Robo Trener",
    page_icon='soccer',
    # layout="wide",
    initial_sidebar_state="auto",
    menu_items=None
    )

col1, col2 = st.columns([1, 3])

with col1:
    st.image('images/esa-logo.jpg')

with col2:
    """
          # Robo trener 

          ### Co chcesz by Robo Trener zrobił? 
          Wybierz opcje po lewej stronie.
          Robo Trener może Ci pomóc:
          - wybrać nową drużynę;
          - dokonać transferów.

          ---  
    """