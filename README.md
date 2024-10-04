# Task Tracker

The Task Manager is a simple Python application that allows users to create, read, update, and delete tasks. It manages tasks using a JSON file as a database, ensuring persistent storage of task information. Each task includes attributes such as a unique ID, title, description, and completion status. The application provides a command-line interface for interacting with the task list and performing basic CRUD operations.

### Key Features:

- Create: Add new tasks with a title and description.
- Read: View the list of all tasks, including details like task ID, title, description, and status (completed or not).
- Update: Edit the title, description, or status of an existing task.
- Delete: Remove a task from the list.
- JSON Storage: Tasks are stored in a JSON file for easy persistence and retrieval.

This project is ideal for learning how to handle file I/O in Python and implement basic CRUD functionalities with a lightweight data storage approach.

### How to use:

Follow the steps to use application

 - Install the package with ```pip install -e pypi_packages/task_tracker/```.
 - Now you can execute this commands:
 
```python
# Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress
```

This project was built with methodology TDD and tested with pytest.

### Reference:

Link of project: https://roadmap.sh/projects/task-tracker