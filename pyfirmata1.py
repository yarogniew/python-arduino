
try:
    from pyfirmata import Arduino, util
except ModuleNotFoundError:
    import pip
    pip.main(['install', 'pyfirmata'])
    from pyfirmata import Arduino, util
except Exception as e:
    print("Rodzaj błędu: {}" .format(e))
              
from time import sleep

i = 0

board = Arduino('/dev/cu.usbmodem1A13121')
while i < 5:
    board.digital[12].write(1)
    sleep(0.5)
    board.digital[12].write(0)
    sleep(0.15)
    i = i + 1
