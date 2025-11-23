# #############################################################################
# ### Modul XIO
# ### V0.99
# #############################################################################

from machine import Pin, PWM        # type: ignore
#from utime import sleep             # type: ignore


class XIO:

    def __init__(self, dir):
        self.dir = dir
        self.io_0 = False
        self.io_1 = False
        self.io_2 = False
        self.io_3 = False
        self.pin_n = []
        if dir:
            self.set_xio_out()
        else:
            self.set_xio_in()

    def set_xio_out(self):
        self.pin_n.append(Pin(10, mode=Pin.OUT))
        self.pin_n.append(Pin(11, mode=Pin.OUT))
        self.pin_n.append(Pin(12, mode=Pin.OUT))
        self.pin_n.append(Pin(13, mode=Pin.OUT))

    def set_xio_in(self):
        self.pin_n[0] = Pin(10, mode=Pin.IN, pull=Pin.PULL_UP)
        self.pin_n[1] = Pin(11, mode=Pin.IN, pull=Pin.PULL_UP)
        self.pin_n[2] = Pin(12, mode=Pin.IN, pull=Pin.PULL_UP)
        self.pin_n[3] = Pin(13, mode=Pin.IN, pull=Pin.PULL_UP)
    
    def set_out(self):
        self.pin_n[0].value(1)
        self.pin_n[1].value(0)
    
# -----------------------------------------------------------------------------
def main():

    print("=== Start Main -> Module_XIO ===")

    try:
        print("Start")

        xio = XIO(1)

        xio.set_out()

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
