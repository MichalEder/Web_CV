import streamlit as st
import json

def add_entry(dictionary, filename):
    """
    Adds a dictionary as a JSON string to a line in a text file.

    Args:
        dictionary (dict): The dictionary to add.
        filename (str, optional): The name of the text file. Defaults to "data.txt".
    """

    try:
        # Convert the dictionary to a JSON string
        json_string = json.dumps(dictionary)

        # Open the file in append mode
        with open(filename, "a") as f:
            f.write(json_string + "\n")  # Add a newline for separation

        st.success("Dictionary added to file successfully!")

    except Exception as e:
        st.error(f"An error occurred: {e}")

def read_resource(filename):
    resources = []
    try:
        with open(filename, "r") as f:
            for line in f:
                resources.append(json.loads(line))
    except FileNotFoundError:
        pass  # Ignore if the file doesn't exist yet
    return resources