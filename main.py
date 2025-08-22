#!/usr/bin/env python3
"""
Movie Booking System
A command-line application for cinema management
"""

import time

# Sample movie data
data = [
    {'Movie ID': 301, 'Title': 'The Quantum Paradox', 'Genre': 'Science Fiction', 'Language': 'English', 'Duration': '145 min', 'Ticket Price (PKR)': 1200},
    {'Movie ID': 302, 'Title': 'Edge of Eternity', 'Genre': 'Action', 'Language': 'English', 'Duration': '140 min', 'Ticket Price (PKR)': 1500},
    {'Movie ID': 303, 'Title': 'Nebula Rising', 'Genre': 'Adventure', 'Language': 'English', 'Duration': '135 min', 'Ticket Price (PKR)': 1100},
    {'Movie ID': 304, 'Title': 'Shadow of the Blade', 'Genre': 'Action', 'Language': 'English', 'Duration': '120 min', 'Ticket Price (PKR)': 1400},
    {'Movie ID': 305, 'Title': 'Toofan', 'Genre': 'Action', 'Language': 'Urdu', 'Duration': '130 min', 'Ticket Price (PKR)': 850},
    {'Movie ID': 306, 'Title': 'Lal Haveli', 'Genre': 'Horror', 'Language': 'Urdu', 'Duration': '120 min', 'Ticket Price (PKR)': 700},
]

# Sample schedule data
schedule = [
    {'Movie ID': 301, 'Show ID': 'S101', 'Date': '2024-12-01', 'Time': '06:00 PM', 'Screen Number': 1},
    {'Movie ID': 302, 'Show ID': 'S102', 'Date': '2024-12-01', 'Time': '09:00 PM', 'Screen Number': 2},
    {'Movie ID': 303, 'Show ID': 'S103', 'Date': '2024-12-01', 'Time': '03:00 PM', 'Screen Number': 3},
    {'Movie ID': 304, 'Show ID': 'S104', 'Date': '2024-12-01', 'Time': '12:00 PM', 'Screen Number': 2},
    {'Movie ID': 301, 'Show ID': 'S105', 'Date': '2024-12-01', 'Time': '07:00 PM', 'Screen Number': 3},
    {'Movie ID': 304, 'Show ID': 'S106', 'Date': '2024-12-01', 'Time': '04:30 PM', 'Screen Number': 4},
    {'Movie ID': 305, 'Show ID': 'S107', 'Date': '2024-12-01', 'Time': '02:00 PM', 'Screen Number': 5},
    {'Movie ID': 305, 'Show ID': 'S108', 'Date': '2024-12-01', 'Time': '08:00 PM', 'Screen Number': 1},
    {'Movie ID': 306, 'Show ID': 'S109', 'Date': '2024-12-01', 'Time': '10:00 PM', 'Screen Number': 3},
]

# Bookings data
bookings = []

def refresh_movie(data):
    """Write movie data to movies.txt file"""
    with open("movies.txt", "w") as file:
        file.truncate(0)  
        headers = f"{'Movie ID':<10} | {'Title':<30} | {'Genre':<17} | {'Language':<12} | {'Duration':<10} | {'Ticket Price (PKR)'}\n"
        file.write(headers)
        
        for movie in data:
            file.write(f"{movie['Movie ID']:<10} | {movie['Title']:<30} | {movie['Genre']:<17} | {movie['Language']:<12} | {movie['Duration']:<10} | {movie['Ticket Price (PKR)']}\n")

def show_movie():
    """Display all movies"""
    refresh_movie(data)
    with open("movies.txt", "r") as file:
         print(file.read())

