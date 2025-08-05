from db.db_config import get_connection

class UpdateService:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def update_movie_title(self, movie_id, new_title):
        query = "UPDATE movies SET title = %s WHERE id = %s;"
        self.cursor.execute(query, (new_title, movie_id))
        self.conn.commit()

    def update_actor_name(self, actor_id, new_name):
        query = "UPDATE actors SET name = %s WHERE id = %s;"
        self.cursor.execute(query, (new_name, actor_id))
        self.conn.commit()

    def update_review(self, review_id, new_text,new_rating):
        self.cursor.execute("UPDATE reviews SET rating = %s, review_text = %s WHERE id = %s;", (new_rating, new_text, review_id))
        self.conn.commit()

    def update_genre(self, genre_id, new_name):
        query = "UPDATE genres SET name = %s WHERE id = %s;"
        self.cursor.execute(query, (new_name, genre_id))
        self.conn.commit()

    def update_user(self, Username, new_name):
        query = "UPDATE users SET name = %s WHERE username = %s;"
        self.cursor.execute(query, (new_name, Username))
        self.conn.commit()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()