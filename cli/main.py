# cli/main.py

from services.insert_service import InsertService
from services.query_service import QueryService
from services.update_service import UpdateService
from services.delete_service import DeleteService
from services.validation_utils import ValidationUtils


def display_menu():
    print("\n Kollywood Reviews CLI ")
    print("1. Add Movie")
    print("2. View All Movies")
    print("3. Update Movie Title")
    print("4. Delete Movie")
    print("5. Exit")

def main():
    insert = InsertService()
    query = QueryService()
    update = UpdateService()
    delete = DeleteService()

    while True:
        display_menu()
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

if __name__ == "__main__":
    main()