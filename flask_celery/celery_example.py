from flask import Flask
from flask_celery import make_celery

app = Flask(__name__)

app.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
app.config['CELERY_BACKEND'] = 'db+sqlite:///results.sqlite'


celery = make_celery(app)

@app.route('/process/<name>/')
def process(name):
    reverse.delay(name)
    return name

@celery.task(name='celery_example.reverse')
def reverse(string):
    return string[::-1]
if __name__ == "__main__":
    app.run(debug=True)