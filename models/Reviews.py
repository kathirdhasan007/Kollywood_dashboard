from db.db_config import get_connection

def add_review(id, movie_id, user_id, rating, comment):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        qry = """INSERT INTO Reviews (id, movie_id, user_id, rating, review_text) VALUES(%s, %s, %s, %s, %s)"""
        cursor.execute(qry, (id, movie_id, user_id, rating, comment))
        return cursor.fetchone()
    except Exception as e:
        print("Error during insert values : ",e)
    finally:
        cursor.close()
        conn.close()

def view_rating(title):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        qry = """SELECT m.title, r.rating, r.review_text FROM Movies m JOIN Reviews r on  m.id = r.movie_id WHERE LIKE '%s';"""
        cursor.execute(qry,(title,))
        return cursor.fetchone()
    except Exception as e:
        print("Error during insert : ",e)
    finally:
        cursor.close()
        conn.close()
