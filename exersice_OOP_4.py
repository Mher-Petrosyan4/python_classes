class Rectangular(object):
    created_rectangulars = 0

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        cls.created_rectangulars += 1
        return self

    def __init__(self, *args):
        self.length, self.width = args

    def __to_sorted_tuple(self):
        return sorted((self.width, self.length))

    def __eq__(self, other):
        if not isinstance(other, Rectangular):
            raise TypeError(f'Can\'t compare {type(self)} and {type(other)}')

        return self.__to_sorted_tuple() == other.__to_sorted_tuple()

    def __gt__(self, other):
        if not isinstance(other, Rectangular):
            raise TypeError(f'Can\'t compare {type(self)} and {type(other)}')

        first_rec = self.__to_sorted_tuple()
        second_rec = other.__to_sorted_tuple()
        is_greater = True
        for i in range(3):
            if first_rec[i] < second_rec[i]:
                is_greater = False
                break
        return is_greater

    def perimeter_of_rectangular(self):
        return 2 * (self.width + self.length)

    def area_of_rectangular(self):
        return self.width * self.length

    def is_alike(self, other):
        first_rec = self.__to_sorted_tuple()
        second_rec = other.__to_sorted_tuple()
        if first_rec[0] / second_rec[0] == first_rec[1] / second_rec[1]:
            return f'{self} and {other} are alike.'
        return f'{self} and {other} are not alike.'


rec_1 = Rectangular(3, 7)
rec_2 = Rectangular(7, 3)
rec_3 = Rectangular(9, 21)
print(rec_1.perimeter_of_rectangular())
print(rec_3.area_of_rectangular())
print(rec_1 == rec_2)
print(rec_1.is_alike(rec_3))
print(Rectangular.created_rectangulars)




