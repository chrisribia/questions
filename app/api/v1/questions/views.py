from flask import jsonify, make_response, request
from flask_restful import Resource

from .modules import QuestionModel

def non_existance():
     return jsonify({
                    "status": 404,
                    "error": "question does not exist"
                })




class Quest(Resource):
    """docstring for Quest class"""

    def __init__(self):
        """initiliase the Quest class"""
        self.db = QuestionModel()


    def post(self):
        """docstring for saving a Quest"""
        question_id = self.db.save()
      
        return make_response(jsonify({
            "status": 201,
            "data": {
                "id": question_id,
                "message": "question added"
            }
        }), 201)
