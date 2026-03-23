from flask import Flask, render_template
import socket
import requests

app = Flask(__name__)


def get_private_ip():
    return socket.gethostbyname(socket.gethostname())


def get_public_ip():
    try:
        return requests.get("https://api.ipify.org").text
    except:
        return "Cannot get public IP"


@app.route('/')
def home():
    private_ip = get_private_ip()
    public_ip = get_public_ip()

    return render_template(
        'index.html',
        private_ip=private_ip,
        public_ip=public_ip
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)