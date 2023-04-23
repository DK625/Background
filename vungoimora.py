import requests
import json
API_TOKEN = "6225309479:AAG7ObpMu3-uetDluTc41ls2mlKxNGOkSRY"

response = requests.get("https://dog.ceo/api/breeds/image/random")
# response = requests.get("https://api.tumblr.com/v2/blog/gaixinhchonloc.com/posts/photo?api_key=OAuth_Consumer_Key")

data = json.loads(response.text)
image_url = data["message"]

url = f"https://api.telegram.org/bot{API_TOKEN}/sendPhoto"
payload = {"chat_id": -900121619, "photo": image_url}

response = requests.post(url, data=payload)
print(response.text)
