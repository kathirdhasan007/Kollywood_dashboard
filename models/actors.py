from db.db_config import get_connection

def insert_actor(id, actor_name):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        qry = """INSERT INTO Actors (id, actor_name) VALUES (%s,%s)"""
        cursor.execute(qry, (id, actor_name))
        conn.commit()
        print("Values inserted in Actors")
    except Exception as e:
        print("Error during inserting  : ",e)
    finally:
        cursor.close()
        conn.close()

def search_movie_by_actor(actor_name):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        qry = """SELECT a.actor_name, m.titleFROM Actors aJOIN Movie_cast mc ON mc.movie_id = a.id JOIN movies m on m.id = mc.movie_idWHERE actor_name LIKE '%s';"""
        cursor.execute(qry,(actor_name,))
        return cursor.fetchone()
    except Exception as e:
        print("Error while searching : ",e)
    finally:
        cursor.close()
        conn.close()
