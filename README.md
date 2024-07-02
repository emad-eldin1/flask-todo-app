# Flask To-Do List Application

This is a simple To-Do List web application built with Flask. It allows users to add and delete tasks.

## Project Structure
```
flask_todo/
├── app.py
├── README.md
├── requirements.txt
├── tests/
│   ├── test_app.py
│   └── test_templates/
│       └── test_index.html
└── templates/
    └── index.html
```

## Requirements

- Python (version 3.6 or higher)
- Flask (`pip install Flask`)
- pytest (for running tests, `pip install pytest`)

## Setup Instructions

1. **Clone the repository** (if applicable) or download the source code.

2. **Navigate to the project directory**:

   ```sh
   cd flask_todo

## Create a virtual environment (optional but recommended):
 ```sh 
    python3 -m venv venv
```

## Activate the virtual environment:

```sh 
    source venv/bin/activate
```
## Install Flask:
```sh
    pip install Flask
```
## Running the Application:
```sh 
python app.py
```
## Running Tests
```
pytest
```
## Usage
- Adding a Task: Enter a task in the input field and click "Add Task".
- Deleting a Task: Click the "Delete" button next to the task you want to remove.
- The To-Do list updates dynamically with each action.

# flask-todo-app
