import streamlit as st
from functions.general import read_resource
import sqlite3

st.set_page_config(layout="wide")

st.title('Formal Education')

try:
    education = read_resource('education')
except sqlite3.Error as e:
    st.error(f"An error occurred while loading education information: {e}")

if education:
    for school in education:
        st.subheader(school['School'])
        st.write(school['Faculty'])
        st.write(f"Field of study: {school['Field']}")
        st.write(f"Duration of study: {school['Years']}")
        st.write(f"Status: {school['Status']}")
        st.write(school['Note'])
        st.markdown("<br>", unsafe_allow_html=True)  # Spacing
        st.markdown("---")
else:
    st.write("No education information added yet.")

