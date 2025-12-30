import os
from dotenv import load_dotenv
from flask import Flask, render_template
from datetime import datetime
db_user = os.getenv("USER_ID")

load_dotenv()
app = Flask(__name__)

@app.route('/')
def home():
    hour = datetime.now().hour
    # 將 .env 讀取到的 db_user 傳遞給模板，命名為 username
    if 5 <= hour < 12:
        greeting = "早安"
    elif 12 <= hour < 18:
        greeting = "午安"
    else:
        greeting = "晚安"
    return render_template('index.html', 
                           username=db_user, 
                           greeting=greeting,
                           current_hour=hour)

@app.route('/about')
def about():
    # 當使用者輸入 /about 時，顯示 about.html
    return render_template('about.html')

if __name__ == '__main__':
    # 修改這行：增加 host="0.0.0.0" 並將 port 改為 8080
    app.run(host="0.0.0.0", port=8080)