roll_value = 0

def on_gesture_shake():
    global roll_value
    roll_value = randint(1, 6)
    if roll_value == 1:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
    elif roll_value == 2:
        basic.show_leds("""
            . . . # .
                        . . # . .
                        . . . . .
                        . . # . .
                        . . . . .
        """)
    elif roll_value == 3:
        basic.show_leds("""
            . . # . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . # . .
        """)
    elif roll_value == 4:
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        . # . # .
                        . . . . .
        """)
    elif roll_value == 5:
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . # . .
                        . # . # .
                        . . . . .
        """)
    elif roll_value == 6:
        basic.show_leds("""
            . # . # .
                        . . . . .
                        . # . # .
                        . . . . .
                        . # . # .
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
