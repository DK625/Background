import requests
from celery import Celery, Task
import os
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
# Vì Celery version 5.2.7 không hỗ trợ trên Windows do phụ thuộc vào các tính năng của eventlet
# Dùng gevent thay thế cho eventlet
# Cài đặt gevent: pip install gevent
# Để sử dụng gevent --> thêm os

app = Celery(
    'tasks', broker='amqp://roegjsyb:GLm6HM5YrT0XlJY34oJxPcyKFyftBv9-@armadillo.rmq.cloudamqp.com/roegjsyb')


@app.task
def send_dog_picture_to_telegram():
    # Lấy URL của hình chó từ API Dog
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    image_url = response.json()['message']

    # Gửi hình ảnh đến Telegram
    bot_token = '6225309479:AAG7ObpMu3-uetDluTc41ls2mlKxNGOkSRY'
    chat_id = -900121619
    url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'
    data = {'chat_id': chat_id}
    files = {'photo': requests.get(image_url).content}
    requests.post(url, data=data, files=files)
