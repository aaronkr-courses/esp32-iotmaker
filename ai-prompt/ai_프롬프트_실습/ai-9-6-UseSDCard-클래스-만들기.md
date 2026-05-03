patterns:
    UseSDcard_class:
        설명: UseSDcard 클래스 템플릿
        방법: |
            Docstring은 :param pin_gpio: 형식으로 하고, 설명은 한글로 함.
        코드:
            from machine import Pin ..
            import time
            import sdcard

            # file: usesdcard.py
            class UseSDcard:  
                __init__(self, spi_bus,cs_gpio,mount='sd') -> None:
                    # spi_bus는 인스턴스로 전달되므로 별도로 만들 필요 없음
                    self.spi_bus = spi_bue 

                    # Pin(cs_gpio)를 만들어서 나중에 SDCard 지정할 때 사용
                    self.cs_gpio = cs_gpio
                    
                    # mount point를 말함
                    self.mount_point = '/' + mount
                    self.sensor_instance = ... 

                    self._file  

                def mount_sdcard() -> bool, message_str:
                    sd = SDcard 인스턴스
                    # vfs 빠뜨리지 말것 
                    vfs = ...
                    ...
                    
                    성공하면
                    return True,'OK!'
                    실패하면
                    return False,오류 메시지

                def make_next_file(prefix: str, digits:int, ext: str) -> bool, message_str:

                    표준 파일 형식은 '{prefix}{ser자릿수 숫자}.{ext}'임
                    prefix와 digits사이에 구분 문자 없음.
                    구분 문자가 필요하면 prefix에 포함해야 함.

                    digits이 3이면 xxx이고 4이면 xxxx 등으로 바뀌므로 조심해야 함.
                    ser이 제일 큰수가 되면 다시 1로 회기함. 


                    기존 파일 읽어서 ser을 확인하고 ser+1 해서 next_ser을 만듬.
                    zfill()메서드 사용하지 말 것.
                    file_name = f'{prefix}{next_ser:0{digits}}.{ext}' 
                    self._file 에 만든 파일 저장

                    새로 만든 파일에 빈 정보 넣어서 초기화함    
                    성공하면
                    return True,'OK!'
                    실패하면
                    return False,오류 메시지

                def get_file() -> str:
                    return self._file

                def append_json(data_dictionary) -> bool, message_str:
                    data_dictionary를 json str로 만들고 뒤에 '\n'을 붙임.
                    {get_file()}에 append함

                    성공하면
                    return True,'OK!'
                    실패하면
                    return False,오류 메시지
                
                def append_str(data_str) -> bool, message_str:
                    data_str을 {get_file()}에 append함

                    성공하면
                    return True,'OK!'
                    실패하면
                    return False,오류 메시지

                def read() -> str:
                    파일을 읽어서 str로 돌려줌.
                    return 읽은 str 전체
       
앞의 patterns:에서 정의된 내용을 참조하여 아래에 지정된 components:를 마이크로파이썬 코드로 만들어 주세요.

components:
- UseSDcard_class

def main():
    from machine import Pin, SPI
    import time
    import pinno as P

    # 핀 번호 설정
    SCK_PIN = P.SCK
    MISO_PIN = P.MISO
    MOSI_PIN = P.MOSI
    CS_PIN = P.CS

    # SPI 버스 초기화
    spi_bus = SPI(1, baudrate=1000000, sck=Pin(SCK_PIN), mosi=Pin(MOSI_PIN), miso=Pin(MISO_PIN))

    # UseSDCard 클래스 인스턴스 생성
    sd = UseSDCard(spi_bus, CS_PIN)

    # SD카드 마운트
    ok, message = sd.mount_sdcard()
    print(ok, message)

    # 새로운 파일 생성
    ok, message = sd.make_next_file(prefix='temphum', digits=3, ext='json')
    print(ok, message, sd.get_file())

    # 노랫말 생성
    song = [{'text': f'노랫말 {i}'} for i in range(5)]

    # SD카드에 노랫말 추가
    for s in song:
        ok, message = sd.append_json(s)
        print(ok, message)

    # 파일 내용 읽기
    file_data = sd.read()
    print(file_data)


if __name__ == '__main__':
    main()