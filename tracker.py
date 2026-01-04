#  SETUP ---
# Global variables and imports go here
job_list = []

# FUNCTIONS 
def print_menu():
    print("\n--- My Job Applications Tracker ---")
    print("1. Add New Job Application")
    print("2. View All Applications")
    print("3. Calculate Average Salary Offer")
    print("4. Delete an Application")
    print("5. Update an Application")
    print("6. Exit")

def add_job():
    """Ask user for details and add to list"""
    company = input("Enter company name: ")
    
    try:
        salary = float(input("Enter the salary offer: "))
        new_job = {"company": company, "salary": salary}
        
        job_list.append(new_job)
        print(f" Application for {company} added successfully.")
    except ValueError:
        print(" Error: Salary must be a number (no commas or symbols).")

def view_job():
    print("\n--- Current Applications ---")
    if not job_list:
        print("No applications found.")
    else:
        for app in job_list:
            print(f"Company: {app['company']} | Salary: ${app['salary']:,.2f}")

def calculate_average():
    if not job_list:
        print("No applications to calculate.")
    else:
        total_salary = 0
        for app in job_list:
            total_salary = total_salary + app['salary']
    
        avg = total_salary / len(job_list)
        print(f"💰 Average Salary across all options: ${avg:,.2f}")

def delete_job():
    name_to_delete = input("Enter the company name to delete: ")
    found = False
    
    for app in job_list:
        if app['company'] == name_to_delete:
            job_list.remove(app)
            found = True
            print(f"🗑️ {name_to_delete} has been deleted.")
            break 
    
    if not found:
        print(f"Company '{name_to_delete}' not found.")

def update_job():
    name_to_update = input("Enter the company name to update: ")
    found = False
    
    for app in job_list:
        if app['company'] == name_to_update:
            print(f"Found {name_to_update}. What would you like to change?")
            print("1. Company Name")
            print("2. Salary")
            update_choice = input("Enter 1 or 2: ")

            if update_choice == '1':
                new_name = input("Enter the new company name: ")
                app['company'] = new_name
                print(f"✅ Company name updated to {new_name}.")
            
            elif update_choice == '2':
                try:
                    new_salary = float(input(f"Enter new salary for {name_to_update}: "))
                    app['salary'] = new_salary
                    print(f"Salary updated to ${new_salary:,.2f}")
                except ValueError:
                    print(" Error: Salary must be a number.")
            
            else:
                print(" Invalid choice.")
            
            found = True
            break
            
    if not found:
        print(f" Company '{name_to_update}' not found.")

# MAIN EXECUTION 
# This is where the program actually starts running
while True:
    print_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_job()
    
    elif choice == '2':
        view_job()
    
    elif choice == '3':
        calculate_average()
    
    elif choice == '4':
        delete_job()

    elif choice == '5':
        update_job()

    elif choice == '6':
        print("Good luck with the job hunt! Goodbye.")
        break
    
    else:
        print("Invalid choice. Please try again.")