def add_movie(data):
    """Add a new movie"""
    try:
        if data!=[]:
            movieid=data[-1]['Movie ID'] + 1  
        else:
            movieid=301
        new_movie = {
            'Movie ID':movieid , 
            'Title': input('Enter Title of movie: ').title(),
            'Genre': input('Enter Genre of movie: ').title(),
            'Language': input('Enter Language of movie: ').title(),
            'Duration': input('Enter Duration of movie(Min): ').title() + ' min',
            'Ticket Price (PKR)': int(input('Enter Price of movie (PKR): '))  
        }
        data.append(new_movie)
        refresh_movie(data)
        print(f"Movie '{new_movie['Title']}' added successfully!")            
    except ValueError:
         print("Invalid input! Ensure the ticket price is an integer.")

def search_movie(data):
    """Search for movies by genre and language"""
    try:
        from tabulate import tabulate
        import pandas as pd
    except ImportError:
        print("This feature requires 'tabulate' and 'pandas' libraries.")
        print("Please install them using: pip install tabulate pandas")
        return
    
    genre_list=['Any']
    language_list=['Any']
    for movie in data:
        if movie['Genre'] not in genre_list:
         genre_list.append(movie['Genre'])
    for movie in data:
        if movie['Language'] not in language_list:
         language_list.append(movie['Language'])
    con='y'
    while con=='y':
        data2 = []
        user_genre=input(f'Write genre from {genre_list}: ').title()
        user_language=input(f'Write language from {language_list}: ').title()
        if user_genre=='Any' and user_language=='Any':
                data2=data       
        elif user_genre=='Any' and user_language in language_list:
                for key in data:
                    if key['Language']==user_language:
                        data2.append(key) 
        elif user_language=='Any' and user_genre in genre_list:
                 for key in data:
                      if key['Genre'] == user_genre:
                          data2.append(key)
        elif user_genre in genre_list and user_language in language_list:
                 for key in data:
                     if key['Genre'] == user_genre and key['Language']==user_language:
                          data2.append(key)     
        else:
                print('Sorry, there are no available movies of this type.')

        df = pd.DataFrame(data2)
        print(tabulate(df, headers='keys', tablefmt='grid'))
        con=input('Do you want to continue (y/n): ')
        if con!='y':
            break

def update_movie(data):
    """Update movie information"""
    show_movie()  
    movie_id = int(input('\nEnter the Movie ID you want to update: '))
    
    selected_movie =[]

    for key in data:
        if key['Movie ID'] == movie_id:
            selected_movie = key
            break
    else:
        print("Movie ID not found.")
        return  
    
    movie = selected_movie['Title']
    
    try:
        while True:
            field_to_change = input(f'Write what you want to change in movie "{movie}" from (Genre, Language, Ticket Price): ').lower()
            
            if field_to_change == 'genre':
                new_genre = input(f'Enter the new genre for "{movie}": ').title()
                selected_movie['Genre'] = new_genre
                print(f"Genre updated to: {new_genre}")
            elif field_to_change == 'language':
                new_language = input(f"Enter the new language for '{movie}': ").title()
                selected_movie['Language'] = new_language
                print(f"Language updated to: {new_language}")
            elif field_to_change == 'ticket price':
                new_price = int(input(f"Enter the new ticket price (PKR) for '{movie}': "))
                selected_movie['Ticket Price (PKR)'] = new_price
                print(f"Ticket price updated to: PKR {new_price}")
            else:
                print("Invalid field. Please choose from 'Genre', 'Language', or 'Ticket Price'.")
                continue
                
            another_update = input("Do you want to update another field? (yes/no): ").strip().lower()
            if another_update not in ['yes', 'y']:
                break
        
        refresh_movie(data)
        print(f"Movie '{movie}' updated successfully!")
        
    except ValueError:
        print("Invalid input! Please ensure numeric values are entered correctly.")

def delete_movie(data):
    """Delete a movie"""
    show_movie()  
    movie_id = int(input('Enter the Movie ID you want to delete: '))
    
    for i, movie in enumerate(data):
        if movie['Movie ID'] == movie_id:
            movie_title = movie['Title']
            confirmation = input(f"Are you sure you want to delete '{movie_title}'? (yes/no): ").strip().lower()
            if confirmation in ['yes', 'y']:
                data.pop(i)
                refresh_movie(data)
                print(f"Movie '{movie_title}' deleted successfully!")
            else:
                print("Deletion cancelled.")
            return
    
    print("Movie ID not found.")

