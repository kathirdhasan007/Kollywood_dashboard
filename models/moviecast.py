from db.db_config import get_connection

def insert_moviecast(movie_id, actor_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        qry = """INSERT INTO Movie_cast (movie_id, actor_id) VALUES (%s, %s)"""
        cursor.execute(qry,(movie_id, actor_id))
        conn.commit()
        print("values Insert in Movie_cast ")
    except Exception as e:
        print("Error during insert values :  ",e)
    finally:
        cursor.close()
        conn.close()