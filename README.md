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

## Build & Run Docker Image

###Step 1: Tag Your Docker Image

``` 
docker tag emad-app:latest emadeldin1/flask-todo-app:latest
```
### Step 2: Login to Docker Hub
``` 
docker login
```
### Step 3: Push to Docker Hub
```
docker push emadeldin1/flask-todo-app:latest
```
### Step4: Pull from Docker Hub
```
docker pull emadeldin1/flask-todo-app:latest
```
# flask-todo-app
