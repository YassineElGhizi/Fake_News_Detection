from flask import Flask, request
from machineLearningModels.fakeNewsPredector import fake_news_det
from machineLearningModels.sentimentAnalysis import sentimentAnalysis

from flask_cors import CORS

from flask_graphql import GraphQLView
from mongoengine import connect
from schema import schema


app = Flask(__name__)
CORS(app)
# connect("fake_news", host="mongodb://localhost/fake_news", alias="default")
r = connect("fake_news", host="mongodb://root:example@localhost:27017/fake_news?authSource=admin", alias="default")


@app.get('/')
def index():
    return "The App is Working"

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        a = request.get_json()
        pred = fake_news_det(str(a['message']))
        return str(pred)
    else:
        return "Ops!! il y un erreur [predict() method]"

@app.route('/sentiment', methods=['POST'])
def predict2():
    if request.method == 'POST':
        a = request.get_json()
        pred = sentimentAnalysis(str(a['sntmnt']))
        return str(pred)

    else:
        return "Ops!! il y un erreur [predict() method]"

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(  
        'graphql',
        schema=schema,
        graphiql=True,
    )
)

if __name__ == '__main__':
    app.run(debug=True)