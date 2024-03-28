import streamlit as st

from functions.db_interaction import add_entry


def add_entry_form(section_title, form_fields, db_table):
    st.title(f"Add {section_title}")

    with st.form(f"{section_title}_form"):
        form_data = {}
        for field_label in form_fields:
            form_data[field_label] = st.text_input(field_label)

        submitted = st.form_submit_button(f"Add {section_title}")

        if submitted:
            add_entry(form_data, db_table)