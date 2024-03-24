import streamlit as st
from functions.general import read_resource

st.set_page_config(layout="wide")

st.title("My Professional Journey")
st.write('''

''')
work_experiences = read_resource('resources/work_experience.txt')

if work_experiences:
    for experience in work_experiences:
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(f"resources/images/{experience['Image']}", width=None)

            with col2:
                st.subheader(experience['Company'])
                st.write(f"Role: {experience['Position/Role']}")
                st.write(f"Duration: {experience['Start Date']} - {experience['End date']}")
                st.write(f"Hard Skills: {experience['Hard Skills']}")
                st.write(f"Soft Skills: {experience['Soft Skills']}")
                st.write(f"{experience['Description']}")
                st.markdown("---")