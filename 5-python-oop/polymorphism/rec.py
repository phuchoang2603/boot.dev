class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        return self.__x1 if self.__x1 < self.__x2 else self.__x2

    def get_right_x(self):
        return self.__x1 if self.__x1 > self.__x2 else self.__x2

    def get_top_y(self):
        return self.__y1 if self.__y1 > self.__y2 else self.__y2

    def get_bottom_y(self):
        return self.__y1 if self.__y1 < self.__y2 else self.__y2

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"

    def overlaps(self, rect):
        if (
            self.get_left_x() < rect.get_right_x()
            and self.get_right_x() > rect.get_left_x()
            and self.get_top_y() > rect.get_bottom_y()
            and self.get_bottom_y() < rect.get_top_y()
        ):
            return True
        else:
            return False
