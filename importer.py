__author__ = 'lifenjoy51'
#구글문서에서 스프레드시트를 읽고 저장한다.
#DB연동을 하지 않고 그냥 파일로 저장한다.
#파일경로는 db/words.txt

import os

#클래스를 사용하지 않고. 단순 구분자만 넣어서 작업한다.

fout = open("words.txt", "w", encoding='utf-8')
fout.write('test')
fout.close()