# #############################################################################
# ### GPIO
# ### V 1.00
# #############################################################################
from machine import Pin, I2C # type: ignore
import libs.mcp23017_raw as mcp23017
from time import sleep # type: ignore


class GPIO:

    def __init__(self):
        self.i2c = I2C(0, scl=Pin(21), sda=Pin(20))
        self.mcp = mcp23017.MCP23017(self.i2c, 0x20)
        self.inputs = 0x00
        self.outputs = 0x00

    def get_input_byte(self):
        self.inputs = int.from_bytes(self.mcp._read(0x13, 1), 'big')
        return self.inputs

    def get_input_bit(self, bit):
        self.inputs = int.from_bytes(self.mcp._read(0x13, 1), 'big')
        return self.inputs & ( 1 << bit)
    
    def get_value_bit(self, bit):
        return self.inputs & ( 1 << bit)

    def set_output_byte(self, value=None):
        if not value == None:
            self.outputs = value
        self.mcp._write([0x12, self.outputs])
        return self.outputs
    
    def set_output_bit(self, bit, value):
        if value == "On":
            self.outputs = self.outputs | ( 1 << bit)
        else:
            self.outputs = self.outputs & ~( 1 << bit)
        self.mcp._write([0x12, self.outputs])
        return self.outputs




# -----------------------------------------------------------------------------
def main():

    print("=== Start Main -> Module_Sound ===")

    try:
        print("Start")

        gpio = GPIO()

        while(True):

            gpio.get_input_byte()
            if gpio.get_value_bit(0):
                gpio.set_output_bit(0, "On")
            if gpio.get_value_bit(1):
                gpio.set_output_bit(1, "On")
            if gpio.get_value_bit(2):
                gpio.set_output_bit(0, "Off")
            if gpio.get_value_bit(3):
                gpio.set_output_bit(1, "Off")
            sleep(0.2)
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
