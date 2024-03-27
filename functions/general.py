import sqlite3
import streamlit as st

def read_resource(table_name, db_file='resources/db.db'):
    """Reads all entries from an SQLite table and returns them as a list of dictionaries.

    Args:
        table_name (str): Name of the table.
        db_file (str, optional): Path to the database file. Defaults to 'resources/db.db'.

    Returns:
        List of dictionaries: Each dictionary represents a row with column names as keys.
    """
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        resources = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]

        resources_dict = [dict(zip(column_names, row)) for row in resources]
        return resources_dict


def add_entry(entry_data, table_name, db_file='resources/db.db'):
    """Adds a new entry to the specified SQLite table, using parameterization for security.

    Args:
        entry_data (dict): The data to be added as a dictionary.
        table_name (str): Name of the table.
        db_file (str, optional): Path to the database file. Defaults to 'resources/db.db'.
    """
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        try:
            columns = ', '.join(entry_data.keys())
            placeholders = ', '.join('?' * len(entry_data))  # Create '?' for each value
            sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            cursor.execute(sql, tuple(entry_data.values()))
            conn.commit()
            st.success("Data added successfully!")
        except sqlite3.Error as e:
            st.error(f"An error occurred: {e}")
