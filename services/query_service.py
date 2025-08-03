from db.db_config import get_connection

class QueryService:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def get_all_movies(self):
        query = "SELECT id, title, release_year, genre_id FROM movies;"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_reviews_by_movie(self, movie_id):
        query = """
            SELECT r.review_text, r.rating, u.username
            FROM reviews r
            JOIN users u ON r.user_id = u.id
            WHERE r.movie_id = %s;
        """
        self.cursor.execute(query, (movie_id,))
        return self.cursor.fetchall()

    def search_movies_by_title(self, keyword):
        query = "SELECT id, title FROM movies WHERE title LIKE %s;"
        self.cursor.execute(query, (keyword,))
        return self.cursor.fetchall()

    def get_cast_by_movie(self, movie_id):
        query = """
            SELECT a.name, mc.actor
            FROM movie_cast mc
            JOIN actors a ON mc.actor_id = a.actor_id
            WHERE mc.movie_id = %s;
        """
        self.cursor.execute(query, (movie_id,))
        return self.cursor.fetchall()

    def get_top_rated_movies(self, limit=5):
        query = """
            SELECT m.title, AVG(r.rating) as avg_rating
            FROM reviews r
            JOIN movies m ON r.movie_id = m.id
            GROUP BY r.movie_id
            ORDER BY avg_rating DESC
            LIMIT %s;
        """
        self.cursor.execute(query, (limit,))
        return self.cursor.fetchall()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

