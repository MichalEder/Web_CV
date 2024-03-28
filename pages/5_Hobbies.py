import streamlit as st
import sqlite3

from functions.db_interaction import read_resource
from functions.user_auth import get_authenticator, load_config
from functions.display import display_hobby

st.set_page_config(layout="wide")

config = load_config()
authenticator = get_authenticator(config)

st.title('What I do for fun (and the unexpected skills I pick up)')
st.markdown("<br>", unsafe_allow_html=True)

try:
    hobbies = read_resource('hobby')
except sqlite3.Error as e:
    st.error(f"An error occurred while loading hobbies: {e}")

if hobbies:
    for hobby in hobbies:
        display_hobby(hobby)
else:
    st.write("No hobbies added yet.")
