class ColorChanger:

    def __init__(self):

        self.color = [255, 0, 0]
        self.color_index = 1
        self.increment = 2

    def change_color_index(self):
        if self.color_index == 1:
            self.color_index = 0
        elif self.color_index == 0:
            self.color_index = 2
        elif self.color_index == 2:
            self.color_index = 1
        self.increment = -self.increment

    def change_color(self):

        self.color[self.color_index] += self.increment
        if self.increment > 0:
            if self.color[self.color_index] >= 255:
                self.color[self.color_index] = 255
                self.change_color_index()
        elif self.color[self.color_index] <= 0:
            self.color[self.color_index] = 0
            self.change_color_index()

        return tuple(self.color)
