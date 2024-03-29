import streamlit as st
import sqlite3

from functions.db_interaction import read_resource
from functions.display import display_course
from functions.user_auth import get_authenticator, load_config

st.set_page_config(layout="wide")

config = load_config()
authenticator = get_authenticator(config)

st.title("Courses Completed and In Progress")
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
I'm always looking for ways to gain knowledge and abilities that will make a positive impact. 
My learning journey is driven by a deep passion for personal and professional growth. 
Here's a snapshot of the courses I'm actively pursuing:
""")
st.markdown("<br>", unsafe_allow_html=True)

try:
    courses = read_resource('courses')
except sqlite3.Error as e:
    st.error(f"An error occurred while loading work experiences: {e}")

if courses:
    for course in courses:
        display_course(course)
else:
    st.write("No courses information added yet.")
