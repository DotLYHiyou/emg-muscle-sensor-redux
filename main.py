# Button A Resets the system
def on_button_pressed_a():
    control.reset()
input.on_button_pressed(Button.A, on_button_pressed_a)

# Logo button turns on low power mode
def on_logo_touched():
    power.low_power_request()
    power.low_power_enable(LowPowerEnable.ALLOW)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

# Variable sets a to the 0 pin reading
a = pins.analog_read_pin(AnalogPin.P0)
# Setting the ground-work for how the computer will communicate.
serial.redirect(SerialPin.USB_TX, SerialPin.USB_RX, BaudRate.BAUD_RATE115200)
# Redirecting everything to USB
serial.redirect_to_usb()

# Constant reading every half-second.
def on_forever():
    basic.pause(500)
    serial.write_line("The reading is now:")
    serial.write_line("" + str(pins.analog_read_pin(AnalogPin.P0)) + " VDN (Voltage Difference Number)")
    serial.write_line("")
basic.forever(on_forever)

# Interactive graph on the micro:bit LED display
def on_forever2():
    led.plot_bar_graph(pins.analog_read_pin(AnalogPin.P0), 1023, False)
basic.forever(on_forever2)
