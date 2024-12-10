import pytest
import sqlite3
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test de l'API /get_cycle_data
def test_get_cycle_data(client):
    # Test avec un ID valide
    response = client.get('/get_cycle_data?id=1')
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'predicted_value' in json_data
    assert 'actual_value' in json_data

    # Test avec un ID invalide
    response = client.get('/get_cycle_data?id=9999')
    assert response.status_code == 404
    json_data = response.get_json()
    assert 'error' in json_data

    # Test sans ID
    response = client.get('/get_cycle_data')
    assert response.status_code == 400
    json_data = response.get_json()
    assert 'error' in json_data
