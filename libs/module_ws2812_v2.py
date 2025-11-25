# Module WS2812 V1.01
import time # type: ignore
import libs.module_neopixel as module_neopixel
from libs.module_init import Global_WS2812 as MyGlobal


class LedState:
    def __init__(self):
        self.state = False
        self.blink_state = False

    def set(self, set):
        self.state = set

    def get(self):
        return self.state
    
    def do_blink(self):
        self.blink_state = not self.blink_state

    def get_blink(self):
        return self.blink_state

    def refresh(self):
        self.state = False
        for strips in strip_obj:
            strips.show()


class Ledsegment:

    def __init__(self, neopixel, start, count):
        self.neopixel = neopixel
        self.start = start
        self.stop = self.start + count - 1
        self.count = count
        self.position = 0
        self.run_state = False
        self.blink_state = False
        self.color_on           = (0,0,0)
        self.color_default      = (0,0,0)
        self.color_off          = (0,0,0)
        self.color_blink_on     = (0,0,0)
        self.color_blink_off    = (0,0,0)
        self.color_half         = (0,0,0)
        self.color_show         = (0,0,0)
        self.color_value        = (0,0,0)
        self.color_red          = (0,0,0)
        self.color_green        = (0,0,0)

    def set_color_on(self, color_on):
        self.color_on = color_on

    def set_color_def(self, color_default):
        self.color_default = color_default
        
    def set_color_off(self, color_off):
        self.color_off = color_off

    def set_color_value(self, color_value):
        self.color_value = color_value

    def set_color_show(self, color_value):
        self.color_show = color_value

    def set_color_blink_off(self, color_value):
        self.color_blink_off = color_value

    def set_color_blink_on(self, color_value):
        self.color_blink_on = color_value
    
    def set_color_half(self, color_value):
        self.color_half = color_value
    
    def set_color_red(self, color_value):
        self.color_red = color_value
    
    def set_color_green(self, color_value):
        self.color_green = color_value

    def set_pixel(self, pixel_num, color=None):
        if color:
            self.color_value = color
        else:
            self.color_value = self.color_show
        self.neopixel.set_pixel(self.start + pixel_num, self.color_value)

    def show_on(self):
        self.color_show = self.color_on
        self.blink_state = False
        self.set_line()

    def show_def(self):
        self.color_show = self.color_default
        self.blink_state = False
        self.set_line()

    def show_off(self):
        self.color_show = self.color_off
        self.blink_state = False
        self.set_line()

    def show_red(self):
        self.color_show = self.color_red
        self.blink_state = False
        self.set_line()

    def show_green(self):
        self.color_show = self.color_green
        self.blink_state = False
        self.set_line()

    def show_half(self):
        self.color_show = self.color_half
        self.blink_state = False
        self.set_line()

    def show_blink(self):
        self.blink_state = True
        if ledstate.get_blink():
            self.color_show = self.color_blink_on
        else:
            self.color_show = self.color_blink_off
        self.set_line()

    def get_blink_state(self):
        return self.blink_state

    def set_line(self):
        self.neopixel.set_pixel_line(self.start, self.stop, self.color_show)

    def show_stripe(self):
        self.neopixel.show()

    def set_stop(self, stop):
        self.stop = stop

def setup_ws2812():

    global strip_obj
    global led_obj
    global ledstate
    global mg
    
    mg = MyGlobal
    
    led_obj = []
    strip_obj = []

    ledstate = LedState()
    
    # WS2812 Pins -> Pin 2 - Pin 9

    strip_obj.append(module_neopixel.Neopixel(mg.numpix_1, 0, 2, "GRB"))
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_2, 1, 3, "GRB"))
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_3, 2, 4, "GRB"))
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_4, 3, 5, "GRB"))
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_5, 4, 6, "GRB"))
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_6, 5, 7, "GRB"))
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_7, 6, 8, "GRB"))
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_8, 7, 9, "GRB"))
    
    # =========================================================================

    led_obj.append(Ledsegment(strip_obj[mg.seg_01_strip], mg.seg_01_start, mg.seg_01_count))      #  ( 0) -> 1. LED-Stripe
    led_obj.append(Ledsegment(strip_obj[mg.seg_02_strip], mg.seg_02_start, mg.seg_02_count))      #  ( 1) -> 2. LED-Stripe
    led_obj.append(Ledsegment(strip_obj[mg.seg_03_strip], mg.seg_03_start, mg.seg_03_count))      #  ( 2) -> 3. LED-Stripe
    led_obj.append(Ledsegment(strip_obj[mg.seg_04_strip], mg.seg_04_start, mg.seg_04_count))      #  ( 3) -> 4. LED-Stripe
    led_obj.append(Ledsegment(strip_obj[mg.seg_05_strip], mg.seg_05_start, mg.seg_05_count))      #  ( 4) -> 5. LED-Stripe
    led_obj.append(Ledsegment(strip_obj[mg.seg_06_strip], mg.seg_06_start, mg.seg_06_count))      #  ( 5) -> 6. LED-Stripe
    led_obj.append(Ledsegment(strip_obj[mg.seg_07_strip], mg.seg_07_start, mg.seg_07_count))      #  ( 6) -> 7. LED-Stripe
    led_obj.append(Ledsegment(strip_obj[mg.seg_08_strip], mg.seg_08_start, mg.seg_08_count))      #  ( 7) -> 8. LED-Stripe
 
    # =========================================================================

    for strips in strip_obj:
        strips.brightness(255)
   
    # Alle Leds auf Vorgabewert -> aus
    for strips in strip_obj:
        strips.set_pixel_line(0, strips.num_leds - 1, mg.color_off)
    for strips in strip_obj:
        strips.show()

    # Setze Farbwerte in alle LED-Objekte
    for leds in led_obj:
        leds.set_color_off(mg.color_off)
        leds.set_color_def(mg.color_def)
        leds.set_color_on(mg.color_on)
        leds.set_color_value(mg.color_dot)
        leds.set_color_show(mg.color_dot)
        leds.set_color_blink_off(mg.color_blink_off)
        leds.set_color_blink_on(mg.color_blink_on)
        leds.set_color_half(mg.color_half)
        leds.set_color_red(mg.color_red)
        leds.set_color_green(mg.color_green)
    
    # Blinken aus
    do_all_no_blink()

