from twilio.rest import Client

account_sid = 'AC7a3c063ecf050c7c6b67642008a0c37e'
auth_token = '5f66224ad8d79624a3270607245fc119'
client = Client(account_sid, auth_token)
twilio_number = 'whatsapp:+14155238886'

def send_whatsapp_message(to, body):
    message = client.messages.create(
    from_=twilio_number,
    body=body,
    to= f'whatsapp:{to}'
    )
    return (message.sid)