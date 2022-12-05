from Old.Motor_Controller import L298N


class Drive:
    # Motor Controllers
    frontLeft = L298N(0, 1, 2)
    frontRight = L298N(3, 4, 5)
    backLeft = L298N(6, 7, 8)
    backRight = L298N(9, 10, 11)

    def __init__(self):
        self.temp = "temp"


# Maps Number From [min_1, max_1] to [min_2, max_2]
def map_to_range(number, min_1, max_1, min_2=0, max_2=100):
    return (number - min_1) * (max_2 - min_2) / (max_1 - min_1) + min_2


print(map_to_range(15, 0, 200))
