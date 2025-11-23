###############################################################################
### MyGlobal
### Pilot_ZiRA-Master V1.01
###############################################################################

class Global_Module:
    
    inc_ws2812          = True
    inc_decoder         = False
    inc_serial          = False
    inc_gpio            = True
    inc_plc             = False
    inc_sound           = True

class Global_WS2812:

    numpix_1            = 200       # Anz. LEDs im 1. Stripe
    numpix_2            = 128       # Anz. LEDs im 2. Stripe
    numpix_3            = 32        # Anz. LEDs im 3. Stripe
    numpix_4            = 32        # Anz. LEDs im 4. Stripe
    numpix_5            = 32        # Anz. LEDs im 5. Stripe
    numpix_6            = 16        # Anz. LEDs im 6. Stripe
    numpix_7            = 16        # Anz. LEDs im 7. Stripe
    numpix_8            = 16        # Anz. LEDs im 6. Stripe
     
    #--------------------------------------------------------------------------

    seg_01_strip        = 0             #  1. Seg -> Stripe      # 0 -> Boden 1
    seg_01_start        = 0             #  1. Seg -> Start
    seg_01_count        = 200           #  1. Seg -> Anzahl

    seg_02_strip        = 1             #  2. Seg -> Stripe      # 1 -> Boden 2
    seg_02_start        = 0             #  2. Seg -> Start
    seg_02_count        = 128           #  2. Seg -> Anzahl

    seg_03_strip        = 2             #  3. Seg -> Stripe      # 2 -> Boden 3
    seg_03_start        = 0             #  3. Seg -> Start
    seg_03_count        = 32            #  3. Seg -> Anzahl

    seg_04_strip        = 3             #  4. Seg -> Stripe      # 3 -> Boden 4
    seg_04_start        = 0             #  4. Seg -> Start
    seg_04_count        = 32            #  4. Seg -> Anzahl

    seg_05_strip        = 4             #  5. Seg -> Stripe      # 4 -> Boden 5
    seg_05_start        = 0             #  5. Seg -> Start
    seg_05_count        = 32           #  5. Seg -> Anzahl
    
    seg_06_strip        = 5             #  6. Seg -> Stripe      # 5 -> Spiegel
    seg_06_start        = 0             #  6. Seg -> Start
    seg_06_count        = 16            #  6. Seg -> Anzahl
    
    seg_07_strip        = 6             #  7. Seg -> Stripe      # 6 -> Laser
    seg_07_start        = 0             #  7. Seg -> Start
    seg_07_count        = 16            #  7. Seg -> Anzahl

    seg_08_strip        = 7             #  8. Seg -> Stripe      # 7 -> Empfänger
    seg_08_start        = 0             #  8. Seg -> Start
    seg_08_count        = 16            #  8. Seg -> Anzahl
    
# -----------------------------------------------------------------------------

    color_def           = (  0,  0,  2)
    color_off           = (  0,  0,  0)
    color_on            = (255, 10, 10)
    color_dot           = (110,  2,  2)
    color_half          = (110,  2,  2)
    color_blink_on      = (255, 20, 20)
    color_blink_off     = (  0,  0,  5)
    color_red           = (120,  0,  0)
    color_green         = (  0,120,  0)


class Global_Default:

    blink_freq          = 3.0           # Blink Frequenz
    

def main():

    print("Start Global Init")
    mg = Global_WS2812
    print(mg.numpix_1)
    print(mg.seg_01_strip, mg.seg_01_start, mg.seg_01_count)
    print(mg.seg_02_strip, mg.seg_02_start, mg.seg_02_count)


#------------------------------------------------------------------------------
#--- Main
#------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
