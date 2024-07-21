"""
Estimated time: 1 hour
Real time: 2 hour 23 min
"""
import os
from prac_07.project import Project
from datetime import datetime


def load_projects(filename):
    projects = []
    with open(filename, "r") as file:
        next(file)
        for line in file:
            projects.append(Project.from_string(line))
    return projects


def save_projects(filename, projects):
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(project.to_string() + "\n")


def display_projects(projects):
    incomplete_projects = [i for i in projects if not i.is_complete()]
    complete_projects = [i for i in projects if i.is_complete()]
    print("Incomplete projects:")
    for project in sorted(incomplete_projects, key=lambda p: p.priority):
        print(f"{project}")
    print("Completed projects:")
    for project in sorted(complete_projects, key=lambda p: p.priority):
        print(f"{project}")


def filter_projects(projects, date_string):
    date = datetime.strptime(date_string, "%d/%m/%Y")
    filtered_projects = [i for i in projects if i.start_date > date]
    for project in sorted(filtered_projects, key=lambda p: p.start_date):
        print(f"{project}")


def add_new_project(projects):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Completion percentage: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    project_choice = int(input("Project choice: "))
    project = projects[project_choice]

    new_completion_percentage = input("New completion percentage: ")
    new_priority = input("New priority: ")

    project.update(new_completion_percentage=int(new_completion_percentage) if new_completion_percentage else None,
                   new_priority=int(new_priority) if new_priority else None)


def main():
    projects = load_projects("projects.txt")

    MENU = """
    - (L)oad projects
    - (S)ave projects
    - (D)isplay projects
    - (F)ilter projects by date
    - (A)dd new project
    - (U)pdate project
    - (Q)uit
    """
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {"projects.txt"}")
    while True:
        print(MENU)
        choice = input(">>> ").upper()
        if choice == 'L':
            filename = input("Filename to load from: ")
            if os.path.exists(filename):
                projects = load_projects(filename)
                print(f"Loaded {len(projects)} projects from {filename}")
            else:
                print("File not found.")
        elif choice == 'S':
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects(projects, date_string)
        elif choice == 'A':
            add_new_project(projects)
        elif choice == 'U':
            update_project(projects)
        elif choice == 'Q':
            save_choice = input(f"Would you like to save to {"projects.txt"}? (Y/N): ").upper()
            if save_choice == 'Y':
                save_projects("projects.txt", projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please choose again.")


main()
