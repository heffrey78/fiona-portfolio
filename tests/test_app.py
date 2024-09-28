import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_portfolio_status_code(self):
        response = self.app.get('/portfolio')
        self.assertEqual(response.status_code, 200)

    def test_personal_work_status_code(self):
        response = self.app.get('/personal-work')
        self.assertEqual(response.status_code, 200)

    def test_project_status_code(self):
        response = self.app.get('/project')
        self.assertEqual(response.status_code, 200)

    def test_about_status_code(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)

    def test_contact_status_code(self):
        response = self.app.get('/contact')
        self.assertEqual(response.status_code, 200)

    def test_contact_form_submission(self):
        response = self.app.post('/contact', data=dict(
            name="Test User",
            email="test@example.com",
            message="This is a test message"
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Thank you for your message!', response.data)

    def test_home_content(self):
        response = self.app.get('/')
        self.assertIn(b'Welcome to My Portfolio', response.data)

    def test_portfolio_content(self):
        response = self.app.get('/portfolio')
        self.assertIn(b'Portfolio', response.data)

    def test_personal_work_content(self):
        response = self.app.get('/personal-work')
        self.assertIn(b'Personal Work', response.data)

if __name__ == '__main__':
    unittest.main()