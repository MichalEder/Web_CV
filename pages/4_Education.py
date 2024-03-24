import streamlit as st

from functions.general import read_resource
st.set_page_config(layout="wide")

st.title('Formal Education')

education = read_resource('resources/education.txt')


if education:
    for school in education:
        st.subheader(school['School'])
        st.write(school['Faculty'])
        st.write(f"Field of study: {school['Field of study']}")
        st.write(f"Duration of study: {school['Years']}")
        st.write(f"Status: {school['Status']}")

        st.write(school['Note'])

        st.markdown("---")  # Add a separator between experiences
else:
    st.write("No work experiences added yet.")

