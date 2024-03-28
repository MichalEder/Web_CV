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

def update_database_entry(table, primary_key, primary_key_value, data):
    """Updates an existing entry in an SQLite database.

        Args:
            table (str): The name of the table to update.
            primary_key (str): The name of the primary key column in the table.
            primary_key_value: The value of the primary key to identify the row to update.
            data (dict): A dictionary containing the new column values to be updated.
    """
    with sqlite3.connect('resources/db.db') as conn:
        cursor = conn.cursor()
    try:
        update_columns = ", ".join([f"{column} = ?" for column in data])
        sql_query = f"UPDATE {table} SET {update_columns} WHERE {primary_key} = ?"
        values = tuple(data.values()) + (primary_key_value,)
        cursor.execute(sql_query, values)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error updating database: {e}")

def delete_entry(table_name, primary_key, primary_key_value, db_file='resources/db.db'):
    """Deletes an entry from the specified SQLite table based on primary key.

    Args:
        table_name (str): Name of the table.
        primary_key (str): Name of the primary key column.
        primary_key_value: Value of the primary key to identify the row to delete.
        db_file (str, optional): Path to the database file. Defaults to 'resources/db.db'.
    """
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        try:
            sql = f"DELETE FROM {table_name} WHERE {primary_key} = ?"
            cursor.execute(sql, (primary_key_value,))
            conn.commit()
            st.success("Entry deleted successfully!")  # Assuming you have 'st' for Streamlit
        except sqlite3.Error as e:
            st.error(f"An error occurred: {e}")