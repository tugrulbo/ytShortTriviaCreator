from http import HTTPStatus
import requests
from models.QuestionModel import QuestionModel

from util.constants import BASE_URL


def getResponse():
    response = requests.get(BASE_URL)

    if(response.status_code == HTTPStatus.OK):
        print("Success Response")
        return response.json()


def getData():

    questionList: list = []
    json = getResponse()
    jsonSize = len(json["results"])
    print(f"Data Size: {jsonSize}")

    for i in range(0, jsonSize):
        dataCategory = json["results"][i]["category"]
        dataType = json["results"][i]["type"]
        dataDifficulty = json["results"][i]["difficulty"]
        dataQuestion = json["results"][i]["question"]
        dataCorrectAnswer = json["results"][i]["correct_answer"]

        model = QuestionModel(
            category=dataCategory,
            type=dataType,
            difficulty=dataDifficulty,
            question=dataQuestion,
            correct_answer=dataCorrectAnswer
        )

        questionList.append(model)

    return questionList
