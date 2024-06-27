import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    """Test the index page"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do List' in response.data

def test_add_task(client):
    """Test adding a new task"""
    response = client.post('/add', data={'task': 'Test Task'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Test Task' in response.data

def test_delete_task(client):
    """Test deleting a task"""
    # Add a task first
    client.post('/add', data={'task': 'Task to be deleted'}, follow_redirects=True)
    # Delete the task
    response = client.post('/delete/0', follow_redirects=True)
    assert response.status_code == 200
    assert b'Task to be deleted' not in response.data

