# services/validation_service.py

import re

class ValidationUtils:

    @staticmethod
    def validate_title(title):
        return bool(title and title.strip())

    @staticmethod
    def validate_actor_name(name):
        return bool(name and name.strip())

    @staticmethod
    def validate_review_text(text):
        return bool(text and text.strip())

    @staticmethod
    def validate_rating(rating):
        return isinstance(rating, int) and 1 <= rating <= 5

    @staticmethod
    def validate_genre_name(genre):
        return bool(genre and genre.strip())

    @staticmethod
    def validate_id(value):
        return isinstance(value, int) and value > 0

    @staticmethod
    def validate_role(role):
        return bool(role and role.strip())

    @staticmethod
    def validate_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None