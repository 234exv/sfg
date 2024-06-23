from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/l7', methods=['GET'])
def handle_l7_request():
    auth_key = request.args.get('auth_key')
    url = request.args.get('url')
    time = request.args.get('time')
    method = request.args.get('method')
    if auth_key == 'KGhbMFhFnmAFJ':
        if method == "CFB":
            subprocess.Popen(['node Danu-Tls.js ', url, time, "10", "15", "proxy.txt"], cwd='/root/test')
        if method == "TRN":
            subprocess.Popen(['node http.js GET', url, time, "10", "15", "proxy.txt"], cwd='/root/test')
        return 'Send'
    else:
        return 'Unauthorized', 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8484)
