import streamlit as st

from functions.db_interaction import read_resource
from functions.user_auth import get_authenticator, load_config
from functions.display import display_project
import sqlite3

st.set_page_config(layout="wide")

config = load_config()
authenticator = get_authenticator(config)

st.title("Putting my skills to work.")
st.markdown("<br>", unsafe_allow_html=True)

try:
    projects = read_resource('projects')
except sqlite3.Error as e:
    st.error(f"An error occurred while loading projects: {e}")

if projects:
    for project in projects:
        display_project(project)
