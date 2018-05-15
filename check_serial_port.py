import serial.tools.list_ports

# http://pyserial.readthedocs.io/en/latest/tools.html

i = 0
faults = 0

def is_int(s):
    # funkcja sprawdzająca czy s jest int
    try:
        int(s)
        return True
    except ValueError:
        return False

ports = list(serial.tools.list_ports.comports())

print()
for p in ports:
    i += 1
    print(f"{i}: {p.device}")

while True:
    if faults > 3:
        print("\nWidzę, że jesteś kompletnym kretynem! Kończymy.")
        break
    print("\n Wpisz numer portu: ")
    x = input()

    if is_int(x):
        number_of_port = int(x)-1

        if number_of_port < i and number_of_port >= 0:
            name_of_port = ports[number_of_port].device
            print(f"O.K. Wybrałeś port o nazwie: {name_of_port}")
            break
        else:
            print("Nie ma takiego numeru portu baranie!")
            faults += 1
    else:
        print("To co wpisałeś nie jest liczbą!")
        faults += 1