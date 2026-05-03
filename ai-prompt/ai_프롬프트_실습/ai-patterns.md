patterns:
    code:
        설명: '입력 받은 내용을 그대로 코드변환합니다'
        매개변수: text
        코드변환: |
            {{text}}    
    i2c:
        설명: 'i2c bus를 만든다.'
        매개변수: 
            i2c_bus: i2c       
            no: 0        
            scl_pin: P.SCL
            sda_pin: P.SDA
        코드변환: |
            from machine import I2C
            {{i2c_bus}} = I2C({{no}}, scl={{scl_pin}}, sda={{sda_pin}})
    spi:
        설명: 'spi bus를 만든다.'
        매개변수:
            spi_bus: spi
            no: 1
            sck_pin: P.SCK
            mosi_pin: P.MOSI
            miso_pin: P.MISO
        코드변환: |
            from machine import SPI
            {{spi_bus}} = SPI({{no}}, sck={{sck_pin}}, mosi={{mosi_pin}}, miso={{miso_pin}})
    sdcard_mount_make_next_file:
        매개변수:
            cs_pin: P.CS
            file_prefix: data
            file_digits: 3
            file_ext: json
        코드변환: |
            from usesdcard import UseSDCard 
            sd = UseSDCard(spi_bus=spi,cs_gpio={{cs_pin}})
            ok,msg = sd.mount_sdcard()
            ok, message = sd.make_next_file(prefix='{{file_prefix}}',digits={{file_digits}},ext='{{file_ext}}')
            print(f'file 초기화({sd.get_file()})')
    rtc:
        매개변수: 
            이름: rtc
            i2c_bus: i2c
        코드변환:
            from ds1307 import DS1307
            {{이름}} = ds1307.DS1307(i2c={{i2c_bus}})
    date_time_str_func:
        방법: rtc.datetime()으로 바꾸지 말 것
        코드변환:
            def data_time_str_func():
                year, month, day, hour, minute, second, week_day, sub_second = rtc.datetime
                date_time_str = f'{year:02d}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}'
                return date_time_str
    
    바이너리_센서:
        설명: '바이너리 센서를 작동한다'
        매개변수:
            pin_instance: 
            run_instance: run
            inverted: False
            callback_on:
            callback_off:
        코드변환: |
            from binarysensor import BinarySensor 
            {{이름}} = BinarySensor(pin_instance={{pin_instance}},inverted={{inverted}},callback_on={{callback_on}},callback_off={{callback_off}}) 
            {{run_instance}}.add({{이름}}.run)
    DHT22:
        매개변수:
            이름: dht
            pin_gpio: P.DHT
        코드변환: |
            from dht22sensor import DHT22Sensor
            {{이름}} = DHT22Sensor(pin_gpio={{pin_gpio}})
    BH1750: 
        매개변수:
            이름: bh1750
            i2c_bus: i2c
        from bh1750sensor import BH1750Sensor
        {{이름}} = BH1750Sensor({{i2c_bus}})
    LED:
        매개변수:
            이름: 
            pin_instance:  
            inverted: False             
        코드변환: |
            from blink import Blink
            {{이름}} = Blink(pin_instance={{pin_instance}},inverted={{inverted}})
            run.add({{이름}}.run)
    릴레이:
        매개변수:
            이름: 
            pin_instance:  
            inverted: False      
        코드변환: |            
            from blink import Blink
            {{이름}} = Blink(pin_instance={{pin_instance}},inverted={{inverted}})
            run.add({{이름}}.run)
    아날로그 센서:
        매개변수:
            이름: 
            pin_instance: 
        코드변환: |
            from machine import ADC
            {{이름}} = ADC({{pin_instance}})
            gas.atten(ADC.ATTN_11DB)
    버튼_PRESSED: 
        방법: {{callback}}은 문자열로 처리하지 말 것. 
        매개변수:
            이름: 
            pin_instance: 
            inverted: True
            callback:            
        코드변환: |            
            from button import Button
            {{이름}} = Button(pin_instance={{pin_instance}},inverted={{inverted}})
            {{이름}}.add(Button.PRESSED,callback={{callback}})
            run.add({{이름}}.run)
    부저:
        매개변수:
            이름: 
            pin_instance: 
            inverted: False
            callback:   
        코드변환: |
            from blink import Blink
            {{이름}} = Blink(pin_instance={{pin_instance}},inverted={{inverted}})
            run.add({{이름}}.run)
    타이머: 
        방법: {{callback}}은 문자열로 처리하지 말 것. 
        매개변수:
            이름:
            period: 
            callback:   
        코드변환: |
            from timerrun import TimerRun
            {{이름}} = TimerRun(period={{period}},callback={{callback}}) 
            run.add({{이름}}.run)
    OLED: 
        코드변환: |
            from ssd1306 import SSD1306_I2C  # OLED 라이브러리
            from hangul import draw_hangul, V2, H2, X4  # 한글 출력 모듈
            WIDTH = 64
            HEIGHT = 48
            oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
    set_on_off_str:
        매개변수:
            이름: 
            토픽: 
        코드변환:|
            if topic == f'cmnd/{C.DEVICE}/{{토픽}}':
                {{이름}}.set_on_off_str(msg)
                mqtt.publish(f'stat/{C.DEVICE}/{{토픽}}',{{이름}}.on_off()) 
    variable_int:
        방법: {{prefix}}가 없으면 ''로 처리할 것
        매개변수:
            prefix: 
            토픽: 
            변수:
        코드변환: |
            {{prefix}}if topic == f'cmnd/{C.DEVICE}/{{토픽}}':
                {{변수}}  = int(msg)
                print(f'new {{변수}}: {{{변수}}}')  
                mqtt.publish(f'stat/{C.DEVICE}/{{토픽}}',str({{변수}}))
    cmnd_TELEPERIOD:
        코드변환: |
            if topic == f'cmnd/{C.DEVICE}/TELEPERIOD':
            TELEPERIOD = int(msg)
            timer_sensor.set(period=TELEPERIOD * 1000)
            tele_msg = {'TELEPERIOD': msg}
            mqtt.publish(f'stat/{C.DEVICE}/TELEPERIOD', msg, retain=True)
            mqtt.publish(f'tele/{C.DEVICE}/INFO', tele_msg, retain=True)
            print(f'TELEPERIOD가 {msg}초로 변경되었습니다.')
    센서_읽기_앞부분: 
        코드변환: |
            import json
            from timerrun import TimerRun
            from run import Run
            from parse import Parse
            import pinno as P

            run = Run()
    센서_읽기_뒷부분: 
        코드변환: |
            def main():
                while True:
                    run.run()
            
            if __name__ == '__main__':
                main()
    프로그램_앞부분: 
        코드변환: |
            from machine import Pin,I2C,ADC,SPI
            from umqtt.simple import MQTTClient
            import json
            from timerrun import TimerRun
            from run import Run
            from usemqttclient import UseMQTTClient 
            from parse import Parse
            import pinno as P
            import config as C

            run = Run()
    프로그램_뒷부분: 
        코드변환: |
            def mqtt_on_connect():
                print('on_connect() called')
                msg = {'TELEPERIOD': TELEPERIOD}
                mqtt.publish(f'tele/{C.DEVICE}/INFO', msg, retain=True)
                on_connect_more()   

            def mqtt_callback(in_topic,in_msg):
                global TELEPERIOD
                topic = in_topic.decode()
                msg   = in_msg.decode()
                
                print(f'RCV> {topic}, |{msg}|')
                    
                if topic == f'cmnd/{C.DEVICE}/TELEPERIOD':
                    TELEPERIOD = int(msg)
                    timer_sensor.set(period=TELEPERIOD*1000)
                    tele_msg = {'TELEPERIOD': msg}
                    mqtt.publish(f'stat/{C.DEVICE}/TELEPERIOD', msg, retain=True)
                    mqtt.publish(f'tele/{C.DEVICE}/INFO', tele_msg, retain=True )
                    print(f'TELEPERIOD가 {msg}초로 변경되었습니다.')
                else:
                    callback_more(topic,msg)

            def send_data():
                data = read_sensors_more()
                mqtt.publish(f'tele/{C.DEVICE}/SENSOR',json.dumps(data))

            client = MQTTClient(C.MQTT_CLIENT_ID, C.MQTT_SERVER,port=C.MQTT_PORT,
                                user=C.MQTT_USER, password=C.MQTT_PASS,keepalive=60)
            mqtt = UseMQTTClient(client,C.DEVICE,C.SSID,C.SSID_PASS,mqtt_callback,mqtt_on_connect)
            run.add(mqtt.run)

            timer_sensor = TimerRun(period=TELEPERIOD*1000,callback=send_data)
            run.add(timer_sensor.run)

            def main():        
                
                while True:
                    run.run()
                    
            if __name__ == '__main__':
                main()

앞의 patterns:에서 정의된 내용을 참조하여 아래에 지정된 components:를 마이크로파이썬 코드변환로 만들어 주세요.
코드변환는 기계적으로 변환만 하고 새롭게 생성하지 마세요.
중복된 import는 생략하세요.
함수는 그 함수를 사용하는 코드변환보다 앞 쪽으로 옮기세요.