def test_led(stripe, pos):
    do_all_off()
    strip_obj[stripe].set_pixel(pos, (70,70,70))
    ledstate.refresh()

def do_all_on():
    # Setze Farbwerte in alle LED-Objekte
    for leds in led_obj:
        leds.show_on()
    ledstate.refresh()

def do_all_off():
    # Setze Farbwerte in alle LED-Objekte
    for leds in led_obj:
        leds.show_off()
    ledstate.refresh()

def do_all_def():
    # Setze Farbwerte in alle LED-Objekte
    for leds in led_obj:
        leds.show_def()
    ledstate.refresh()

def do_all_no_blink():
    for leds in led_obj:
        leds.blink_state = False

def do_blink():
    ledstate.do_blink()
    for leds in led_obj:
        if leds.get_blink_state():
            leds.show_blink()
        else:
            pass
    
    ledstate.set(True)
    ledstate.refresh()

def do_test_on():
    #print("Test on")
    led_obj[0].show_on()
    led_obj[1].show_on()
    ledstate.set(True)
 
def do_test_off():
    #print("Test off")
    led_obj[0].show_off()
    led_obj[1].show_off()
    ledstate.set(True)

def do_refresh():

    ledstate.refresh()

def do_get_state():

    return ledstate.get()

def set_all_off():                          # Setze Farbwerte in alle LED-Objekte
    # Setze Farbwerte in alle LED-Objekte
    for leds in led_obj:
        leds.show_off()
    ledstate.refresh()

def set_all_def():                          # Setze Farbwerte in alle LED-Objekte
    for leds in led_obj:
        leds.show_def()
    ledstate.refresh()

def set_all_on():                           # Setze Farbwerte in alle LED-Objekte
    for leds in led_obj:
        leds.show_def()
    ledstate.refresh()

def self_test():                                # Pro Stripe einmal Aus-RGB(25%) -Aus 
    for strips in strip_obj:
        # Alle Aus
        strips.set_pixel_line(0, strips.num_leds - 1, (0,0,0))
        strips.show()
        time.sleep(0.1)
        # Alle Rot
        strips.set_pixel_line(0, strips.num_leds - 1, (50,0,0))
        strips.show()
        time.sleep(0.1)
        # Alle Grün
        strips.set_pixel_line(0, strips.num_leds - 1, (0,50,0))
        strips.show()
        time.sleep(0.1)
        # Alle Blau
        strips.set_pixel_line(0, strips.num_leds - 1, (0,0,50))
        strips.show()
        time.sleep(0.1)
        # Alle Aus
        strips.set_pixel_line(0, strips.num_leds - 1, (0,0,0))
        strips.show()
        time.sleep(0.1)


def do_blink_test():
    loops = 4
    looptime = 0.15
    #print(len(led_obj))
    for x in range(len(led_obj)):
        led_obj[x].show_blink()
        for i in range(loops):
            do_blink()
            time.sleep(looptime)
        led_obj[x].show_off()
        do_refresh()
    

def do_obj_on_off_def_off():
    
    delay_time = 0.3
    for x in range(len(led_obj)):
        led_obj[x].show_on()
        do_refresh()
        time.sleep(delay_time)
        led_obj[x].show_off()
        do_refresh()
        time.sleep(delay_time)
        led_obj[x].show_def()
        do_refresh()
        time.sleep(delay_time)
        led_obj[x].show_off()
        do_refresh()

def do_dot_test():
    delay_time = 0.2
    color_now = (0,10,60)
    for y in range(len(led_obj)):
        for x in range(led_obj[y].count):
            if x > 0:
                led_obj[y].set_pixel(x - 1, (0,0,0))
            led_obj[y].set_pixel(x, color_now)
            do_refresh()
            time.sleep(delay_time)
        led_obj[y].show_off()
        do_refresh()
        time.sleep(delay_time)
        
def set_led_obj(obj,state):
    if state == "off":
        led_obj[obj].show_off()
    if state == "def":
        led_obj[obj].show_def()
    if state == "on":
        led_obj[obj].show_on()
    if state == "half":
        led_obj[obj].show_half()
    if state == "blink":
        led_obj[obj].show_blink()
    if state == "red":
        led_obj[obj].show_red()
    if state == "green":
        led_obj[obj].show_green()
    if state == "green_half":
        led_obj[obj].set_stop(10)
        led_obj[obj].show_green()
    do_refresh()

# -----------------------------------------------------------------------------

def main():
    
    print("WS2812 -> Start of Program !!!")

    print("WS2812 -> Setup")
    setup_ws2812()
        
    print("WS2812 -> Run self test")
    self_test()
    
    set_led_obj(2,"green_half")
        
    

    print("WS2812 -> End of Program !!!")

# End

#------------------------------------------------------------------------------
#--- Main
#------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
