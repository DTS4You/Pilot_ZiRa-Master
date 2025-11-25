# Pilot_ZiRa-Master
Pilot ZiRa 1. System
-------------------------------------------------------------------------------
--- Hardware:
-------------------------------------------------------------------------------
------LED-Belegung:
J401 -> Pin 2	-> 161 -> Gitter-Rahmen Horizontal 2 x parallel
J402 -> Pin 3   ->  84 -> Gitter-Rahmen Vertikal   6 x parallel
J403 -> Pin 4   ->  32 -> CO2-Anzeige
J404 -> Pin 5   ->  28 -> Energie Windrad    -> Richtung drehen
J405 -> Pin 6   ->  30 -> Energie Kohle      -> Richtung drehen
J406 -> Pin 7   -> ---frei---
J407 -> Pin 8   -> ---frei---
J408 -> Pin 9	-> ---frei---
-------------------------------------------------------------------------------
------ IO-Belegung:
J301 -> I 0.0	-> Taster vorne 			-> Öffner               -> Pull-Down, aktiv low
J302 -> I 0.1	-> Taster vorne 			-> Schliesser           -> Pull-Down, aktiv high
J303 -> I 0.2	-> Taster hinten			-> Öffner               -> Pull-Down, aktiv low
J304 -> I 0.3	-> Taster hinten			-> Schliesser           -> Pull-Down, aktiv high
J305 -> I 0.4	-> Reed-Kontakt				-> Position Grün        -> Pull-Down, aktiv high
J306 -> I 0.5	-> Reed-Kontakt				-> Position Rot         -> Pull-Down, aktiv high
J307 -> I 0.6
J308 -> I 0.7
#------------------------------------------------------------------------------
J301 -> Q 0.0	-> Taster LED vorne			-> Grüne LED
J302 -> Q 0.1	-> Taster LED vorne			-> Rote LED
J303 -> Q 0.2	-> Taster LED hinten		-> Grüne LED
J304 -> Q 0.3	-> Taster LED vorne			-> Rote LED
J305 -> Q 0.4   -> LED-Kerzen 1,3,5
J306 -> Q 0.5   -> LED-Kerzen 2,4,6
J307 -> Q 0.6   -> Windräder                -> StepDown 0,8V
J308 -> Q 0.7	-> Elektromagnet Ausgabe	-> High -> Stromlos Türe öffnet -> über Relaismodul Öffner
#------------------------------------------------------------------------------
J201 -> Pin 0   -> Audio-Ausgang über PWM
J201 -> Pin 1   -> Audio-Ausgang über PWM
#------------------------------------------------------------------------------
Taster-Belegung:
Schliesser  -> Grün - Grün
Öffner      -> Blau - Blau
LED rot     -> Rot - Schwarz
LED grün    -> Rot - Schwarz
-------------------------------------------------------------------------------
--- XIO-Belegung:
XIO -> 0	-> Pin(10) -> Input -> Status Bit 0
XIO -> 1    -> Pin(11) -> Input -> Status Bit 1
XIO -> 2    -> Pin(12) -> Input -> Status Bit 2
XIO -> 3    -> Pin(13) -> Input -> Status Bit 3
-------------------------------------------------------------------------------
--- Status:
0 -> Keine Anzeige
1 -> Animation  -> Grün
2 -> Animation  -> Rot
-------------------------------------------------------------------------------
LED-Zuordnung Master
01 -> 161 -> Gitter-Rahmen Horizontal 2 x parallel
02 ->  84 -> Gitter-Rahmen Vertikal   6 x parallel
03 ->  32 -> CO2-Anzeige
04 ->  28 -> Energie Windrad    -> Richtung drehen
05 ->  30 -> Energie Kohle      -> Richtung drehen

LED-Zuordnung Slave
Grün
01 ->  26 -> Nutzwärme Austritt
02 ->  54 -> Nutzwärem Eintritt
03 ->  48 -> Kondensator
04 ->  42 -> Abwärme Austritt
05 ->  48 -> Drossel           -> Richtung anpassen
06 ->  64 -> Verdampfer
07 ->  52 -> Abwärme Eintritt  -> Richtung anpassen
08 -> 109 -> Kompressor 1 und Kompressor 2
08 -> 41 - 56  -> Kompressor 1 
08 -> 91 - 106 -> Kompressor 2

Rot
02 ->  26 -> Dampf
03 ->  48 -> Auspuff
#------------------------------------------------------------------------------
--- Beschreibung:
State:
    0   ## Nach dem Einschalten
        -> Nach Reset oder Neustart
        --> Alle Merker auf aus
        --> Alle LED-Stripes aus
        --> Alles Taster-LEDs aus
        --> Relais aus
        --> Audio-Ausgang aus
        --> Starte Timer -> 3 Sekunden

    1   ## Tor schliessen, Befüllen und Freigabe
        -> Timer abgelaufen oder Einsprung auf 1 
        --> Alle LED-Stripes auf Blau 5%
        --> Relais an -> Tor kann geschlossen werden
        --> Taster-LED vorne aus
        --> Taster-LED hinten gelb blinken

    2   ## Warte auf Modul (Rot/Grün)
        -> Taster hinten betätigt
            -> Taster hinten gelb 
            -> Wenn I0.4 und nicht I0.5
                -> Merker 1 an     -> Modul Grün
            -> Wenn I0.5 und nicht I0.4
                -> Merker 1 aus    -> Modul Rot

    3   ## Warte auf Taster vorne
        -> I0.4 oder I0.5 an
            -> Wenn Merker 1 an    -> Modul Grün  
                -> Taster vorne LED grün blinken
                -> Wert für Ablauf Sequenz auf "30 Sekunden" setzen
            -> Wenn Merker 1 aus   -> Modul Rot
                -> Taster vorne LED rot  blinken
                -> Wert für Ablauf Sequenz auf "20 Sekunden" setzen

    4   ## Warte auf Sequenz-Ende
        -> Taster vorne betätigt
            -> Wenn Merker 1 an     -> Modul Grün
                -> Animation "Grün" Start
            -> Wenn Merker 1 aus    -> Modul Rot
                -> Animation "Rot" Start

    5   ## Co2 Anzeige
        -> Timer Sequenz Ende abgelaufen
            -> Wenn Merker 1 an     -> Modul Grün
                -> Animation "Grün" Stop
                -> Rahmen grün blinken
                -> Co2 Anzeige grün
            -> Wenn Merker 1 aus    -> Modul Rot
                -> Animation "Rot" Stop
                -> Rahmen rot blinken
                -> Co2 Anzeige rot
            -> Timer 2 Sekunden starten

    6   ## Tonausgane ; Tor auf / zu

    7   ## Alles auf Start
    