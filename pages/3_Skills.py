import streamlit as st
from functions.general import read_resource

st.set_page_config(layout="wide")

st.markdown("""
<style>

[data-testid="stImage"] img { /* Styling for images */
    max-width: 100px;
    height: 100px;
    object-fit: scale-down;
}
</style>
""", unsafe_allow_html=True)

st.title("The tools in my ever-evolving toolkit")
st.markdown("<br>", unsafe_allow_html=True)


skills = read_resource('resources/skills.txt')

col1, col2, col3 = st.columns([1,1,1])
st.columns([1 for item in skills])
if skills:
    for skill in skills:
        match skills.index(skill) + 1:
            case 1 | 4 | 7 | 10:
                with col1:
                    st.image(f"resources/images/{skill['Image']}", width=200)
                    st.subheader(skill['Skill'])
                    st.write(f"Level: {skill['Level']}")
                    st.write(f"{skill['Description']}")
                    st.write(' ')
                    st.markdown("---")
            case 2 | 5 | 8 | 11:
                with col2:
                    st.image(f"resources/images/{skill['Image']}", width=200)
                    st.subheader(skill['Skill'])
                    st.write(f"Level: {skill['Level']}")
                    st.write(f"{skill['Description']}")
                    st.write(' ')
                    st.markdown("---")
            case 3 | 6 | 9 | 12:
                with col3:
                    st.image(f"resources/images/{skill['Image']}", width=150)
                    st.subheader(skill['Skill'])
                    st.write(f"Level: {skill['Level']}")
                    st.write(f"{skill['Description']}")
                    st.write(' ')
                    st.markdown("---")
