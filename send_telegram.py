# import requests
# import json
# import time
# from celery import Celery
# import pika

# app = Celery(
#     'tasks', broker='amqps://roegjsyb:GLm6HM5YrT0XlJY34oJxPcyKFyftBv9-@armadillo.rmq.cloudamqp.com/roegjsyb')


# @app.task
# def send_dog_photo():
#     # Lấy một hình ảnh chó ngẫu nhiên từ API Dog
#     dog_url = 'https://dog.ceo/api/breeds/image/random'
#     response = requests.get(dog_url)
#     json_data = json.loads(response.text)
#     dog_photo_url = json_data['message']

#     # Gửi hình ảnh chó vào hàng đợi của RabbitMQ
#     rabbitmq_url = 'amqps://roegjsyb:GLm6HM5YrT0XlJY34oJxPcyKFyftBv9-@armadillo.rmq.cloudamqp.com/roegjsyb'
#     connection = pika.BlockingConnection(pika.URLParameters(rabbitmq_url))
#     channel = connection.channel()
#     channel.queue_declare(queue='dog_photo')
#     channel.basic_publish(
#         exchange='', routing_key='dog_photo', body=dog_photo_url)
#     connection.close()

#     # Gửi hình ảnh chó đến chatbot của Telegram
#     telegram_bot_token = '6225309479:AAG7ObpMu3-uetDluTc41ls2mlKxNGOkSRY'
#     telegram_chat_id = '-900121619'
#     telegram_api_url = f'https://api.telegram.org/bot{telegram_bot_token}/sendPhoto'
#     response = requests.post(telegram_api_url, data={
#                              'chat_id': telegram_chat_id, 'photo': dog_photo_url})
#     print(response.text)


# # Lặp lại task sau mỗi 10 phút
# while True:
#     send_dog_photo.delay()
#     time.sleep(600)  # đợi 10 phút
