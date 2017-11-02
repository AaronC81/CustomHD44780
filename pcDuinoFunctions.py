def write_pin(pinNumber, output):
    with open("/sys/devices/virtual/misc/gpio/pin/gpio" + str(pinNumber), 'w') as f:
        f.write(str(output))

def pin_mode(pinNumber, mode):
    with open('/sys/devices/virtual/misc/gpio/mode/gpio' + str(pinNumber), 'w') as f:
        f.write(str(mode))