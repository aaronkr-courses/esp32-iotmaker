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