## AI 프롬프트 실습 9-4: BH1750의 조도 값을 OLED에 표시하기
## 프롬프트 
file: ai-9-4-bh1750-oled.md
```
( 여기에 'ai-patterns.md'의 내용을 붙여 넣으세요. )

components:
- 센서읽기_앞부분

brightness = 0

components:

- i2c:
    scl_pin: Pin(P.SCL)
    sda_pin: Pin(P.SDA)
- 조도:
    이름: bh1750
- OLED

def display_oled():
    oled.fill(0)
    draw_hangul(oled,'조도',0,0)
    oled.text(f'{brightness} lx',0,20)
    oled.show()

def sensor_read():
    global brightness
    data = bh1750.read()
    print(data)
    p = Parse(data)
    brightness = p.value
    print(f'{p.key}: {p.value}')
    display_oled()

components:
- 타이머:
    이름: timer_sensor
    period: 5*1000
    callback: sensor_read

- 센서읽기_뒷부분
```
## AI가 만든 코드
프로그램: 9_5_bh1750_oled.py
```python
from machine import Pin, I2C
from timerrun import TimerRun
from run import Run
from parse import Parse
import pinno as P

brightness = 0

run = Run()

# I2C 설정
i2c = I2C(0, scl=Pin(P.SCL), sda=Pin(P.SDA))

# 조도 센서 설정
from bh1750sensor import BH1750Sensor
bh1750 = BH1750Sensor(i2c)

# OLED 디스플레이 설정
from ssd1306 import SSD1306_I2C  # OLED 라이브러리
from hangul import draw_hangul, V2, H2, X4  # 한글 출력 모듈
WIDTH = 64
HEIGHT = 48
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

def display_oled(): 
    oled.fill(0)
    draw_hangul(oled, '조도', 0, 0)
    oled.text(f'{brightness} lx', 0, 20)
    oled.show()

def sensor_read():
    global brightness
    data = bh1750.read()  # bh1750 센서에서 데이터를 읽어옴
    print(data)
    p = Parse(data)
    brightness = p.value
    print(f'{p.key}: {p.value}')

    display_oled()

# 타이머 설정
timer_sensor = TimerRun(period=5*1000, callback=sensor_read)
run.add(timer_sensor.run)

def main(): 
    while True:
        run.run()

if __name__ == '__main__':
    main()
```