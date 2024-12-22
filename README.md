# Movie-booking-system
Simple Python Project (Semester 1) showcasing foundational Python concepts while offering a detailed and feature-rich Movie Ticket Booking System with separate Admin and Customer modules.
## Movie Booking System
## Project Overview
The Movie Booking System is a command-line-based application that allows cinema admins to manage movies, shows, and bookings, while customers can browse movies, book tickets, and manage their reservations.

This system is ideal for small to medium-sized cinemas looking to automate their operations and improve efficiency.

## Features
### Admin Module
Manage Movies: Add, update, delete, and search for movies by genre or language.
Show Scheduling: Schedule shows, update details, or remove them.
Booking Management: Monitor ticket bookings and cancellations.
Reports and Analysis: Access insights like total sales and most popular movies.
### Customer Module
Movie Browsing: View available movies and their details.
Real-Time Ticket Booking: Check seat availability, book tickets, and process payments.
Booking Management: Cancel tickets and view reservation details.
## Important Note
This project does not include persistent data storage. All updates made to movies, shows, or bookings are stored temporarily in variables during runtime. When the program is terminated and restarted:

Any updates made via the Admin Panel (e.g., adding or updating movies) will be reset.
Data loaded initially from files (like movies.txt) will overwrite any runtime changes.
To make data persistent, future versions of this system plan to integrate a relational database.

## Technologies Used
Programming Language: Python
Libraries:
tabulate: For formatting tabular data.
pandas: For data manipulation and analysis.
Setup Instructions
## Follow these steps to run the project locally:

### Clone the repository:


git clone https://github.com/fast-freshe/Movie-booking-system.git

### Ensure Python is installed on your system. Install required libraries:


pip install tabulate pandas
### Run the project:
python main.py

## Known Limitations
Non-persistent data: Updates to movies, shows, or bookings are session-based and will reset upon restarting the program.
File-based data: Current implementation relies on text files (movies.txt, etc.) for initial data loading.
## Future Development
* Database Integration: Transition to a relational database for persistent data management.
* GUI: Develop a graphical user interface using frameworks like Tkinter or PyQt.
* Advanced Features:
Online payment systems.
User reviews and ratings.
Loyalty rewards for frequent customers.
## License
This project is licensed under the MIT License. See the LICENSE file for details.
