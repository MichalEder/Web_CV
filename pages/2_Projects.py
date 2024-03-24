import streamlit as st
from functions.general import read_resource

st.set_page_config(layout="wide")

st.title("Putting my skills to work.")
st.markdown("<br>", unsafe_allow_html=True)
projects = read_resource('resources/projects.txt')

if projects:
    for project in projects:
        with st.container():
            col1, col2 = st.columns([1, 6])
            with col1:
                st.image(f"resources/images/{project['Image']}", use_column_width='auto')

            with col2:
                st.subheader(project['Project'])
                st.write(f"Technologies: {project['Tech']}")
                st.write(f"{project['Description']}")
                st.write(f"{project['Link']}")
                st.markdown("---")
                st.markdown("<br>", unsafe_allow_html=True)

