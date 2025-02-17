# ========================================
# Reynaldo Pena
# CIS261
# Lab: Movie Guide Part 2
# ========================================

filename = input("Enter filename: ").strip()

def load_movies():
    """read movies from the file into list"""
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_movies():
    """write movies from list into file"""
    with open(filename, "w") as file:
        for movie in movies:
            file.write(movie + "\n")

movies = load_movies()

def show_menu():
    """Display the menu options for the user."""
    print("\nMovieGuide")# - Movie Guide header
    print("=" * 12)# - Separator line using "=" * 12
    print("COMMAND MENU")# - COMMAND MENU
    print("lists - list all movies") # Four command options (lists, add, del, exit)
    print("add - Add a movie") 
    print("del - Delete a movie")
    print("exit - Exit program")

def list_movies(movies):
    """Display all movies in the list with numbers."""
    print("\nMovies:")# - Print "Movies:" header
    if not movies:
        print("No movies in the list.")
    else:
        for i, movie in enumerate(movies, start = 1):
            print(f"{i}. {movie}")

def add_movie(filename, movies):
    """Get movie name from user and add it to the list."""
    title = input("\nName:").strip() 
    if title:
        movies.append(title) 
        save_movies()
        print(f"\n{title} has been added to the list.") 
    else:
        print("\nMovie title cannot be blank.")
    list_movies() 

def delete_movie():
    """Delete a movie from the list by number."""
    list_movies() 
    
    if not movies:
        return
    
    try:
        number = int(input("\nNumber: "))
        if 1 <= number <= len(movies): 
            title = movies.pop(number - 1)
            save_movies()
            print(f"\n{title} has been deleted from the list.")  
        else:
            print("\nInvalid response")
    except ValueError:
        print("\nInvalid response")

    list_movies()
    
def main():
    """Main program loop."""

    show_menu() 
    while True: 
        command = input("\nCommand: ").strip().lower()
        if command.lower() == "lists":
            list_movies()
        elif command.lower() == "add": 
            add_movie()
        elif command.lower() == "del":
            delete_movie()
        elif command.lower() == "exit":
            print("\nBye!")
            break
        else:
            print("\nInvalid response") 
            show_menu() 

if __name__ == "__main__":
    main()