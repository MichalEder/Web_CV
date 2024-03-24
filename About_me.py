import streamlit as st
st.set_page_config(layout="wide")
st.title("Hi there! Welcome to my corner of the web.")
col1, col2 = st.columns([1,1])


with col1:
    st.header("About Me")
    st.write("I'm Michal Eder, and I\'m excited to share my projects, ideas, and maybe a few random thoughts with you.")
    st.header("Languages")
    st.write("Hi there! Welcome to my corner of the web. I'm Michal Eder, and I\'m excited to share my projects, ideas, and maybe a few random thoughts with you.")

    st.header("Contact")
    st.write("Phone: +420 602 680 577")
    st.write("Email: edermichal.eder@gmail")
    st.write("[GitHub](https://www.linkedin.com/in/michal-eder-447049272/) ")
    st.write("[LinkedIn](https://www.linkedin.com/in/michal-eder-447049272/)")

with col2:
    st.image('resources/images/profile.jpg', width=300)