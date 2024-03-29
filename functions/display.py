import streamlit as st
from functions.db_interaction import update_database_entry, delete_entry


def display_edit_skill(skill):
    """Displays an editable form for a given skill. Allows for modification or deletion of the skill entry.

    Allows the user to modify the skill

    Args:
        skill (dict): A dictionary containing the skill's information, including
        'Skill', 'Level', 'Image', 'Description'
    """
    with st.form(f"{skill['Skill']} Edit"):
        skill_edited = st.text_input("Skill", value=skill['Skill'])
        level_edited = st.text_input("Level", value=skill['Level'])
        description_edited = st.text_area("Description:", value=skill['Description'])
        image_edited = st.text_input("Image", value=skill['Image'])

        submitted = st.form_submit_button("Edit skill")
        submitted_delete = st.form_submit_button("Delete skill")

        if submitted_delete:
            delete_entry('skills', 'ID', skill['ID'])

        if submitted:
            skill_edit_dict = {
                'Skill': skill_edited,
                'Level': level_edited,
                'Description': description_edited,
                'Image': image_edited
            }
            update_database_entry('skills', 'ID', skill['ID'], skill_edit_dict)


def display_skill(skill):
    """Displays information about a given skill.

    Args:
        skill (dict): A dictionary containing the skill's information, including
        'Skill', 'Level', 'Image', 'Description'
    """
    if st.session_state["authentication_status"]:
        display_edit_skill(skill)
    else:
        st.image(f"resources/images/{skill['Image']}", width=100)
        st.subheader(skill['Skill'])
        st.write(f"Level: {skill['Level']}")
        st.write(f"{skill['Description']}")
        st.write(' ')
    st.markdown("---")


def display_edit_project(project):
    """Displays an editable form for a project.

    Allows the user to modify the project title, technologies, description, link, and image,
    or delete the project from the database.

    Args:
        project (dict): A dictionary containing the project's information, including
            'Project', 'Tech', 'Description', 'Link', and 'Image'.
    """
    with st.form(f"{project['Project']} Edit"):
        project_edited = st.text_input("Project", value=project['Project'])
        tech_edited = st.text_input("Technologies", value=project['Tech'])
        description_edited = st.text_area("Description:", value=project['Description'])
        link_edited = st.text_input("Link", value=project['Link'])
        image_edited = st.text_input("Image", value=project['Image'])

        submitted_edit = st.form_submit_button("Edit project")
        submitted_delete = st.form_submit_button("Delete Project")

        if submitted_delete:
            delete_entry('projects', 'ID', project['ID'])

        if submitted_edit:
            project_edit_dict = {
                'Project': project_edited,
                'Tech': tech_edited,
                'Link': link_edited,
                'Description': description_edited,
                'Image': image_edited
            }
            update_database_entry('projects', 'ID', project['ID'], project_edit_dict)


def display_project(project):
    """Displays information about a project in a visually organized format.

    Args:
        project (dict): A dictionary containing the project's information, including
            'Project', 'Tech', 'Description', 'Link', and 'Image'.
    """
    with (st.container()):
        if st.session_state["authentication_status"]:
            display_edit_project(project)

        else:
            col1, col2 = st.columns([1, 6])
            with col1:
                st.image(f"resources/images/{project['Image']}", width=150)

            with col2:
                st.subheader(project['Project'])
                st.write(f"Technologies: {project['Tech']}")
                st.write(project['Description'])
                if 'Link' in project and project['Link'].startswith('http'):
                    st.markdown(f"[Link]({project['Link']})")
                else:
                    st.write(f"{project['Link']}")
    st.markdown("---")


