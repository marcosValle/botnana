import sys
import requests
import threading

data={
	'os':sys.platform
}

def sendReq():
    threading.Timer(5.0, sendReq).start()
    r = requests.get("http://127.0.0.1:5000/botPing/9002", data=data)

sendReq()
