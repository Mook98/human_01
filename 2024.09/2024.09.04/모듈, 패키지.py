#모듈 만들기(mod1.py파일로 저장)
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

#mod1.py 모듈 불러오기
import mod1
print(mod1.add(3, 4))
print(mod1.sub(4, 2))

#모듈이름 붙이지 않고 해당 모듈의 함수 사용 방법
from mod1 import add
add(3, 4)

from mod1 import add, sub
from mod1 import *

#클래스나 변수 등을 포함한 모듈
#mod2.py로 저장
PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r ** 2)

def add(a, b):
    return a + b

#mod2.py 모듈 실행
import mod2
print(mod2.PI)

a = mod2.Math()
print(a.solv(2))
print(mod2.add(mod2.PI, 4.4))

#다른 파일에서 모듈 불러오기
import sys
sys.path
sys.path.append("C:/Work")
sys.path

#다른 디렉토리에서 python 접속 후 모듈 실행
import mod2

#패키지 만들기
#다음과 같은 디렉토리에 .py파일 생성
#C:/Work/game/__init__.py
#C:/Work/game/sound/__init__.py
#C:/Work/game/sound/echo.py
#C:/Work/game/graphic/__init__.py
#C:/Work/game/grapgic/render.py

#echo.py 내용
def echo_test():
    print("echo")

#render.py 내용
def render_test():
    print("render")

#PYTONPATH 환경 변수 추가(CMD에서 실행)
#set PYTHONPATH=C:/Work/game

#echo 모듈 import하여 실행
import game.sound.echo
game.sound.echo.echo_test()

#from ... import로 echo 모듈 실행
#exit() #오류 발생할 수 있기 때문에 인터프리터 종료 후 다시 실행
#python
from game.sound import echo
echo.echo_test()

#echo 모듈 echo_test 함수 직접 import
from game.sound.echo import echo_test
echo_test()

#패키지 변수 및 함수 정의
#C:/Work/game/__init__.py 파일에 공동 변수나 함수 정의
VERSION = 3.5

def print_version_info():
    print(f"The version of this game is {VERSION}.")

#실행
import game
print(game.VERSION)
game.print_version_info()

#C:/Work/game/__init__.py 파일에 다른 모듈 import 하여 사용
from .graphic.render import render_test

VERSION = 3.5

def print_version_info():
    print(f"The version of this game is {VERSION}.")

#실행
import game
game.render_test()

#패키지 초기화
#C:/Work/game/__init__.py 파일에 처음 불러올 때 실행되어야 하는 코드 작성
from .graphic.render import render_test

VERSION = 3.5

def print_version_info():
    print(f"The version of this game is {VERSION}.")

print("Initializing game")

#실행
import game
#하위 모듈 함수 불러올 때도 실행된다
from game.graphic.render import render_test

#__all__
#모듈을 *를 사용하여 import 할 때에는 init파일에 all 변수 설정
#C:/Work/game/sound/__init__.py 파일에 작성
__all__ = ['echo']

#실행
from game.sound import *
echo.echo_test()

#relative 패키지
#render 모듈에서 echo 모듈 사용하기(relative 이용)
from ..sound.echo import echo_test

def render_test():
    print("render")
    echo_test()

#실행
from game.sound.echo import echo_test
render_test()