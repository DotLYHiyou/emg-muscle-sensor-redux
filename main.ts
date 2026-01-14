// Button A Resets the system
input.onButtonPressed(Button.A, function () {
    control.reset()
})
// Logo button turns on low power mode
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    power.lowPowerRequest()
    power.lowPowerEnable(LowPowerEnable.Allow)
})
// Variable sets "a" to the 0 pin reading
let a = pins.analogReadPin(AnalogPin.P0)
// Instructions on how to send data outside of the micro:bit through USB.
serial.redirect(
SerialPin.USB_TX,
SerialPin.USB_RX,
BaudRate.BaudRate115200
)
// Redirecting everything to USB
serial.redirectToUSB()
// Constant reading every half-second.
basic.forever(function () {
    basic.pause(500)
    serial.writeLine("The reading is now:")
    serial.writeLine("" + pins.analogReadPin(AnalogPin.P0) + " VDN (Voltage Difference Number)")
    serial.writeLine("")
})
// Interactive graph on the micro:bit LED display
basic.forever(function () {
    led.plotBarGraph(
    pins.analogReadPin(AnalogPin.P0),
    1023,
    false
    )
})
