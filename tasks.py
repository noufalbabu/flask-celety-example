from celery import Celery

# app = Celery('tasks', backend='redis://localhost', broker='pyamqp://')
app = Celery('tasks',broker='amqp://localhost//', backend='db+sqlite:///results.sqlite')
# app = Celery('tasks',broker='amqp://noufal:noufal123@localhost/noufal_vhost')
# app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def reverse(string):
	return string[::-1]