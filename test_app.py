"""
Unit tests for the Flask backend application
Run with: pytest test_app.py -v
"""
import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestHomeEndpoint:
    """Tests for the home endpoint"""
    
    def test_home_returns_200(self, client):
        """Test that home endpoint returns status code 200"""
        response = client.get('/')
        assert response.status_code == 200
    
    def test_home_returns_success_status(self, client):
        """Test that home endpoint returns success status"""
        response = client.get('/')
        data = response.get_json()
        assert data['status'] == 'success'
    
    def test_home_returns_message(self, client):
        """Test that home endpoint returns correct message"""
        response = client.get('/')
        data = response.get_json()
        assert 'CI/CD Pipeline' in data['message']


class TestHealthEndpoint:
    """Tests for the health check endpoint"""
    
    def test_health_returns_200(self, client):
        """Test that health endpoint returns status code 200"""
        response = client.get('/health')
        assert response.status_code == 200
    
    def test_health_returns_healthy_status(self, client):
        """Test that health endpoint returns healthy status"""
        response = client.get('/health')
        data = response.get_json()
        assert data['status'] == 'healthy'
    
    def test_health_returns_version(self, client):
        """Test that health endpoint returns version"""
        response = client.get('/health')
        data = response.get_json()
        assert 'version' in data


class TestAddEndpoint:
    """Tests for the add endpoint"""
    
    def test_add_returns_200(self, client):
        """Test that add endpoint returns status code 200"""
        response = client.get('/api/add')
        assert response.status_code == 200
    
    def test_add_returns_correct_result(self, client):
        """Test that add endpoint returns correct calculation"""
        response = client.get('/api/add')
        data = response.get_json()
        assert data['result'] == 2
        assert data['operand1'] == 1
        assert data['operand2'] == 1
    
    def test_add_returns_operation_type(self, client):
        """Test that add endpoint identifies operation type"""
        response = client.get('/api/add')
        data = response.get_json()
        assert data['operation'] == 'add'


class TestSimpleArithmetic:
    """Tests for basic arithmetic (as per assignment sample)"""
    
    def test_basic_addition(self):
        """Sample test from assignment"""
        assert 1 + 1 == 2
    
    def test_addition_with_larger_numbers(self):
        """Extended arithmetic test"""
        assert 5 + 10 == 15
        assert 100 + 50 == 150
