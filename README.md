**Job Application Tracker**

A simple, efficient Command Line Interface (CLI) tool built with Python to help job seekers organize their job search. This application allows users to track companies, manage salary offers, and analyze their potential earnings.

**Features**

- Create: Add new job applications with company name and salary offer.

- Read: View all current applications in a formatted list.

- Update: Edit existing entries to correct company names or update salary offers.

- Delete: Remove applications that are no longer relevant.

- Analyze: Automatically calculate the average salary across all your job offers.

- Safety: Includes error handling to prevent crashes from invalid input (e.g., typing text instead of numbers).

**Built With**

Language: Python 3

**Concepts Used**

- Lists & Dictionaries

- CRUD Logic (Create, Read, Update, Delete)

- Input Validation (try/except)

- Control Flow (Loops & Conditionals)

**How to Run?**

Prerequisite: Ensure you have Python installed on your computer.

1. Download: Download the job_tracker.py file.

2. Run: Open your terminal or command prompt, navigate to the folder, and type:

python job_tracker.py


**Usage Example**

--- My Job Applications Tracker ---
1. Add New Job Application
2. View All Applications
3. Calculate Average Salary Offer
4. Delete an Application
5. Update an Application
6. Exit

Enter your choice (1-6): 1
Enter company name: Google
Enter the salary offer: 120000
Application for Google added successfully.


**Future Improvements**

Persistence: Add Save/Load functionality (CSV/JSON) so data isn't lost when the program closes.

Search: Filter jobs by salary range or name.

GUI: Build a graphical window.

Author
Oubah