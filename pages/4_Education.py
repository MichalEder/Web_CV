import streamlit as st
import sqlite3

from functions.db_interaction import read_resource
from functions.user_auth import get_authenticator, load_config
from functions.display import display_education

st.set_page_config(layout="wide")

config = load_config()
authenticator = get_authenticator(config)

st.title('Formal Education')
st.markdown("<br>", unsafe_allow_html=True)

try:
    education = read_resource('education')
except sqlite3.Error as e:
    st.error(f"An error occurred while loading education information: {e}")

if education:
    for school in education:
        display_education(school)
else:
    st.write("No education information added yet.")


