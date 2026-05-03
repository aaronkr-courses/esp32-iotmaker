

(여기에 'ai-patterns.md'의 내용을 붙여 넣으세요.)

components:
- 프로그램_앞부분

temperature = 0
humidity = 0
display_seq = 5 
TELEPERIOD = 10

def on_connect_more():
    print('on_connect_more()...')

def callback_more(topic:str,msg:str):
    
    components:
    - set_on_off_str:
        이름: relay
        토픽: RELAY

def read_sensors_more():
    
    global temperature,humidity

    data == dht.read()
    print(data)
    p = Parse(data)
    humidity = p.values[0]
    temperature = p.values[1]

    print(f'{p.keys[1]}: {p.values[1]}, {p.keys[0]}: {p.values[0]} ')
    
    return data

components:
- DHT22:
    이름: dht
    pin_gpio: P.DHT
- 릴레이:
    이름: relay
    pin_instance: Pin(P.RELAY_IN,Pin.OUT)
    inverted: false
- i2c:
    scl_pin: Pin(P.SCL)
    sda_pin: Pin(P.SDA)
- OLED

def display_oled(): 
    global display_seq
    
    display_seq += 1
    display_seq = display_seq % 2
    
    if display_seq == 0: 
        oled.fill(0)  # 화면 지우기
        draw_hangul(oled, '온도', 0, 0) 
        draw_hangul(oled, f'{temperature} C', 0, 20)
        #oled.text(f'{temperature} C', 0, 20) 
        oled.show()  # OLED 화면 업데이트
    else: 
        oled.fill(0)  # 화면 지우기
        draw_hangul(oled, '습도', 0, 0) 
        draw_hangul(oled, f'{humidity}', 0, 20)
        #oled.text(f'{humidity}', 0, 20) 
        oled.show()  # OLED 화면 업데이트    

- 타이머: 
    period: 3*1000
    callback: display_oled

- 프로그램_뒷부분
