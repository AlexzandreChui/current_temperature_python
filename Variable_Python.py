# Created By: Alex.C
# Created On:2022/09/27
# This program changes the counter by 1 when the A buttono is pressed.

def on_button_pressed_a():
    global counter
    counter += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

#Created By: Alex.C
# Created On:2022/09/27
# This program changes the counter by -1 when the B button is pressed.

def on_button_pressed_b():
    global counter
    counter += -1
input.on_button_pressed(Button.B, on_button_pressed_b)

# Created By:Alex.C
# Created On:2022/09/27
# This program shows the counter number when the A+B is pressed.

def on_button_pressed_ab():
    basic.show_number(counter)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

counter = 0
counter = 0