def display_edit_work(experience):
    """Displays an editable form for a work experience entry.

    Allows modification or deletion of information about a past or current work experience

    Args:
        experience (dict): A dictionary containing the work experience information, including
            'Company', 'Role', 'Description', 'Duration', 'Skills', 'Tools',  and 'Image'
    """
    with st.form(f"{experience['Position_Role']} Edit"):
        company_edited = st.text_input("Company", value=experience['Company'])
        position_role_edited = st.text_input("Position/ Role", value=experience['Position_Role'])
        start_date_edited = st.text_input("Start date", value=experience['Start_Date'])
        end_date_edited = st.text_input("End date:", value=experience['End_date'])
        skills_edited = st.text_input("Skills", value=experience['Skills'])
        tools_edited = st.text_input("Tools", value=experience['Tools'])
        description_edited = st.text_area("Description", value=experience['Description'])
        image_edited = st.text_input("Image", value=experience['Image'])

        submitted_edit = st.form_submit_button("Edit experience")
        submitted_delete = st.form_submit_button("Delete experience")

        if submitted_delete:
            delete_entry('work_experience', 'ID', experience['ID'])

        if submitted_edit:
            experience_edit_dict = {
                'Company': company_edited,
                'Position_Role': position_role_edited,
                'Start_date': start_date_edited,
                'End_date': end_date_edited,
                'Skills': skills_edited,
                'Tools': tools_edited,
                'Description': description_edited,
                'Image': image_edited
            }
            update_database_entry('work_experience', 'ID', experience['ID'], experience_edit_dict)


def display_work(experience):
    """Displays information about a work experience in a visually organized format.

    Args:
        experience (dict): A dictionary containing the work experience's information, including
            'Company', 'Role', 'Description', 'Duration', 'Skills', 'Tools',  and 'Image'
    """
    with st.container():
        if st.session_state["authentication_status"]:
            display_edit_work(experience)
        else:
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(f"resources/images/{experience['Image']}", width=None)

            with col2:
                st.subheader(experience['Company'])
                st.write(f"Role: {experience['Position_Role']}")
                st.write(f"Duration: {experience['Start_Date']} - {experience['End_date']}")

                st.markdown("<br>", unsafe_allow_html=True)

                st.write(f"Skills: {experience['Skills']}")
                st.write(f"Tools: {experience['Tools']}")
                st.write(f"{experience['Description']}")

            st.markdown("---")
            st.markdown("<br>", unsafe_allow_html=True)


def display_edit_course(course):
    """Displays an editable form for a completed course or certification.

    Allows modification or deletion of details related to the course,

    Args:
        course (dict): A dictionary containing the course information, including
            'course', 'provider', 'description', 'date_of_compl', 'link_to_course', 'course_type',  and 'image'
    """
    with st.form(f"{course['course']} Edit"):
        course_edited = st.text_input("Course", value=course['course'])
        provider_edited = st.text_input("Provider", value=course['provider'])
        date_of_compl_edited = st.text_input("Completed:", value=course['date_of_compl'])
        course_type_edited = st.text_input("Course type:", value=course['course_type'])
        link_to_course_edited = st.text_input("Link", value=course['link_to_course'])
        description_edited = st.text_area("Description", value=course['description'])
        image_edited = st.text_input("Image", value=course['image'])

        submitted_edit = st.form_submit_button("Edit course")
        submitted_delete = st.form_submit_button("Delete course")

        if submitted_delete:
            delete_entry('courses', 'ID', course['ID'])

        if submitted_edit:
            course_edit_dict = {
                'course': course_edited,
                'provider': provider_edited,
                'date_of_compl': date_of_compl_edited,
                'course_type': course_type_edited,
                'link_to_course': link_to_course_edited,
                'description': description_edited,
                'image': image_edited
            }
            update_database_entry('courses', 'ID', course['ID'], course_edit_dict)


