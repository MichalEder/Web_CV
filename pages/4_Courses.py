import streamlit as st
from functions.general import read_resource

st.set_page_config(layout="wide")


st.title("Courses Completed and In Progress")
st.write("I\'m always looking for ways to gain knowledge and abilities that will make a positive impact. My learning journey is driven by a deep passion for personal and professional growth. Here's a snapshot of the courses I'm actively pursuing for that purpose:")
st.markdown("<br>", unsafe_allow_html=True)

courses = read_resource('resources/courses.txt')

if courses:
    for course in courses:
        with st.container():
            col1, col2 = st.columns([1, 3])  # Adjust column ratios as needed

            with col1:
                st.image(f"resources/images/{course['image']}", width=None)

            with col2:
                st.subheader(course['course'])
                st.write(course['provider'])
                st.write(f"Completed: {course['date_of_compl']}")
                st.write(f"Course type: {course['course_type']}")
                st.write(f"Link: {course['link_to_course']}")
                st.write(course['description'])
                st.markdown("---")  # Add a separator between experiences