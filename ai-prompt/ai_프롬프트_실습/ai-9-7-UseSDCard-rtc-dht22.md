( 여기에 'ai-patterns.md'의 내용을 넣으세요. )

components:
- 센서읽기_앞부분

- DHT22:
    이름: dht
    pin_gpio: P.DHT

- i2c:
    scl_pin: P.SCL
    sda_pin: P.SDA

- spi:
    sck_pin: P.SCK
    mosi_pin: P.MOSI
    miso_pin : P.MISO

- sdcard_mount_make_next_file:
    cs_pin: P.CS
    file_prefix: temphum
    file_digits: 3
    file_ext: json

- rtc

- date_time_str_func

def read_sensor():

    data = dht.read()
    p = Parse(data)
    
    print(f"{p.name}> 온도: {p.value[1]}°{p.temp_unit}, 습도: {p.value[0]}%")
    
    data['Time'] = date_time_str_func()
    
    ok, msg = sd.append_json(data)
    if not ok:
        print(f"SD 카드 기록 실패: {msg}")
    else:
        print(f"데이터 기록 완료: {data}")

components:
- 타이머:
    이름: timer_sensor
    period: 5*1000
    callback: read_sensor

- 센서읽기_뒷부분