def display_course(course):
    """Displays information about a courses in a visually organized format.

    Args:
        course (dict): A dictionary containing the work experience's information, including
            'course', 'provider', 'description', 'date_of_compl', 'link_to_course', 'course_type',  and 'image'
    """
    with st.container():
        if st.session_state["authentication_status"]:
            display_edit_course(course)
        else:
            col1, col2 = st.columns([1, 3])

            with col1:
                st.image(f"resources/images/{course['image']}", width=None)

            with col2:
                st.subheader(course['course'])
                st.write(course['provider'])
                st.write(f"Completed: {course['date_of_compl']}")
                st.write(f"Course type: {course['course_type']}")
                st.markdown(f"[Link to Course]({course['link_to_course']})")
                st.write(course['description'])

        st.markdown("---")
        st.markdown("<br>", unsafe_allow_html=True)


def display_edit_education(school):
    """Displays an editable form for formal education.

    Allows modification or deletion of details related to the edutacion

    Args:
        school (dict): A dictionary containing the course information, including
            'School', 'Faculty', 'Field', 'Years', 'Status' and 'Note'
    """
    with st.form(f"{school['Years']} Edit"):
        school_edited = st.text_input("School", value=school['School'])
        faculty_edited = st.text_input("Faculty", value=school['Faculty'])
        field_edited = st.text_input("Field of study", value=school['Field'])
        years_edited = st.text_input("Years of studies:", value=school['Years'])
        status_edited = st.text_input("Status:", value=school['Status'])
        note_edited = st.text_area("Note", value=school['Note'])

        submitted_edit = st.form_submit_button("Edit education")
        submitted_delete = st.form_submit_button("Delete education")

        if submitted_delete:
            delete_entry('education', 'ID', school['ID'])

        if submitted_edit:
            school_edit_dict = {
                'School': school_edited,
                'Faculty': faculty_edited,
                'Field': field_edited,
                'Years': years_edited,
                'Status': status_edited,
                'Note': note_edited,
            }
            update_database_entry('education', 'ID', school['ID'], school_edit_dict)


def display_education(school):
    """Displays information about education in a visually organized format.

    Args:
        school (dict): A dictionary containing the information about education, including
            'School', 'Faculty', 'Field', 'Years', 'Status' and 'Note'
    """
    if st.session_state["authentication_status"]:
        display_edit_education(school)
    else:
        st.subheader(school['School'])
        st.write(school['Faculty'])
        st.write(f"Field of study: {school['Field']}")
        st.write(f"Duration of study: {school['Years']}")
        st.write(f"Status: {school['Status']}")
        st.write(school['Note'])
    st.markdown("---")


def display_edit_hobby(hobby):
    """Displays an editable form for hobby.

    Allows modification or deletion of details related to the hobby

    Args:
        hobby (dict): A dictionary containing the course information. including
            'Hobby', 'Description', 'Image'
    """
    with st.form(f"{hobby['Hobby']} Edit"):
        hobby_edited = st.text_input("Hobby", value=hobby['Hobby'])
        description_edited = st.text_area("Description", value=hobby['Description'])
        image_edited = st.text_input("Image:", value=hobby['Image'])

        submitted_edit = st.form_submit_button("Edit hobby")
        submitted_delete = st.form_submit_button("Delete hobby")

        if submitted_delete:
            delete_entry('hobby', 'ID', hobby['ID'])

        if submitted_edit:
            hobby_edit_dict = {
                'Hobby': hobby_edited,
                'Description': description_edited,
                'Image': image_edited,
            }
            update_database_entry('hobby', 'ID', hobby['ID'], hobby_edit_dict)


def display_hobby(hobby):
    """Displays information about hobbies in a visually organized format.

    Args:
        hobby (dict): A dictionary containing the information about hobby, including
            'Hobby', 'Description', 'Image'
    """
    if st.session_state["authentication_status"]:
        display_edit_hobby(hobby)
    else:
        with st.container():
            st.subheader(f"{hobby['Hobby']}")
            col1, col2 = st.columns([1, 5])

            with col1:
                st.image(f"resources/images/{hobby['Image']}", width=200)

            with col2:
                st.markdown(f"{hobby['Description']}")

    st.markdown("---")
