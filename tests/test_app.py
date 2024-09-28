import unittest
from app import app
import json

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_status_code(self):
        response = self.app.get('/about')
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

    def test_contact_status_code(self):
        response = self.app.get('/contact')
        self.assertEqual(response.status_code, 200)

    def test_contact_form_submission(self):
        response = self.app.post('/contact', data=dict(
            name="Test User",
            email="test@example.com",
            subject="Test Subject",
            message="This is a test message"
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Thank you for your message!', response.data)

    def test_send_message_ajax(self):
        response = self.app.post('/send-message', data=dict(
            name="Test User",
            email="test@example.com",
            subject="Test Subject",
            message="This is a test message"
        ))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertIn('Thank you for your message!', data['message'])

    def test_portfolio_detail(self):
        response = self.app.get('/portfolio/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Project Details', response.data)

    def test_404_error(self):
        response = self.app.get('/nonexistent-page')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'404', response.data)
        self.assertIn(b'Page Not Found', response.data)

    def test_home_content(self):
        response = self.app.get('/')
        self.assertIn(b"Fiona's Portfolio", response.data)

    def test_about_content(self):
        response = self.app.get('/about')
        self.assertIn(b'About Me', response.data)

    def test_portfolio_content(self):
        response = self.app.get('/portfolio')
        self.assertIn(b'My Portfolio', response.data)

    def test_personal_work_content(self):
        response = self.app.get('/personal-work')
        self.assertIn(b'Personal Work', response.data)

    def test_contact_content(self):
        response = self.app.get('/contact')
        self.assertIn(b'Contact Me', response.data)

    def test_liveness_check(self):
        response = self.app.get('/liveness_check')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'OK')

    def test_readiness_check(self):
        response = self.app.get('/readiness_check')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'OK')

    def test_current_year_in_context(self):
        with app.test_request_context():
            from datetime import datetime
            current_year = datetime.utcnow().year
            self.assertEqual(app.jinja_env.globals['current_year'], current_year)

if __name__ == '__main__':
    unittest.main()