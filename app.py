__author__ = 'lifenjoy51'

import os, random
from flask import Flask, request, send_from_directory, jsonify

app = Flask(__name__)

# 단어를 저장할 리스트.
word_list = []


@app.route("/")
def main():
    return send_from_directory('static', 'word.html')


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


@app.route("/hello")
def hello():
    return 'hello world!'


@app.route("/word")
def word():
    idx = random.randint(0, len(word_list))
    w = word_list[idx]
    print(w)
    return jsonify(w)


@app.route("/words")
def words():
    return jsonify(results=word_list)


# 파일에서 단어를 불러와 메모리에 올리는 함수.
def load():
    # 기존에 있던 목록을 삭제한다. 중복을 제거하기 위해.
    word_list.clear()

    #파일을 연다.
    fin = open("words.txt", "r", encoding='utf-8')
    #파일에서 한 줄씩 읽는다.
    for line in fin.read().splitlines():
        #단어를 저장할 딕셔너리를 생성.
        w = {}
        w['word'] = line.split("\t")[0]  #word에는 탭 앞에꺼
        w['meaning'] = line.split("\t")[1]  #meaning에는 탭 뒤어꺼
        #목록에 저장한다.
        word_list.append(w)
    #파일을 닫는다. 안닫으면 안됨!
    fin.close()


if __name__ == "__main__":
    load()  # 시작할 때 파일에서 불러온다.
    app.run(host='0.0.0.0')
