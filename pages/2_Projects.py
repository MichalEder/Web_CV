import streamlit as st
from functions.general import read_resource
import sqlite3

st.set_page_config(layout="wide")

st.title("Putting my skills to work.")

try:
    projects = read_resource('projects')
except sqlite3.Error as e:
    st.error(f"An error occurred while loading projects: {e}")

if projects:
    for project in projects:
        with st.container():
            col1, col2 = st.columns([1, 6])
            with col1:
                st.image(f"resources/images/{project['Image']}", width=200)  # Control image size

            with col2:
                st.subheader(project['Project'])
                st.write(f"Technologies: {project['Tech']}")
                st.write(project['Description'])
                if 'Link' in project and project['Link'].startswith('http'):
                    st.markdown(f"[Link]({project['Link']})")
                else:
                    st.write(f"{project['Link']}")
                st.markdown("---")