(여기에 'ai-9-1-센서-클래스-템플릿.md'의 내용을 붙여 넣으세요)

components:
- sensor_calss:
    센서_모델: BH1750
    클래스_이름: BH1750Sensor
    pin_type: i2c_bus
    key_1: Brightness, 정수
    라이브러리: |
        import bh1750fvi 하지 말고 직접 코드 만들어 줘.

def main(): 
    import pinno as P 
    from parse import Parse

    i2c = I2C(0, scl=Pin(P.SCL), sda=Pin(P.SDA))
    sensor = BH1750Sensor(i2c_bus=i2c)
    while True:        
        data = sensor.read()
        print(data)
        p = Parse(data) 
        print(f'name: {p.name}, {p.key}: {p.value}')   

        time.sleep_ms(5000)

if __name__ == '__main__':
    main()  