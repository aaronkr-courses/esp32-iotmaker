## AI 프롬프트 실습 9-2: DHT22Sensor 클래스 만들기
## 프롬프트 
file: ai-9-2-DHT22Sensor-클래스-만들기.md
```
(여기에 'ai-9-1-센서-클래스-템플릿.md'의 내용을 붙여 넣으세요)

components:
- sensor_class:
    센서_모델: DHT22
    클래스_이름: DHT22Sensor
    pin_type: pin_gpio 
    key_1: Temperature, 소수점 1자리
    key_2: Humidity, 정수
    temp_unit: C
    라이브러리: |
        import dht 

def main():
    import pinno as P 
    from parse import Parse
    
    sensor = DHT22Sensor(P.DHT)
    while True:
        data = sensor.read()
        print(data)
        p = Parse(data) 
        print(f'name: {p.name}, {p.keys[1]}: {p.values[1]}, {p.keys[0]}: {p.values[0]}, TempUint: {p.temp_unit}')   

        time.sleep_ms(5000)

if __name__ == '__main__':
    main()
```
## AI가 만든 코드
프로그램: \lib\dht22sensor.py
```python
from machine import Pin
import time
import dht

class DHT22Sensor:
    """
    :param pin_gpio: GPIO 핀 번호를 받아서 DHT22 센서를 초기화
    :param ser: 센서의 고유 식별자 (시리얼 번호 등)
    """
    def __init__(self, pin_gpio, ser=None):
        # DHT22 모델 설정
        self._model = "DHT22"
        self._model_ser = f"{self._model}_{ser}" if ser else self._model
        self.pin_gpio = pin_gpio
        self.temp_unit = "C"
        self.sensor_instance = dht.DHT22(Pin(pin_gpio))
        self._key = ["Temperature", "Humidity"]
        self._value = [None, None]

    def read(self):
        try:
            # 센서 값 읽기
            self.sensor_instance.measure()
            temp = round(self.sensor_instance.temperature(), 1)  # 소수점 1자리로 설정
            hum = int(self.sensor_instance.humidity())           # 정수로 설정
            self._value = [temp, hum]
            return {
                "TempUnit": self.temp_unit,
                self._model_ser: {
                    self._key[0]: self._value[0],
                    self._key[1]: self._value[1]
                }
            }
        except Exception as e:
            print("Error reading from DHT22:", e)
            return None

def main():
    import pinno as P
    from parse import Parse

    sensor = DHT22Sensor(P.DHT, ser="001")  # 예시로 "001"을 ser에 입력
    while True:        
        data = sensor.read()
        print(data)
        p = Parse(data)
        print(f'name: {p.name}, {p.keys[0]}: {p.values[0]}, {p.keys[1]}: {p.values[1]}, TempUnit: {p.temp_unit}')

        time.sleep_ms(5000)

if __name__ == '__main__':
    main()
```
