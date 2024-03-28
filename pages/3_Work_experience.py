import streamlit as st
import sqlite3

from functions.display import display_work
from functions.db_interaction import read_resource
from functions.user_auth import get_authenticator, load_config


st.set_page_config(layout="wide")

config = load_config()
authenticator = get_authenticator(config)

st.title("My Professional Journey")
st.markdown("<br>", unsafe_allow_html=True)

try:
    work_experiences = read_resource('work_experience')
except sqlite3.Error as e:
    st.error(f"An error occurred while loading work experiences: {e}")

if work_experiences:
    for experience in work_experiences:
        display_work(experience)
else:
    st.write("No work experience information added yet.")

