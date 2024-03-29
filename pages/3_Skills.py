import streamlit as st
import sqlite3


from functions.db_interaction import read_resource
from functions.user_auth import get_authenticator, load_config
from functions.display import display_skill

st.set_page_config(layout="wide")

config = load_config()
authenticator = get_authenticator(config)

st.markdown("""
<style>

[data-testid="stImage"] img {
    max-width: 100px;
    height: 100px;
    object-fit: scale-down;
}
</style>
""", unsafe_allow_html=True)

st.title("The tools in my ever-evolving toolkit")
st.markdown("<br>", unsafe_allow_html=True)

try:
    skills = read_resource('skills')
except sqlite3.Error as e:
    st.error(f"An error occurred while loading skills: {e}")


col1, col2, col3 = st.columns([1, 1, 1])

if skills:
    for i, skill in enumerate(skills):
        column_index = i % 3
        if column_index == 0:
            with col1:
                display_skill(skill)
        elif column_index == 1:
            with col2:
                display_skill(skill)
        else:
            with col3:
                display_skill(skill)
