import streamlit as st
import pandas as pd
import os

cwd = os.getcwd()

df = pd.read_csv(cwd + f'\data\stats_all.csv', sep=",")

print(df.head(5))

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