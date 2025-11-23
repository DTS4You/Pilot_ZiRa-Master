# #############################################################################
# ### Modul XIO
# ### V0.99
# #############################################################################

from machine import Pin, PWM        # type: ignore
from utime import sleep             # type: ignore


class XIO:

    def __init__(self, dir):
        self.dir = dir
        self.value = 0x00
        self.io = [False, False, False, False]
        self.pin = []
        if dir:
            self.set_xio_out()
        else:
            self.set_xio_in()

    def set_xio_out(self):
        self.pin.append(Pin(10, mode=Pin.OUT))
        self.pin.append(Pin(11, mode=Pin.OUT))
        self.pin.append(Pin(12, mode=Pin.OUT))
        self.pin.append(Pin(13, mode=Pin.OUT))

    def set_xio_in(self):
        self.pin.append(Pin(10, mode=Pin.IN, pull=Pin.PULL_UP))
        self.pin.append(Pin(11, mode=Pin.IN, pull=Pin.PULL_UP))
        self.pin.append(Pin(12, mode=Pin.IN, pull=Pin.PULL_UP))
        self.pin.append(Pin(13, mode=Pin.IN, pull=Pin.PULL_UP))

    def read_input(self):
        for i in range(4):
            self.io[i] = self.pin[i].value()

    def write_output(self):
        for i in range(4):
            self.pin[i].value(self.io[i])
    
    def set_bit(self, bit, value=True):
        self.io[bit] = value
        return self.io[bit]
    
    def get_bit(self, bit):
        return self.io[bit]
    
    def set_byte(self, value):
        self.value = value
        for i in range(4):
            if (self.value & 1 << i ):
                self.io[i] = True
            else:
                self.io[i] = False

    def read_byte(self):
        self.value = 0x00
        for i in range(4):
            if self.io[i] == True:
                self.value = self.value | 1 << i
        return self.value
    
# -----------------------------------------------------------------------------
def main():

    print("=== Start Main -> Module_XIO ===")

    try:
        print("Start")

        print("Create Object")
        xio = XIO(1)

        xio.write_output()

        sleep(1)
        
        xio.set_bit(0, True)
        xio.set_bit(1, False)
        xio.set_bit(2, True)
        xio.set_bit(3, False)

        xio.write_output()

        sleep(1)

        xio.set_byte(0xAA)
        xio.write_output()
        print(hex(xio.read_byte()))

        sleep(1)

        xio.set_byte(0x55)
        xio.write_output()
        print(hex(xio.read_byte()))

        print("Delete Object")
        del xio
      

    except KeyboardInterrupt:
        print("Keyboard Interrupt")
    finally:
        print("Exiting the program")
    print("=== End Main ===")

# ------------------------------------------------------------------------------
# --- Main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

# =============================================================================