def refresh_show(schedule):
    """Write show data to show.txt file"""
    with open("show.txt", "w") as file:
        file.truncate(0)  
        headers = f"{'Movie ID':<10} | {'Show ID':<30} | {'Date':<17} | {'Time':<10} | {'Screen Number'}\n"
        file.write(headers)
        
        for movie in schedule:
            file.write(f"{movie['Movie ID']:<10} | {movie['Show ID']:<30} | {movie['Date']:<17} | {movie['Time']:<10} | {movie['Screen Number']}\n")

def show_sch():
    """Display all shows"""
    refresh_show(schedule)
    with open("show.txt", "r") as file:
         print(file.read())

def add_show(schedule, data):
    """Add a new show"""
    last_show_id = schedule[-1]['Show ID']
    next_show_id = 'S' + str(int(last_show_id[1:]) + 1)
    
    show_movie()
    movie_id = int(input("Enter Movie ID for the show: "))
    
    # Check if movie exists
    movie_exists = any(movie['Movie ID'] == movie_id for movie in data)
    if not movie_exists:
        print("Movie ID not found. Please add the movie first.")
        return
    
    date = input("Enter show date (YYYY-MM-DD): ")
    time = input("Enter show time (HH:MM AM/PM): ")
    screen_number = int(input("Enter screen number: "))
    
    new_show = {
        'Movie ID': movie_id,
        'Show ID': next_show_id,
        'Date': date,
        'Time': time,
        'Screen Number': screen_number
    }
    
    schedule.append(new_show)
    refresh_show(schedule)
    print(f"Show '{next_show_id}' added successfully!")

def search_show(data, schedule):
    """Search for shows"""
    try:
        from tabulate import tabulate
        import pandas as pd
    except ImportError:
        print("This feature requires 'tabulate' and 'pandas' libraries.")
        return
    
    print("Search shows by:")
    print("1. Movie ID")
    print("2. Date")
    print("3. Screen Number")
    
    choice = input("Enter your choice: ")
    
    filtered_shows = []
    
    if choice == "1":
        movie_id = int(input("Enter Movie ID: "))
        filtered_shows = [show for show in schedule if show['Movie ID'] == movie_id]
    elif choice == "2":
        date = input("Enter date (YYYY-MM-DD): ")
        filtered_shows = [show for show in schedule if show['Date'] == date]
    elif choice == "3":
        screen_num = int(input("Enter screen number: "))
        filtered_shows = [show for show in schedule if show['Screen Number'] == screen_num]
    else:
        print("Invalid choice!")
        return
    
    if filtered_shows:
        df = pd.DataFrame(filtered_shows)
        print(tabulate(df, headers='keys', tablefmt='grid'))
    else:
        print("No shows found matching the criteria.")

def update_show(schedule, data):
    """Update show information"""
    show_sch()
    show_id = input("Enter Show ID to update: ")
    
    show_found = False
    for show in schedule:
        if show['Show ID'] == show_id:
            show_found = True
            print(f"Updating show: {show_id}")
            
            print("What would you like to update?")
            print("1. Date")
            print("2. Time") 
            print("3. Screen Number")
            
            update_choice = input("Enter your choice: ")
            
            if update_choice == "1":
                new_date = input("Enter new date (YYYY-MM-DD): ")
                show['Date'] = new_date
                print(f"Date updated to: {new_date}")
            elif update_choice == "2":
                new_time = input("Enter new time (HH:MM AM/PM): ")
                show['Time'] = new_time
                print(f"Time updated to: {new_time}")
            elif update_choice == "3":
                new_screen = int(input("Enter new screen number: "))
                show['Screen Number'] = new_screen
                print(f"Screen number updated to: {new_screen}")
            else:
                print("Invalid choice!")
                return
            
            refresh_show(schedule)
            print("Show updated successfully!")
            break
    
    if not show_found:
        print(f"Show with ID {show_id} not found.")

