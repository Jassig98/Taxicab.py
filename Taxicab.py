# Author: Jasmine Singh
# Github username: Jassig98
# Date: October 26, 2022
# Description: Taxicab class, 3 private data members

class Taxicab:
    def __init__(self,x,y):
        self.x_coordinate = x
        self.y_coordinate = y
        self.odometer = 0

    def move_x(self,distance):
        self.x_coordinate += distance
        self.odometer += abs(distance)

    def move_y(self,distance):
        self.y_coordinate += distance
        self.odometer += abs(distance)

    def get_x_coordinate(self):
        return self.x_coordinate

    def get_y_coordinate(self):
        return self.y_coordinate

    def get_odometer(self):
        return self.odometer


