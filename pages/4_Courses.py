import streamlit as st
import sqlite3
from functions.general import read_resource

st.set_page_config(layout="wide")


st.title("Courses Completed and In Progress")
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
        with st.container():
            col1, col2 = st.columns([1, 3])

            with col1:
                st.image(f"resources/images/{course['image']}", width=None)

            with col2:
                st.subheader(course['course'])
                st.write(course['provider'])
                st.write(f"Completed: {course['date_of_compl']}")
                st.write(f"Course type: {course['course_type']}")
                st.markdown(f"[Link to Course]({course['link_to_course']})")
                st.write(course['description'])
                st.markdown("---")
                st.markdown("<br>", unsafe_allow_html=True)