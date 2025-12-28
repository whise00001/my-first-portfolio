import os
from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()
app = Flask(__name__)
db_user = os.getenv("USER_ID")

@app.route('/')
def home():
    # 將 .env 讀取到的 db_user 傳遞給模板，命名為 username
    return render_template('index.html', username=db_user)

if __name__ == '__main__':
    app.run(debug=True)