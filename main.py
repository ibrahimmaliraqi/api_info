import requests
import time
import random
from fake_useragent import UserAgent
from flask import Flask ,request ,jsonify 
us = UserAgent()
UserAgent = us.random
app = Flask(__name__)
@app.route("/")
def instalog():
    USERNAME = request.args.get("email")
    if not USERNAME:
        return jsonify({"error":"you must put an email."})
    PASSWORD = "skjdjdjs8.Udh"
    session = requests.Session()
    session.headers = ({
        'User-Agent': UserAgent,
        'X-Requested-With': 'XMLHttpRequest',
        'X-Csrftoken':''.join(random.choice('YqhRSXWMvC91NqaaYkEPvlSGP3oEFEq0')for _ in range(32)),
    });tim = int(time.time())
    data = ({
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{PASSWORD}',
    'username':f'{USERNAME}'
    });response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/',
        headers=session.headers,
        data=data
    );res = response
    if ('"authenticated":false') in res.text:
        return jsonify({"code":"true"})
    else:
        return jsonify({"code":"false"})