def delete_show(schedule):
    """Delete a show"""
    show_sch()
    show_id = input("Enter Show ID to delete: ")
    
    show_found = False
    for i, show in enumerate(schedule):
        if show['Show ID'] == show_id:
            show_found = True
            confirmation = input(f"Are you sure you want to delete show '{show_id}'? (yes/no): ").strip().lower()
            if confirmation in ['yes', 'y']:
                schedule.pop(i)
                refresh_show(schedule)
                print(f"Show '{show_id}' deleted successfully!")
            else:
                print("Deletion cancelled.")
            break
    
    if not show_found:
        print(f"Show with ID {show_id} not found.")

def refresh_booking(bookings):
    """Write booking data to bookings.txt file"""
    with open("bookings.txt", "w") as file:
        headers = f"{'Booking ID':<10} | {'Show ID':<10} | {'Customer Name':<30} | {'Contact Number':<20} | {'Number of Tickets'}\n"
        file.write(headers)

        for booking in bookings:
            content = f"{booking['Booking ID']:<10} | {booking['Show ID']:<10} | {booking['Customer Name']:<30} | {booking['Contact Number']:<20} | {booking['Number of Tickets']}\n"
            file.write(content)   

def view_bookings():
    """Display all bookings"""
    if not bookings:
        print("No bookings found.")
        return
    
    refresh_booking(bookings)
    with open("bookings.txt", "r") as file:
        print(file.read())

def book_ticket(schedule, data, bookings):
    """Book tickets for a show"""
    show_sch()
    show_id = input("Enter Show ID for booking: ")
    
    # Find the show
    show_details = None
    for show in schedule:
        if show['Show ID'] == show_id:
            show_details = show
            break
    
    if not show_details:
        print("Show ID not found.")
        return
    
    # Find movie details for pricing
    movie_details = None
    for movie in data:
        if movie['Movie ID'] == show_details['Movie ID']:
            movie_details = movie
            break
    
    if not movie_details:
        print("Movie details not found.")
        return
    
    print(f"Movie: {movie_details['Title']}")
    print(f"Show: {show_details['Show ID']} on {show_details['Date']} at {show_details['Time']}")
    print(f"Screen: {show_details['Screen Number']}")
    print(f"Ticket Price: PKR {movie_details['Ticket Price (PKR)']}")
    
    customer_name = input("Enter customer name: ")
    contact_number = input("Enter contact number: ")
    
    try:
        num_tickets = int(input("Enter number of tickets: "))
        if num_tickets <= 0:
            print("Number of tickets must be positive.")
            return
    except ValueError:
        print("Invalid number of tickets.")
        return

    price = movie_details['Ticket Price (PKR)']
    total_cost = num_tickets * price
    print(f"Total cost: PKR {total_cost}")

    if bookings!=[]:
        last_booking_id = bookings[-1]['Booking ID']
        next_booking_id = 'B' + str(int(last_booking_id[1:]) + 1)
    else:
        next_booking_id='B100'
        
    bookings.append({
        'Booking ID': next_booking_id,
        'Show ID': show_id,
        'Customer Name': customer_name,
        'Contact Number': contact_number,
        'Number of Tickets': num_tickets
    })
    refresh_booking(bookings)

    payment = input('Enter your payment option (1/2/3):\n 1. Debit Card\n 2. Credit Card\n 3. Easy Paisa\n')

    while True:
        if payment in ['1', '2', '3']:
            print('Processing...........') 
            time.sleep(2)
            print(f'Successful, {total_cost} deducted from {customer_name} Account.')
            break
        else:
            print("Invalid input. Please choose from (1/2/3).")
            payment = input('Enter your payment option (1/2/3): ')

    print("Booking Successful!")

    data2=[]
    data2.append({
        'Booking ID': next_booking_id,
        'Show ID': show_id,
        'Customer Name': customer_name,
        'Contact Number': contact_number,
        'Number of Tickets': num_tickets
    })

    try:
        from tabulate import tabulate
        import pandas as pd
        df = pd.DataFrame(data2)
        print(tabulate(df, headers='keys', tablefmt='grid'))
    except ImportError:
        print(f"Booking details: ID: {next_booking_id}, Show: {show_id}, Customer: {customer_name}")

