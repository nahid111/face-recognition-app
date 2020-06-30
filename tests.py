import unittest
from tests_base import BaseTestCase


class FlaskTestCase(BaseTestCase):

	def test_index(self):
		response = self.client.get('/', content_type='html/text')
		self.assertEqual(response.status_code, 200)


	def test_login_page_loads(self):
		response = self.client.get('/admin/', follow_redirects=True)
		self.assertTrue(b'Please Login' in response.data)

	def test_logout(self):
		self.client.post(
			'/admin/',
			data = dict(username="admin", password="wrong"),
			follow_redirects=True
		)
		response = self.client.post('/logout', follow_redirects=True)
		self.assertIn(b'You have Logged Out Successfully', response.data)


	def test_login_required(self):
		response = self.client.get('/admin/home', follow_redirects=True)
		self.assertIn(b'Login to Continue', response.data)

	def test_login_to_admin_home_page(self):
		response = self.client.post(
			'/admin/',
			data = dict(username="admin", password="admin"),
			follow_redirects=True
		)
		self.assertIn(b'Welcome to the Admin Panel', response.data)


	def test_incorrect_login(self):
		response = self.client.post(
			'/admin/',
			data = dict(username="admin", password="wrong"),
			follow_redirects=True
		)
		self.assertIn(b'Password is incorrect', response.data)


	









if __name__ == '__main__':
	unittest.main()
