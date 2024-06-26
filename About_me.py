import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
components.html(open('custom_head.html', 'r').read(), height=10, width=10)
st.title("Hi there! Welcome to my corner of the web.")
st.markdown("<br>", unsafe_allow_html=True)
col1, col2 = st.columns([1,1])

st.write('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css"/>',
        unsafe_allow_html=True)

with col1:
    st.write("I'm Michal Eder. Welcome to my online portfolio. Here you'll find information about my skills and experience, along with some projects I'm passionate about. Use the sidebar to navigate. Feel free to get in touch!")

    st.subheader("About me")
    st.write(
        "After 6 years in the automotive industry, I found myself captivated by IT. Drawn to its power for optimization and automation, I decided to fully immerse myself in this field and completed a retraining course.  I'm fascinated by the world of programming and the endless possibilities it offers. The satisfaction of transforming effort into tangible solutions fuels my drive to continue growing in the IT world.")
    st.markdown("<br>", unsafe_allow_html=True)
    st.write(
        "Currently, I'm actively exploring career paths at the intersection of web development and quality assurance. While web development broadly interests me, I'm strongly drawn to the meticulous nature of QA, aligning well with my background in the automotive industry. My goal is to leverage my technical skills, passion for creating well-structured solutions, and problem-solving mindset to contribute to dynamic web projects.")
    st.markdown("<br>", unsafe_allow_html=True)

    st.write("Let's explore some of my projects and skills in the corresponding sections in the sidebar")
    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("Languages")
    st.write("English - B2 - Used on daily basis")
    st.write("Deutsch - A2-B1 - Slightly rusty, haven't spoken in a while, used only for reading tech. documentation")
    st.write("Czech - C2 - Native speaker")


with col2:
    st.image('resources/images/profile.jpg', width=300)
    c = st.container()
    st.markdown("<br>", unsafe_allow_html=True)
    with c:
        st.markdown('<i class="fas fa-phone"></i> +420 602 680 577<br>', unsafe_allow_html=True)
        st.markdown('<i class="fas fa-envelope"></i> edermichal.eder@gmail.com<br>', unsafe_allow_html=True)
        st.markdown("""
                   [<i class="fab fa-github"></i> GitHub](https://github.com/MichalEder)<br> 
                   [<i class="fab fa-linkedin"></i> LinkedIn](https://www.linkedin.com/in/michal-eder-447049272/)
               """, unsafe_allow_html=True)