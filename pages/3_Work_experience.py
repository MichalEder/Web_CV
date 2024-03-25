import streamlit as st
import sqlite3
from functions.general import read_resource


st.set_page_config(layout="wide")

st.title("My Professional Journey")
st.markdown("<br>", unsafe_allow_html=True)

try:
    work_experiences = read_resource('work_experience')
except sqlite3.Error as e:
    st.error(f"An error occurred while loading work experiences: {e}")

if work_experiences:
    for experience in work_experiences:
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(f"resources/images/{experience['Image']}", width=None)

            with col2:
                st.subheader(experience['Company'])
                st.write(f"Role: {experience['Position_Role']}")
                st.write(f"Duration: {experience['Start_Date']} - {experience['End_date']}")


                st.markdown("<br>", unsafe_allow_html=True)

                st.write(f"Skills: {experience['Skills']}")
                st.write(f"Tools: {experience['Tools']}")
                st.write(f"{experience['Description']}")

                st.markdown("---")
                st.markdown("<br>", unsafe_allow_html=True)