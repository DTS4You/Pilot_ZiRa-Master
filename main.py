######################################################
### Projekt: Pilot-ZiRa-Master                     ###
### Version: 1.01                                  ###
### Datum  : 25.11.2025                            ###
######################################################
#from machine import Pin, Timer       # type: ignore
from libs.module_init import Global_Module as MyModule
from time import sleep                # type: ignore


TASTER_VORNE    = 0b00000010
TASTER_HINTEN   = 0b00001000
KONTAKT_RED     = 0b00100000
KONTAKT_GREEN   = 0b00010000
OUT_TASTER_VORNE_GREEN  = 0
OUT_TASTER_VORNE_RED    = 1
OUT_WINRAD              = 6
OUT_MAGNET              = 7

def set_led_to_color(color):
    for i in range(5):
        MyWS2812.set_led_obj(i, color)

# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------

def main():

    print("=== Start Main ===")

    state_value     = 0

    try:
        print("Start Main Loop")
 
        set_led_to_color("def")

        gpio = MyGPIO.GPIO()

        xio = MyXIO.XIO("OUTPUT")

        sound = MySound.PWM_SOUND(0,1)

        sound.play_off()
        
        while (True):

            value_io = gpio.get_input_byte()
            
            if state_value < 3:
                if value_io & TASTER_HINTEN:
                    if value_io & KONTAKT_GREEN:
                        print("Green")
                        xio.write_io(0x01)
                        gpio.set_output_bit(OUT_WINRAD, "On")
                        set_led_to_color("green")
                        MyWS2812.set_led_obj(4, "def")
                        gpio.set_output_bit(OUT_TASTER_VORNE_GREEN, "On")
                        gpio.set_output_bit(OUT_TASTER_VORNE_RED, "Off")
                        state_value = 1
                    elif value_io & KONTAKT_RED:
                        print("Red")
                        xio.write_io(0x02)
                        gpio.set_output_bit(OUT_WINRAD, "Off")
                        set_led_to_color("red")
                        MyWS2812.set_led_obj(3, "def")
                        gpio.set_output_bit(OUT_TASTER_VORNE_GREEN, "Off")
                        gpio.set_output_bit(OUT_TASTER_VORNE_RED, "On")
                        state_value = 2
                    else:
                        print("Default")
                        xio.write_io(0x00)
                        gpio.set_output_bit(OUT_WINRAD, "Off")
                        set_led_to_color("def")
                        gpio.set_output_bit(OUT_TASTER_VORNE_GREEN, "Off")
                        gpio.set_output_bit(OUT_TASTER_VORNE_RED, "Off")
                        state_value = 0

            if state_value == 1:
                if value_io & TASTER_VORNE:
                    sound.play_sound("green")
                    gpio.set_output_bit(OUT_MAGNET, "On")
                    gpio.set_output_bit(OUT_WINRAD, "Off")
                    state_value = 3
                    sleep(2)
                    gpio.set_output_bit(OUT_MAGNET, "Off")
                    set_led_to_color("def")
                    

            if state_value == 2:
                if value_io & TASTER_VORNE:
                    sound.play_sound("red")
                    gpio.set_output_bit(OUT_WINRAD, "Off")
                    state_value = 3
                    sleep(2)
                    set_led_to_color("def")
        
            if state_value == 3:
                #if value_io & TASTER_HINTEN:
                if True:
                    gpio.set_output_bit(OUT_WINRAD, "Off")
                    gpio.set_output_bit(OUT_MAGNET, "Off")
                    set_led_to_color("def")
                    gpio.set_output_bit(OUT_TASTER_VORNE_GREEN, "Off")
                    gpio.set_output_bit(OUT_TASTER_VORNE_RED, "Off")
                    sleep(1)
                    state_value = 0
            
            sleep(0.2)

    except KeyboardInterrupt:
        print("Keyboard Interrupt")
    finally:
        print("Exiting the program")   

    print("=== End of Main ===")

# ==============================================================================
# ==============================================================================
    
# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################

if __name__ == "__main__":
    
    if MyModule.inc_gpio:
        print("I2C_GPIO -> Load-Module")
        import libs.module_gpio as MyGPIO
    else:
        print("I2C_GPIO -> nicht vorhanden")

    if MyModule.inc_ws2812:
        print("WS2812 -> Load-Module")
        import libs.module_ws2812_v2 as MyWS2812         # Modul WS2812  -> WS2812-Ansteuerung
        #print("WS2812 -> Setup")
        MyWS2812.setup_ws2812()
        ### Test ###
        print("WS2812 -> Run self test")
        MyWS2812.self_test()
    else:
        print("WS2812 -> nicht vorhanden")

    if MyModule.inc_sound:
        print("Sound -> Load-Module")
        import libs.module_sound as MySound
    else:
        print("Sound -> nicht vorhanden")

    if MyModule.inc_xio:
        print("XIO -> Load-Module")
        import libs.module_xio as MyXIO
    else:
        print("XIO -> nicht vorhanden")


    main()      # Start Main $$$

# Normal sollte das Programm hier nie ankommen !
print("___ End of Programm ___")
print("§§§> !!! STOP !!! <§§§")

# ##############################################################################
