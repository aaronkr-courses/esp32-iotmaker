( 여기에 'ai-patterns.md'를 붙여 넣어세요. )

components:
- 프로그램_앞부분

gas_value = 0
gas_threshold = 200
brightness = 0
TELEPERIOD = 5 

def on_connect_more():
    print('on_connect_more()...')

def callback_more(topic:str,msg:str):
    global gas_threshold
    
    components:
    - set_on_off_str:
        이름: led_1
        토픽: LED_1

    components:
    - variable_int:
        prefix: el
        토픽: THRESHOLD
        변수: gas_threshold
        
    display_oled()

def read_sensors_more():

    global brightness,gas_value

    data1 = bh1750.read()
    print(data1)
    p = Parse(data1)
    brightness = p.value
    
    gas_value = gas.read()
    data2 = {"gas": {{"value": gas_value}}}
    print(f'gas:{{gas_value}}')   

    if gas_value > gas_threshold:
        bz.begin_blink(on=300,off=200)
    else:
        bz.end_blink()

    display_oled()

    data1.update(data2) # 2 개의 딕셔너리 결합
    
    return data1

def pir_on():
    mqtt.publish(f'tele/{C.DEVICE}/PIR','on',retain=True)
    print('PIR on')

def pir_off():
    mqtt.publish(f'tele/{C.DEVICE}/PIR','off',retain=True)
    print('PIR off')

def display_oled(): 
    oled.fill(0)  # 화면 지우기
    draw_hangul(oled, '가스조도' 0, 0) 
    oled.text(str(gas_value)+'/'+str(gas_threshold), 0, 20) 
    oled.text(str(brightness),0, 32)
    oled.show()  # OLED 화면 업데이트

components:
- i2c:
    scl_pin: Pin(P.SCL)
    sda_pin: Pin(P.SDA)

- 바이너리_센서:
    이름: pir
    pin_instance: Pin(P.PIR_IN,Pin.IN)
    run_instance: run
    inverted: False
    callback_on: pir_on
    callback_off: pir_off

- 조도:
    이름: bh1750

- LED:
    이름: led_1
    pin_instance: Pin(P.LED_1_IN,Pin.OUT)
    inverted: False

- 아날로그 센서:
    이름: gas
    pin_instance: Pin(P.A0_IN)

- 부저:
    이름: bz
    pin_instance: Pin(P.BUZZER_IN,Pin.OUT)

- OLED

- 타이머:
    이름: timer_oled
    period: 3*1000
    callback: display_oled

- 프로그램_뒷부분
