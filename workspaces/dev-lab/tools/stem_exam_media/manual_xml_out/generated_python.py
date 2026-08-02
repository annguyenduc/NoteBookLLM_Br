from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1

def on_button_a_pressed():
  global ngaTu
  ngaTu = 0
  while True:
    if False and False:
      ngaTu = ngaTu + 1
      display.scroll(ngaTu)
      await robot.follow_line_by_time(0.4, then=STOP)
    elif False:
      robot.speed_ratio(left=35, right=60)
      robot.forward()
    elif False:
      robot.speed_ratio(left=60, right=35)
      robot.forward()
    elif False:
      robot.speed_ratio(left=(-20), right=60)
      robot.forward()
    elif False:
      robot.speed_ratio(left=60, right=(-20))
      robot.forward()
    else:
      robot.speed_ratio(left=60, right=60)
      robot.forward()

button_a.on_pressed = on_button_a_pressed


line.read()[0]

line.read()[3]

line.read()[1]

line.read()[2]

line.read()[0]

line.read()[3]
