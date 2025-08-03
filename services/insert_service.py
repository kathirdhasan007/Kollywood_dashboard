# services/insert_service.py

from db.db_config import get_connection
from services.validation_utils import ValidationUtils
from utils.app_logger import logger

logger.info("Movie inserted successfully")
logger.error("Failed to insert actor: name missing")

class InsertService:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def insert_movie(self, title,release_year, genre_id):
        if ValidationUtils.validate_title(title):
            query = "INSERT INTO movies (title,release_year,genre_id) VALUES (%s,%s,%s);"
            self.cursor.execute(query, (title,release_year,genre_id))
            self.conn.commit()

    def insert_actor(self, name):
        if ValidationUtils.validate_actor_name(name):
            query = "INSERT INTO actors (name) VALUES (%s);"
            self.cursor.execute(query, (name,))
            self.conn.commit()

    def insert_genre(self, genre_name):
        if ValidationUtils.validate_genre_name(genre_name):
            query = "INSERT INTO genres (name) VALUES (%s);"
            self.cursor.execute(query, (genre_name,))
            self.conn.commit()

    def insert_user(self, username, email):
        if ValidationUtils.validate_title(username) and ValidationUtils.validate_email(email):
            query = "INSERT INTO users (username, email) VALUES (%s, %s);"
            self.cursor.execute(query, (username, email))
            self.conn.commit()

    def insert_review(self, movie_id, user_id, review_text, rating):
        if ValidationUtils.validate_review_text(review_text) and ValidationUtils.validate_rating(rating):
            query = """
                INSERT INTO reviews (movie_id, user_id, review_text, rating)
                VALUES (%s, %s, %s, %s);
            """
            self.cursor.execute(query, (movie_id, user_id, review_text, rating))
            self.conn.commit()

    def insert_movie_cast(self, movie_id, actor_id):
        query = "INSERT INTO movie_cast (movie_id, actor_id, role) VALUES (%s, %s, %s);"
        self.cursor.execute(query, (movie_id, actor_id))
        self.conn.commit()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()