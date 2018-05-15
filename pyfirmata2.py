try:
    from pyfirmata import Arduino, util
except ModuleNotFoundError:
    import pip

    pip.main(['install', 'pyfirmata'])
    from pyfirmata import Arduino, util
except Exception as e:
    print("Rodzaj błędu: {}".format(e))

from time import sleep

wynik = 0
board = Arduino('/dev/cu.usbmodem1A13121')
# pin = 12

def ledin(pin):

    board.digital[pin].write(1)
    sleep(1)
    board.digital[pin].write(0)
    sleep(0.15)


# iterator = util.Iterator(board)
# iterator.start()

# pin0 = board.get_pin('a:0:i')
# sleep(1.0)
# print(pin0.read()*1000.0)

while True:
    try:
        it = util.Iterator(board)
        it.start()
        board.analog[0].enable_reporting()
        sleep(0.5)
        wynik = int(board.analog[0].read() * 10000)
        print(wynik)
        if wynik < 100 or wynik > 9900:
            ledin(12)

    except KeyboardInterrupt:
        exit()
        break