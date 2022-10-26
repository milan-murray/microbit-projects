def temp_down_animation():
    basic.show_leds("""
        . . # . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . # . # .
                . . # . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                # . . . #
                . # . # .
                . . # . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                # . . . #
                . # . # .
                . . # . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                # . . . #
                . # . # .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                # . . . #
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)


def temp_up_animation():
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . # . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . # . .
                . # . # .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . # . # .
                # . . . #
    """)
    basic.show_leds("""
        . . . . .
                . . # . .
                . # . # .
                # . . . #
                . . . . .
    """)
    basic.show_leds("""
        . . # . .
                . # . # .
                # . . . #
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . # . # .
                # . . . #
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        # . . . #
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)


new_temp = 0
music.set_volume(69)
music.start_melody(music.built_in_melody(
    Melodies.POWER_UP), MelodyOptions.ONCE)
old_temp = input.temperature()
basic.show_leds("""
    . . . . .
        . # # # .
        . . # . .
        . . # . .
        . . . . .
""")
lowest_temp = old_temp
highest_temp = old_temp


def on_forever():
    global new_temp, highest_temp, lowest_temp, old_temp
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(15000)
    basic.show_leds("""
        . . . . .
                . # # # .
                . . # . .
                . . # . .
                . . . . .
    """)
    basic.pause(5000)
    new_temp = input.temperature()
    if new_temp > highest_temp:
        highest_temp = new_temp
        music.start_melody(music.built_in_melody(
            Melodies.BA_DING), MelodyOptions.ONCE)
    elif new_temp < lowest_temp:
        lowest_temp = new_temp
        music.start_melody(music.built_in_melody(Melodies.WAWAWAWAA),
                           MelodyOptions.ONCE)
    if new_temp > old_temp:
        temp_up_animation()
    elif new_temp < old_temp:
        temp_down_animation()
    basic.show_number(new_temp)
    basic.pause(1000)
    basic.show_number(new_temp)
    old_temp = new_temp
    basic.pause(1000)


basic.forever(on_forever)
