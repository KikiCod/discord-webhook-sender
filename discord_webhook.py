import requests

# Discord Webhook URL
your_webhook_url = 'webhookurl'

# Message to send to webhook
message = '@everyone Hello!'

# Preparing JSON data
data = {
    'content': message
}

# POST isteği gönderiliyor 50 defa
for i in range(50):
    response = requests.post(your_webhook_url, json=data)
    if response.status_code == 204:
        print('{}. message sent successfully!'.format(i+1))
    else:
        print('{}. message sending failed. Error code: {}'.format(i+1, response.status_code))
