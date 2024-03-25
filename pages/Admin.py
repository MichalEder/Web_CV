import yaml
import streamlit as st
import streamlit_authenticator as stauth
from yaml.loader import SafeLoader
from functions.general import add_entry

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

    if st.session_state["authentication_status"]:
        st.title("Add project:")

        with st.form("projects_form"):

            Project = st.text_input("Project:")
            Tech = st.text_input("Technologies:")
            Description = st.text_area("Description:")
            Link = st.text_input("Link:")
            Image = st.text_input("Image")

            submitted = st.form_submit_button("Add project")

            if submitted:
                projects_dict = {
                    'Project':Project,
                    'Tech': Tech,
                    'Description': Description,
                    'Link' : Link,
                    'Image' : Image
                }
                add_entry(projects_dict, 'projects')

        st.title("Add formal education:")

        with st.form("formal_edu_form"):

            school = st.text_input("School:")
            years = st.text_input("Years:")
            faculty = st.text_input("Faculty:")
            field = st.text_input("Field of study:")
            note = st.text_input("Note:")


            submitted = st.form_submit_button("Add formal education")

            if submitted:
                formal_edu_dict = {
                    'School': school,
                    'Years': years,
                    'Faculty': faculty,
                    'Field': field,
                    'Note': note
                }
                add_entry(formal_edu_dict, 'education')

        st.title("Add courses:")

        with st.form("courses"):
            course = st.text_input("Course name: ")
            Provider = st.text_input("Course provider: ")
            Course_type = st.text_input("Type of course:")
            Description = st.text_area("Description:")
            link_to_course = st.text_input("Link to course:")
            Date_of_compl = st.text_input("Date of completion")
            Image = st.text_input("Image")


            submitted = st.form_submit_button("Add course")

            if submitted:
                course_dict = {
                    'course' : course,
                    'provider': Provider,
                    'link_to_course' : link_to_course,
                    'description' : Description,
                    'course_type': Course_type,
                    'date_of_compl': Date_of_compl,
                    'image': Image
                }
                add_entry(course_dict, 'courses')

        st.title("Add work experience")

        with st.form("work_form"):
            # Create form elements for dictionary entries
            company = st.text_input("Company:")
            role = st.text_input("Position:")
            start_date = st.text_input("Start date:")
            end_date = st.text_input("End date:")
            skills = st.text_input("Skills:")
            tools = st.text_input("Tools")
            description = st.text_area("Description:")
            image = st.text_input("Image:")


            submitted = st.form_submit_button("Add work experience")

            if submitted:
                work_exp_dict = {
                    'Company': company,
                    'Position_Role': role,
                    'Start_Date': start_date,
                    'End_date': end_date,
                    'Skills': skills,
                    'Tools': tools,
                    'Description': description,
                    'Image': image
                }
                add_entry(work_exp_dict, 'work_experience')

        st.title("Add hobby")

        with st.form("hobby_form"):
            hobby = st.text_input("Hobby")
            description = st.text_area("Description:")
            image = st.text_input("Image:")


            submitted = st.form_submit_button("Add hobby")

            if submitted:
                hobby_dict = {
                    'Hobby': hobby,
                    'Description': description,
                    'Image': image
                }
                add_entry(hobby_dict, 'hobby')
        st.title("Add skill:")

        with st.form("skills"):

            skill = st.text_input("Skill")
            level = st.text_input("Level")
            description = st.text_input("Description:")
            image = st.text_input("Image")


            submitted = st.form_submit_button("Add skill")

            if submitted:
                course_dict = {
                    'Skill': skill,
                    'Level': level,
                    'Description': description,
                    'Image': image
                }
                add_entry(course_dict, 'skills')

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')

elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')