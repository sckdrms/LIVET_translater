from flask import Flask, request, render_template
import requests
import json
import webbrowser
import threading
from pathlib import Path
import tempfile

app = Flask(__name__)

# 네이버 Papago NMT API에 대한 클라이언트 ID와 클라이언트 시크릿을 입력하세요.
client_id = "mTtCqhKOF4HIt2NMhBIh"
client_secret = "d5CfF_r__q"

@app.route('/', methods=['GET', 'POST'])
def index():
    translation = ''
    selected_source = 'ko' # Default value
    selected_target = 'en' # Default value
    if request.method == 'POST':
        original_text = request.form.get('text')
        selected_target = request.form.get('language') 
        selected_source = request.form.get('source')

        headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}
        data = {"source": selected_source, "target": selected_target, "text": original_text}
        papago_url = "https://openapi.naver.com/v1/papago/n2mt"

        response = requests.post(papago_url, headers=headers, data=data)
        res = json.loads(response.text)
        translation = res['message']['result']['translatedText']

    return render_template('index.html', translation=translation, selected_source=selected_source, selected_target=selected_target)


if __name__ == '__main__':
    # 임시 파일을 사용하여 웹 브라우저가 이미 열려 있는지 확인
    temp_file = Path(tempfile.gettempdir()) / 'webbrowser_open.tmp'
    if not temp_file.exists():
        temp_file.touch()
        # 새로운 쓰레드에서 웹 브라우저를 연다.
        threading.Timer(1, lambda: webbrowser.open("http://localhost:5000")).start()

    try:
        # 모든 네트워크에서 접근 가능하도록 host를 0.0.0.0으로 설정.
        app.run(host='0.0.0.0', debug=True)
    finally:
        if temp_file.exists():
            temp_file.unlink()
