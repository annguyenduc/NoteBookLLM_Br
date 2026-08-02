from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1

def on_button_a_pressed():
  global ngaTu
  display.scroll('GO')
  ngaTu = 0
  while True:
    await robot.follow_line_until_cross(then=STOP)
    ngaTu = ngaTu + 1
    display.scroll(ngaTu)
    await robot.follow_line_by_time(0.4, then=STOP)

button_a.on_pressed = on_button_a_pressed
