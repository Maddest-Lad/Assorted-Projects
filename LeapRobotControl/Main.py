import Leap
import time


class LeapControl:

    def init(self):
        # Initialize the listener
        self.controller = Leap.Controller()
        self.frame = self.controller.frame()
        self.calibration = []

    def update(self):
        frame = self.controller.frame()  # Take a new snapshot of hand position

        if len(frame.hands) == 2:  # Make sure that we only read two hands

            right = frame.hands.rightmost
            left = frame.hands.leftmost

            rightPos = right.palm_position
            leftPos = left.palm_position

            return leftPos[2], rightPos[2]
        else:
            return None

    def calibrate(self):  # Calibrates The Sensor On Startup
        Left, Right = [], []

        print("Calibrating ...")

        for i in range(100):
            data = self.update()
            time.sleep(0.1)

            if data is not None:
                Left.append(data[0])
                Right.append(data[1])

        leftMin, leftMax = min(Left), max(Left)
        rightMin, rightMax = min(Right), max(Right)

        self.calibration = [int(leftMin), int(leftMax), int(rightMin), int(rightMax)]
        print("Calibration Finished")

    def map(self, value, a, b, c, d):
        y = (value - a) / (b - a) * (d - c) + c
        return y

    def getMovement(self):
        data = None

        while data is None:
            data = self.update()

        left = int(self.map(data[0], self.calibration[0], self.calibration[1], 0, 100))
        right = int(self.map(data[1], self.calibration[2], self.calibration[3], 0, 100))
        return left, right


leap = LeapControl()
leap.calibrate()

while True:
    payload = leap.getMovement()
    print(payload)