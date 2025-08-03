# services/delete_service.py

from db.db_config import get_connection

class DeleteService:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def delete_movie(self, movie_id):
        query = "DELETE FROM movies WHERE id = %s;"
        self.cursor.execute(query, (movie_id,))
        self.conn.commit()

    def delete_actor(self, actor_id):
        query = "DELETE FROM actors WHERE id = %s;"
        self.cursor.execute(query, (actor_id,))
        self.conn.commit()

    def delete_review(self, review_id):
        query = "DELETE FROM reviews WHERE id = %s;"
        self.cursor.execute(query, (review_id,))
        self.conn.commit()

    def delete_genre(self, genre_id):
        query = "DELETE FROM genres WHERE id = ?;"
        self.cursor.execute(query, (genre_id,))
        self.conn.commit()

    def delete_cast_entry(self, movie_id):
        query = "DELETE FROM movie_cast WHERE movie_id = %s;"
        self.cursor.execute(query, (movie_id))
        self.conn.commit()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()