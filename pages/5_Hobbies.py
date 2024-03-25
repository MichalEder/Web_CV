import streamlit as st
import sqlite3
from functions.general import read_resource

st.set_page_config(layout="wide")

st.title('What I do for fun (and the unexpected skills I pick up)')

try:
    hobbies = read_resource('hobby')
except sqlite3.Error as e:
    st.error(f"An error occurred while loading hobbies: {e}")

if hobbies:
    for hobby in hobbies:
        with st.container():
            st.subheader(f"{hobby['Hobby']}")
            col1, col2 = st.columns([1, 5])

            with col1:
                st.image(f"resources/images/{hobby['Image']}", width=200)

            with col2:
                st.markdown(f"{hobby['Description']}")
        st.markdown("---")
