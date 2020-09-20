import unittest
import connexion

class TestPing(unittest.TestCase):

    def setUp(self):
        self.app =  connexion.FlaskApp(__name__, specification_dir='../swagger/')
        self.app.add_api('api.yaml')


    def test_status_code(self):
        response = self.app.app.test_client().get('/v1/ping')
        self.assertEqual(response.status_code, 200)
        self.assertTrue("PONG" in str(response.data))

if __name__ == '__main__':
    unittest.main()