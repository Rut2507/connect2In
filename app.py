from flask import Flask, render_template, request
import threading
from linkedin_bot import LinkedInBot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    username = request.form['username']
    password = request.form['password']
    keywords = request.form['keywords']
    num_pages = int(request.form['num_pages'])
    thread = threading.Thread(target=start_bot, args=(username, password, keywords, num_pages))
    thread.start()
    return render_template('index.html')

def start_bot(username, password, keywords, num_pages):
    bot = LinkedInBot(username, password, keywords, num_pages)
    bot.run()

if __name__ == '__main__':
    app.run(debug=True)
