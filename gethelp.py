from flask import Flask
from twilio.rest import Client

app = Flask(__name__)

# Find these values at https://twilio.com/user/account
account_sid = "ACe9d2cb48926ff9ae14b8163bfdcb1c7b"
auth_token = "6fde649d783d3b5eda8ceec374076ca6"

client = Client(account_sid, auth_token)


@app.route('/')
def hello_world():
    sendText()
    return 'We\'ve sent help'


def sendText():
    client.api.account.messages.create(
        to="+447508383843",
        from_="+447481342827",
        body="Jack has fallen")