def view_available_seats(schedule, bookings):
    """View available seats for shows"""
    max_seats_per_screen = 100  # Assuming 100 seats per screen
    
    show_sch()
    show_id = input("Enter Show ID to check available seats: ")
    
    # Find the show
    show_found = False
    for show in schedule:
        if show['Show ID'] == show_id:
            show_found = True
            # Calculate booked seats for this show
            booked_seats = 0
            for booking in bookings:
                if booking['Show ID'] == show_id:
                    booked_seats += booking['Number of Tickets']
            
            available_seats = max_seats_per_screen - booked_seats
            print(f"Show ID: {show_id}")
            print(f"Total Seats: {max_seats_per_screen}")
            print(f"Booked Seats: {booked_seats}")
            print(f"Available Seats: {available_seats}")
            break
    
    if not show_found:
        print("Show ID not found.")

def cancel_ticket(bookings):
    """Cancel a booking"""
    if not bookings:
        print("No bookings found.")
        return
    
    view_bookings()
    booking_id = input("Enter Booking ID to cancel: ")
    
    for i, booking in enumerate(bookings):
        if booking['Booking ID'] == booking_id:
            confirmation = input(f"Are you sure you want to cancel booking '{booking_id}' for {booking['Customer Name']}? (yes/no): ").strip().lower()
            if confirmation in ['yes', 'y']:
                bookings.pop(i)
                refresh_booking(bookings)
                print(f"Booking '{booking_id}' cancelled successfully!")
            else:
                print("Cancellation aborted.")
            return
    
    print("Booking ID not found.")

def total_sales_analysis(bookings, schedule, data):
    """Analyze total sales"""
    if not bookings:
        print("No bookings found for analysis.")
        return
    
    total_sales = 0
    
    for booking in bookings:
        show_id = booking['Show ID']
        num_tickets = booking['Number of Tickets']
        
        # Find the show to get movie ID
        movie_id = None
        for show in schedule:
            if show['Show ID'] == show_id:
                movie_id = show['Movie ID']
                break
        
        if movie_id:
            # Find the movie to get ticket price
            for movie in data:
                if movie['Movie ID'] == movie_id:
                    ticket_price = movie['Ticket Price (PKR)']
                    total_sales += num_tickets * ticket_price
                    break
    
    print(f"Total Sales: PKR {total_sales}")

def most_popular_movie(bookings, schedule, data):
    """Find the most popular movie"""
    if not bookings:
        print("No bookings found for analysis.")
        return
    
    # Dictionary to store movie ID and ticket count
    movie_ticket_count = {}
    
    for booking in bookings:
        show_id = booking['Show ID']
        num_tickets = booking['Number of Tickets']
        
        # Find the show to get movie ID
        for show in schedule:
            if show['Show ID'] == show_id:
                movie_id = show['Movie ID']
                if movie_id in movie_ticket_count:
                    movie_ticket_count[movie_id] += num_tickets
                else:
                    movie_ticket_count[movie_id] = num_tickets
                break
    
    if not movie_ticket_count:
        print("No movie data found.")
        return
    
    # Find the movie with maximum tickets
    most_popular_id = max(movie_ticket_count, key=movie_ticket_count.get)
    max_tickets = movie_ticket_count[most_popular_id]
    
    # Find the movie title
    most_popular_title = None
    for movie in data:
        if movie['Movie ID'] == most_popular_id:
            most_popular_title = movie['Title']
            break
    
    print(f"The most popular movie is '{most_popular_title}' with {max_tickets} tickets sold.")

