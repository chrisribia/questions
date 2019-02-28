import datetime
from flask import jsonify, make_response, request
from flask_restful import Resource

questions = []


class QuestionModel():
    """Class with methods to perform CRUD operations on the DB"""

    def __init__(self):
        self.db = questions
        if len(self.db)  == 0:
            self.id = 1
        else: 
            self.id = len(self.db)+1

        

    def save(self):
                
        data = {
            'id': self.id,
            'title': request.json.get('title'),
            'question':request.json.get('question'),
            'dateposted': datetime.datetime.utcnow()             
        }
        self.db.append(data)
        return self.id
