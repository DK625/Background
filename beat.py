from celery import Celery
from celery.schedules import crontab

app = Celery(
    'tasks', broker='amqp://roegjsyb:GLm6HM5YrT0XlJY34oJxPcyKFyftBv9-@armadillo.rmq.cloudamqp.com/roegjsyb')

# app.conf.beat_schedule = {
#     'send-dog-picture-to-telegram-every-1-minutes': {
#         'task': 'tasks.send_dog_picture_to_telegram',
#         'schedule': crontab(minute='*/1')
#     }
# }
app.conf.beat_schedule = {
    'send-dog-picture-to-telegram-every-10-seconds': {
        'task': 'tasks.send_dog_picture_to_telegram',
        'schedule': 10.0,
    }
}
# celery -A tasks worker --loglevel=info
# celery -A beat beat --loglevel=info
