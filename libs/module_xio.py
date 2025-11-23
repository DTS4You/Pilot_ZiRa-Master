# #############################################################################
# ### Modul XIO
# ### V0.99
# #############################################################################

from machine import Pin, PWM        # type: ignore
from utime import sleep             # type: ignore


class XIO:

    def __init__(self, dir):
        self.dir = dir
        self.io = []
        self.io.append(False)
        self.io.append(False)
        self.io.append(False)
        self.io.append(False)
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
        pass

    def write_output(self):
        for i in range(4):
            self.pin[i].value(self.io[i])
    
    def set_bit(self, bit, value=True):
        self.io[bit] = value
        return self.io[bit]
    
    def get_bit(self, bit):
        return self.io[bit]
    
# -----------------------------------------------------------------------------
def main():

    print("=== Start Main -> Module_XIO ===")

    try:
        print("Start")

        xio = XIO(1)

        xio.write_output()

        sleep(1)
        
        xio.set_bit(0, True)
        xio.set_bit(1, False)
        xio.set_bit(2, True)
        xio.set_bit(3, False)

        xio.write_output()

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
