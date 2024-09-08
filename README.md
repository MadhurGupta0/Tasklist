# Task List Web App

This Django web application provides a "Task List" page that displays tasks from a database, allowing users to filter by status and sort by priority or due date. The app includes basic unit tests for filtering and sorting functionality.

## Table of Contents
1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Testing](#testing)
6. [Code Overview](#code-overview)
7. [Contributing](#contributing)

## Features
- Task model with fields: `title`, `description`, `due_date`, `priority`, and `status`.
- Ability to filter tasks by their `status`.
- Ability to sort tasks by `priority` or `due_date`.
- A user-friendly interface for displaying tasks in a table format.
- Unit tests for filtering and sorting functionality.

## Requirements
- Python 3.8+
- Django 3.2+
- SQLite (default Django database)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MadhurGupta0/Tasklist/
   cd tasklist

2. **Create and activate a virtual environment:**

```bash
Always show details

python -m venv venv
source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
```
3. **Install the dependencies:**

```bash
Always show details

pip install -r requirements.txt
```
4. **Run the initial migrations:**

```bash
Always show details

python manage.py makemigrations
python manage.py migrate
```
5. **Create a superuser to access the admin panel (optional):**

```bash
Always show details

python manage.py createsuperuser
```
6. **Start the development server:**

```bash
Always show details


python manage.py runserver
```
7. **Access the application:**
    
Open your web browser and navigate to http://localhost:8000/.

## Usage

The Task List page displays all tasks stored in the database.
- Users can filter tasks by their status (e.g., "To Do", "In Progress", "Done").
- Users can sort tasks by priority (High, Medium, Low) or due_date.

## Testing

Run the unit tests:

```bash
Always show details

python manage.py test
```
This will run the unit tests defined in the tests folder to verify filtering and sorting functionality.

## Code Overview

### Models

The Task model in home/models.py defines the following fields:

- title: CharField
- description: TextField
- due_date: DateField
- priority: IntegerField with choices (High, Medium, Low)
- status: CharField with choices ('To Do', 'In Progress', 'Done')

### Views

The task_list view in home/views.py handles:

- Filtering tasks by status.
- Sorting tasks by priority or due_date.

### Templates

task_list.html in home/templates/ provides a basic UI to display tasks in a table, with options to filter and sort.

### Tests

home/tests/test_tasks.py includes unit tests to check:

- Filtering by status.
- Sorting by priority and due_date.

## Contributing

Feel free to submit pull requests or open issues to improve the application. 



