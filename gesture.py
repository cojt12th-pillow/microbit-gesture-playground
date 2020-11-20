ShakeTime = 0
preZ = 0

def on_forever():
    global preZ, ShakeTime
    serial.write_value("x", input.acceleration(Dimension.X))
    serial.write_value("y", input.acceleration(Dimension.Y))
    serial.write_value("z", input.acceleration(Dimension.Z))
    basic.show_number(ShakeTime)
    preZ = input.acceleration(Dimension.Z)
    basic.pause(1000)
    serial.write_value("diff", abs(preZ - input.acceleration(Dimension.Z)))
    if abs(preZ - input.acceleration(Dimension.Z)) > 200:
        ShakeTime += 1
    else:
        ShakeTime = 0
basic.forever(on_forever)