from db.db_config import get_connection

def insert_genres(id,genre_name):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        qry = """INSERT INTO Genres (id, genre_name) VALUES (%s, %s)"""
        cursor.execute(qry,(id, genre_name))
        conn.commit()
        print("values Insert in Genres ")
    except Exception as e:
        print("Error durig insert values :  ",e)
    finally:
        cursor.close()
        conn.close()

def get_all_genre():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        qry = "SELECT * FROM Genres"
        cursor.execute(qry)
        result = cursor.fetchone
        return result
    except Exception as e:
        print("Execution Error :  ",e)
    finally:
        cursor.close()
        conn.close()

