(여기에 'ai-9-1-센서-클래스-템플릿.md'의 내용을 붙여 넣으세요)

components:
- sensor_calss:
    센서_모델: DS18B20
    클래스_이름: DS18B20Sensor
    pin_type: pin_gpio
    key_1: Temperature, 소숫점 1자리
    라이브러리: |
        특이사항 없음.

def main():
    import pinno as P
    from parse import Parse

    sensor = DS18B20Sensor(pin_gpio=P.DS18B20)  # DS18B20 센서를 특정 GPIO에 연결함.    
    while True:
        data = sensor.read()
        print(data)

        p = Parse(data)
    
        for i in range(len(p.names)):
            print(f'name: {p.names[i]}, Id: {p.ow_ids[i]}, {p.ow_keys[i]}: {p.ow_values[i]}')

        time.sleep_ms(5000)

if __name__ == '__main__':
    main()