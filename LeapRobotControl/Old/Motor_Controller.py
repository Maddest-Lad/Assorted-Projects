import gpiozero


class L298N:

    def __init__(self, forward, backward, pwm):

        # On/Off output
        self.forward = gpiozero.OutputDevice(forward)
        self.backward = gpiozero.OutputDevice(backward)
        self.pwm = gpiozero.PWMOutputDevice(pwm)

    # Set's Wheel Power
    # Power : value from [-100, 100] which dictates the duty cycle for pwm
    def set_power(self, power) -> None:
        # If Positive, Forward is Primary Direction - Otherwise Negative Is
        if power > 0:
            self.forward.on()
            self.backward.off()
        else:
            self.forward.off()
            self.backward.on()

        self.pwm.value = abs(power)
