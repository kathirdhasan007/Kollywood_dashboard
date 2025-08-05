# cli/main.py

from services.insert_service import InsertService
from services.query_service import QueryService
from services.update_service import UpdateService
from services.delete_service import DeleteService
from services.validation_utils import ValidationUtils
import hashlib

insert = InsertService()
query = QueryService()
update = UpdateService()
delete = DeleteService()


def display_menu():
    print("\n Kollywood Reviews CLI ")
    print("1. Users")
    print("2. Movie")
    print("3. Review")
    print("4. Genre")
    print("5. Exit")

def display_users():
    print("1. Add Users")
    print("2. View All Users")
    print("3. Update Username")
    print("4. Delete Users")
    print("5. Exit")

def display_Movie():
    print("1. Add Movie")
    print("2. View All Movies")
    print("3. Update Movie Title")
    print("4. Delete Movie")
    print("5. Exit")

def display_Review():
    print("1. Add Review")
    print("2. View All Review")
    print("3. Update Review")
    print("4. Delete Review")
    print("5. Exit")

def display_genre():
    print("1. Add Genre")
    print("2. View All Genre")
    print("3. Update Genre")
    print("4. Delete Genre")
    print("5. Exit")

def display_actors():
    print("1. Add Actor")
    print("2. View All Actor")
    print("3. Update Actor")
    print("4. Delete Actor")
    print("5. Exit")

def display_Movie_cast():
    print("1. Add Movie Cast")
    print("2. View All Movie Cast")
    print("3. Update Movie Cast")
    print("4. Delete Movie Cast")
    print("5. Exit")

def user():
    while True:
        display_users()
        choice_users = input("\n Enter your choice: ").strip()

        if choice_users == '1':
            username = input("Enter user name : ")
            email = input("Enter your email : ")
            passwor = input("Enter Your Secure password : ")
            password  = hashlib.sha256(passwor.encode()).hexdigest()
            if ValidationUtils.validate_email(email):
                insert.insert_user(username,email,password)
                print("Users added !")
            else:
                print(" Enter Valid email : ")
        
        elif choice_users == '2':
            keyword = input("Enter the username : ")
            users = query.search_users_by_name(keyword)
            print("\n Users List:")
            for user in users:
                print(f"- {user[0]}: {user[1]}: {user[2]}: {user[3]}")

        elif choice_users == '3':
            username = input("Enter User name you want to update: ")
            new_user = input("Enter you new username : ")
            update.update_user(username, new_user)
            print("User updated !")

        elif choice_users == '4':
            user_id = int(input("Enter user ID you want to delete : "))
            delete.delete_user(user_id)

        elif choice_users == '5':
            print(" Goodbye!")
            insert.close()
            query.close()
            update.close()
            delete.close()
            break

        else:
           print(" Invalid option. Please choose between 1–5.")  


def movie():
    while True:
        display_Movie()
        choice = input("\n Enter your choice: ").strip()

        if choice == '1':
            title = input(" Enter movie title : ")
            release_year = input(" Enter release_year : ")
            genre_id = input("Enter the movie genre_id : ")
            if ValidationUtils.validate_title(title):
                insert.insert_movie(title,release_year, genre_id)
                print(" Movie added!")
            else:
                print(" Invalid title. Try again.")

        elif choice == '2':
            movies = query.get_all_movies()
            print("\n Movie List:")
            for movie in movies:
                print(f"- {movie[0]}: {movie[1]}: {movie[2]}: {movie[3]}")
        
        elif choice == '3':
            movie_id = int(input(" Movie ID to update: "))
            new_title = input(" New title: ")
            if ValidationUtils.validate_title(new_title):
                update.update_movie_title(movie_id, new_title)
                print(" Movie updated!")
            else:
                print(" Invalid title.")

        elif choice == '4':
            movie_id = int(input(" Movie ID to delete: "))
            if ValidationUtils.validate_id(movie_id):
                delete.delete_movie(movie_id)
                print(" Movie deleted!")
            else:
                print(" Invalid ID.")

        elif choice == '5':
            print(" Goodbye!")
            insert.close()
            query.close()
            update.close()
            delete.close()
            break

        else:
            print(" Invalid option. Please choose between 1–5.")

def Reviews():
    
    while True:
        display_Review()
        choice = input("Enter the Choice : ")
        if choice == '1':
            movie_id = input("Enter Movie id you want review : ")
            user_id = input("Enter the user id : ")
            review_text = input("Enter the Comments about the Mvoie : ")
            rating = input("Enter Rating of this movie (1-5) : ")
            if ValidationUtils.validate_rating(rating) and ValidationUtils.validate_review_text(review_text):
                insert.insert_review(movie_id,user_id,review_text,rating)
                print("Review added !")
            else:
                print("invalid rating or comments !!")
        
        elif choice == '2':
            reviews = query.view_all_Reviews()
            print("\n Review list !")
            for review in reviews:
                print(f" {review[0]}: {review[1]}: {review[2]} {review[3]}:\t {review[4]}: {review[5]}")

        elif choice == '3':
            review_id = input("Enter the review id you want to update :")
            new_rating = input("Enter Rating of movie (1-5) : ")
            new_text = input("Enter the Comments about the Mvoie : ")
            if ValidationUtils.validate_rating(new_rating) and ValidationUtils.validate_review_text(new_text):
                update.update_review(review_id,new_rating,new_text)
            else:
                print("Enter valid comments and rating !!")
        
        elif choice == '4':
            delete_id = input("Enter the review id you want to Delete : ")
            delete.delete_review(delete_id)
            print("Review deleted : ")

        elif choice == '5':
            print(" Goodbye!")
            insert.close()
            query.close()
            update.close()
            delete.close()
            break

        else:
            print(" Invalid option. Please choose between 1–5.")

def genre():

    while True:
        display_genre()
        choice_genre = input("Enter the Choice : ")
        if choice_genre == '1':
            genre_name =  input("Enter the genre name : ")
            if ValidationUtils.validate_genre_name(genre_name):
                insert.insert_genre(genre_name)
                print("Genre inserted !!")
            else:
                print("Enter the valid name : ")

        elif choice_genre == '2':
            genres = query.view_all_genres()
            for genre in genres:
                print(f"- {genre[0]}:   {genre[1]}")

        elif choice_genre == '3':
            genre_id = input("Enter the genre id : ")
            genre_name = input("Enter the genre name : ")
            if ValidationUtils.validate_genre_name(genre_name):
                update.update_genre(genre_id, genre_name)
                print("Genre updated !!")
            else:
                print("Enter the valid genre name !!")

        elif choice_genre == '4':
            genre_id = input("Enter the genre id you want to delete : ")
            delete.delete_genre(genre_id)
            print("genre deleted !!")

        elif choice_genre == '5':
            
            print(" Goodbye!")
            insert.close()
            query.close()
            update.close()
            delete.close()
            break

        else:
            print(" Invalid option. Please choose between 1–5.")

def main():


    while True:
        display_menu()
        choice = input("\n Enter your choice: ").strip()

        if choice == '1':
            user()

        elif choice == '2':
            movie()

        elif choice == '3':
            Reviews()

        elif choice == '4':
            genre()

        elif choice == '5':  
            print(" Goodbye!")
            insert.close()
            query.close()
            update.close()
            delete.close()
            break
        else:
            print(" Invalid option. Please choose between 1–5.")

if __name__ == "__main__":
    main()