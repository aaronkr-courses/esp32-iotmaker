patterns: 
    LED:
        설명: LED인스턴스를 만듦.
        방법: {{inverted}}가 없으면 False로 지정함.  
        코드: |
            from blink import Blink
            {{이름}} = Blink(pin_instance={{pin_instance}},inverted={{inverted}})
            run.add({{이름}}.run)
    타이머: 
        코드: |
            from timerrun import TimerRun
            {{이름}} = TimerRun(period={{period}},callback={{callback}}) 
            run.add({{이름}}.run)
    앞_부분:
        코드: |
            from machine import Pin
            from run import Run
            import pinno as P

            run = Run()
    뒷_부분:
        코드: |
            def main():
                while True:
                    run.run()

            if __name__ == '__main__':
                main()
