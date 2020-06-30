from app import app, db
import unittest


class FlaskTestCase(unittest.TestCase):

	#check flask was set up correctly
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/', content_type='html/text')
		self.assertEqual(response.status_code, 200)

	#
	def test_login_page_loads(self):
		tester = app.test_client(self)
		response = tester.get('/admin/', content_type='html/text')
		self.assertTrue(b'Please Login' in response.data)









if __name__ == '__main__':
	unittest.main()
