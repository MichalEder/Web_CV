import yaml
import streamlit as st
import streamlit_authenticator as stauth
from yaml.loader import SafeLoader

from functions.admin_section import add_entry_form
from functions.general import save_uploaded_image

st.set_page_config(layout="wide")

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized'])

authenticator.login()

if st.session_state["authentication_status"]:
    authenticator.logout(location='sidebar')


    uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    if uploaded_image is not None:
        image_path = save_uploaded_image(uploaded_image)
        st.success('Image uploaded and saved successfully!')
    with st.expander('Add project'):
        add_entry_form('Project:', ['Project', 'Tech', 'Description', 'Link', 'Image'], 'projects')
    with st.expander('Add formal education'):
        add_entry_form('Formal Education:', ['School', 'Years', 'Faculty', 'Field', 'Note'], 'education')
    with st.expander('Add course'):
        add_entry_form("Courses:", ['course', 'provider', 'course_type', 'description', 'date_of_compl', 'link_to_course', 'image'], 'courses')
    with st.expander('Add work experience'):
        add_entry_form('Work experience', ['Company','Position_Role','Start_Date','End_date','Skills', 'Tools', 'Description','Image'], 'work_experience' )
    with st.expander('Add skills'):
        add_entry_form('Skills', ['Skill', 'Level', 'Description', 'Image'], 'skills')
    with st.expander('Add hobby'):
        add_entry_form('Hobby', ['Hobby', 'Description', 'Image'], 'hobby')


elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')

elif st.session_state["authentication_status"] is None:
    st.warning('I am pretty sure you are not an admin, so this section is not meant for you. Try different one.')
