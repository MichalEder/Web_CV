import streamlit as st
from functions.general import read_resource

st.set_page_config(layout="wide")

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


skills = read_resource('skills')

col1, col2, col3 = st.columns([1, 1, 1])

if skills:
    for i, skill in enumerate(skills):
        column_index = i % 3  # Will cycle between 0, 1, and 2
        if column_index == 0:
            with col1:
                st.image(f"resources/images/{skill['Image']}", width=100)
                st.subheader(skill['Skill'])
                st.write(f"Level: {skill['Level']}")
                st.write(f"{skill['Description']}")
                st.write(' ')
                st.markdown("---")
        elif column_index == 1:
            with col2:
                st.image(f"resources/images/{skill['Image']}", width=100)
                st.subheader(skill['Skill'])
                st.write(f"Level: {skill['Level']}")
                st.write(f"{skill['Description']}")
                st.write(' ')
                st.markdown("---")
        else:
            with col3:
                st.image(f"resources/images/{skill['Image']}", width=100)
                st.subheader(skill['Skill'])
                st.write(f"Level: {skill['Level']}")
                st.write(f"{skill['Description']}")
                st.write(' ')
                st.markdown("---")