def main():
    """Main function to run the movie booking system"""
    print("Welcome to the Movie Ticket Booking System!")
    while True:
        print("\nAre you an Admin or a Customer?")
        print("1. Admin")
        print("2. Customer")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            password=input('Enter password (hint:admin): ')
            if password=='admin':
                print("Successfully logined.....\nAdmin Panel")
                while True:
                    print("\nChoose an operation:")
                    print("1. Manage Movies")
                    print("2. Manage Shows")
                    print("3. View Bookings")
                    print("4. Analize Bookings")
                    print("5. Go Back")
                    admin_choice = input("Enter your choice: ")
    
                    if admin_choice == "1":
                        print("\nMovie Management:")
                        print("1. Add a Movie")
                        print("2. View All Movies")
                        print("3. Search for a Movie")
                        print("4. Update a Movie")
                        print("5. Delete a Movie")
                        movie_choice = input("Enter your choice: ")
    
                        if movie_choice == "1":
                            add_movie(data)
                        elif movie_choice == "2":
                            show_movie()
                        elif movie_choice == "3":
                            search_movie(data)
                        elif movie_choice == "4":
                            update_movie(data)
                        elif movie_choice == "5":
                            delete_movie(data)
                        else:
                            print("Invalid choice! Please try again.")
    
                    elif admin_choice == "2":
                        print("\nShow Management:")
                        print("1. Add a Show")
                        print("2. View All Shows")
                        print("3. Search for a Show")
                        print("4. Update a Show")
                        print("5. Delete a Show")
                        show_choice = input("Enter your choice: ").strip()
    
                        if show_choice == "1":
                            add_show(schedule,data)
                        elif show_choice == "2":
                            show_sch()
                        elif show_choice == "3":
                            search_show(data, schedule)
                        elif show_choice == "4":
                            update_show(schedule, data)
                        elif show_choice == "5":
                            delete_show(schedule)
                        else:
                            print("Invalid choice! Please try again.")
    
                    elif admin_choice == "3":
                        print("\nViewing All Bookings:")
                        view_bookings()
                    elif admin_choice == "4":
                        print("1. Analize the Total Sales")
                        print("2. Analize which is the most popular movie")
                        analysis_choice = input("Enter your choice: ").strip()
                        if analysis_choice == "1":
                            total_sales_analysis(bookings,schedule,data)
                        elif analysis_choice == "2":
                            most_popular_movie(bookings, schedule, data)
                        else:
                            print("Invalid choice! Please try again.")
                        
                    elif admin_choice == "5":
                        print("Returning to main menu...")
                        break
    
                    else:
                        print("Invalid choice! Please try again.")
            else:
                print("Invalid password!")

        elif choice == "2":
            print("\nCustomer Panel")
            while True:
                print("\nChoose an operation:")
                print("1. View Movies")
                print("2. Search for a Movie")
                print("3. View Shows")
                print("4. Search for a Show")
                print("5. Book Tickets")
                print("6. View Available Seats")
                print("7. Cancel Tickets")
                print("8. Go Back")
                customer_choice = input("Enter your choice: ").strip()

                if customer_choice == "1":
                    show_movie()
                elif customer_choice == "2":
                    search_movie(data)
                elif customer_choice == "3":
                    show_sch()
                elif customer_choice == "4":
                    search_show(data, schedule)
                elif customer_choice == "5":
                    book_ticket(schedule,data, bookings)
                elif customer_choice == "6":
                    view_available_seats(schedule, bookings)
                elif customer_choice == "7":
                    cancel_ticket(bookings)
                elif customer_choice == "8":
                    print("Returning to main menu...")
                    break
                else:
                    print("Invalid choice! Please try again.")

        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()