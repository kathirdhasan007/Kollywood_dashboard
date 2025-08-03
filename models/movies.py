from db.db_config import get_connection

def create_movie(movie_id, title, release_year, genre_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        qry = """ INSERT INTO Movies VALUES(%s,%s,%s,%s) """
        cursor.execute(qry,(movie_id, title, release_year, genre_id))
        conn.commit()
        print("values Inserted in Movies Table")
    except Exception as err:
        print("Error: ",err)
    finally:
        cursor.close()
        conn.close()

def deleteData(title):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        qry = """DELETE FROM Movies WHERE title like '%s'"""
        cursor.execute(qry,(title,))
        conn.commit()
    except Exception as err:
        print("Error: ",err)
    finally:
        cursor.close()
        conn.close()

def searchMovie(title):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        qry = """SELECT * FROM movies WHERE like %s"""
        cursor.execute(qry,title)
        return cursor.fetchone()
    except Exception as err:
        print("Error: ",err)
    finally:
        cursor.close()
        conn.close()