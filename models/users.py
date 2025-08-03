# users.py

from db.db_config import get_connection
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, email, password):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO users (username, email, password)
            VALUES (%s, %s, %s)
        """
        hashed_pw = hash_password(password)
        cursor.execute(query, (username, email, hashed_pw))
        conn.commit()
        print(" User registered successfully")
    except Exception as e:
        print(" Error during registration:", e)
    finally:
        cursor.close()
        conn.close()

def authenticate_user(username, password):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        hashed_pw = hash_password(password)
        query = """
            SELECT * FROM users
            WHERE username = %s AND password = %s
        """
        cursor.execute(query, (username, hashed_pw))
        result = cursor.fetchone()
        return result
    except Exception as e:
        print(" Authentication error:", e)
        return None
    finally:
        cursor.close()
        conn.close()

def get_user_by_id(user_id):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT username, email FROM users WHERE id = %s", (user_id,))
        return cursor.fetchone()
    except Exception as e:
        print("Error retrieving user:", e)
        return None
    finally:
        cursor.close()
        conn.close()