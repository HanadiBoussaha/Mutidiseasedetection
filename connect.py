import mysql.connector
import bcrypt
import streamlit as st

# 
# MySQL connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="projetgl"
    )

# Sign-up function
def signup_user(name, email, password):
    conn = get_connection()
    cursor = conn.cursor()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, email, hashed_password.decode('utf-8')))
    conn.commit()
    cursor.close()
    conn.close()

     
# Login function
def login_user(name, password):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT password FROM users WHERE name = %s"
    cursor.execute(query, (name,))
    record = cursor.fetchone()
    cursor.close()
    conn.close()
    if record:
        return bcrypt.checkpw(password.encode('utf-8'), record[0].encode('utf-8'))
    return False


# Create patient
def create_patient(name, age,gender, disease):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO patients (name, age,gender, disease) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, age,gender, disease))
    conn.commit()
    cursor.close()
    conn.close()

# Read patients
def get_patients():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM patients"
    cursor.execute(query)
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return records
# Fonction pour mettre à jour un patient dans la base de données
def update_patient(patient_id, updated_data):
    try:
        conn = get_connection()
        if conn is None:
            st.error("Database connection failed!")
            return
        
        cursor = conn.cursor()

        # Générer la requête SQL
        set_clause = ", ".join([f"{key} = %s" for key in updated_data.keys()])
        values = list(updated_data.values())
        values.append(patient_id)

        query = f"""
            UPDATE patients
            SET {set_clause}
            WHERE id = %s
        """

        cursor.execute(query, values)
        conn.commit()
        conn.close()
        
        st.success(f"Patient with ID {patient_id} updated successfully!")
    except mysql.connector.Error as e:
        st.error(f"Error updating patient: {e}")


# Delete patient
def delete_patient(patient_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM patients WHERE id = %s", (patient_id,))
    conn.commit()
    conn.close()
