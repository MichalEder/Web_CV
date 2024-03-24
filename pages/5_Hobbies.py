import streamlit as st

from functions.general import read_resource
st.set_page_config(layout="wide")


st.title('What I do for fun (and the unexpected skills I pick up).')
st.markdown("<br>", unsafe_allow_html=True)


hobbies = read_resource('resources/hobby.txt')
if hobbies:
    for hobby in hobbies:

        with st.container():
            st.subheader(f"{hobby['Hobby']}")
            col1, col2 = st.columns([1,5])

            with col1:

                st.image(f"resources/images/{hobby['Image']}")

            with col2:

                st.markdown(f"{hobby['Description']}")
        st.markdown("---")