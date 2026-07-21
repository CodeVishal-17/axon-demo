from celery import Celery
celery_app = Celery('tasks', broker='pyamqp://guest@localhost//')

@celery_app.task
def background_job():
    print("Running in Celery")
