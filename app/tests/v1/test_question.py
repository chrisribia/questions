import json
import unittest

from ... import create_app


class QuestionTestCase(unittest.TestCase):
    """
    This class represents the question test cases
    """

    def setUp(self):
        APP = create_app("testing")
        self.app = APP.test_client()

        self.question = {
            "created_By": 1,
            "title": "How to write tests",
            "question": "I was wondering  how do u write tests"

        }
 
    def test_post_question(self):
        """method to test post a question endpoint"""
        response = self.app.post("/api/v1/questions",
                                 headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.question))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            result['data']['message'], "question added")
        self.assertEqual(
        result['status'], 201)