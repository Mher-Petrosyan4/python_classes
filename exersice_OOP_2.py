# # ex 1
# class Person:
#     def __init__(self, name, surname, age, faculty):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.faculty = faculty
#
#     def fullname(self):
#         return f'{self.name} {self.surname}'
#
#     def age(self):
#         return self.age
#
#
# class Student(Person):
#     def __init__(self, name_, surname_, age_, faculty_, admission_year):
#         super().__init__(name_, surname_, age_, faculty_)
#         self.admission_year = admission_year
#
#     def change_faculty(self, fac_1):
#         self.faculty = fac_1
#
#
# student_1 = Student('Mher', 'Petrosyan', 26, 'Accounting', 2012)
# print(student_1.fullname())
# student_1.change_faculty('Information technologies')
# print(student_1.faculty)
# print(student_1.age)
#
#
# # ex 2
# class Country:
#     def __init__(self, name, continent):
#         self.country_name = name
#         self.continent = continent
#
#     def country_presentation(self):
#         return f'The country {self.country_name} is located in {self.continent}'
#
#
# class Brand:
#     def __init__(self, name, start_date):
#         self.brand_name = name
#         self.start_date = start_date
#
#     def brand_presentation(self):
#         return f'The {self.brand_name} brand was founded in {self.start_date}'
#
#
# class Season:
#     def __init__(self, name, average_temp):
#         self.season_name = name
#         self.temperature = average_temp
#
#     def season_presentation(self):
#         return f'In {self.season_name} season the average temperature is {self.temperature}'
#
#
# class Product(Country, Brand, Season):
#     def __init__(self, country_name, continent_name, prod_brand, prod_brand_date, season_type,
#                  season_temp, product_name, product_type, price, quantity):
#         self.name = product_name
#         self.type = product_type
#         self.price = price
#         self.quantity = quantity
#         self.disc_percent = 0
#         self.added_amount = 0
#         self.decreased_amount = 0
#         Country.__init__(self, country_name, continent_name)
#         Brand.__init__(self, prod_brand, prod_brand_date)
#         Season.__init__(self, season_type, season_temp)
#
#     def product_info(self):
#         return f'The {self.name} was produced in {self.continent}, {self.country_name}.' \
#                f' Its the {self.type} type, the price is {self.price} USD and the remain in warehouse' \
#                f' is {self.quantity} items.'
#
#     def discount(self, percent):
#         self.disc_percent = percent
#         self.price -= (self.price * self.disc_percent / 100)
#
#     def add_qnt(self, qnt):
#         self.quantity += qnt
#         self.added_amount += qnt
#
#     def decrease_qnt(self, qnt):
#         if qnt > self.quantity:
#             raise Exception("You dont have enough quantity in your warehouse.")
#         self.quantity -= qnt
#         self.decreased_amount += qnt
#
#
# product_1 = Product('Usa', 'North America', 'Adidas', 2021, 'summer', 30, 'Ultraboost', 'Boots', 190, 22)
#
#
# # ex 3
# class Hotel:
#     def __init__(self, name, place):
#         self.hotel_name = name
#         self.hotel_place = place
#         self.mid_rooms = {}
#         self.lux_rooms = {}
#         self.mid_rooms_price = 20000
#         self.lux_rooms_price = 35000
#
#     def hotel_presentation(self):
#         return f'The {self.hotel_name} is located in {self.hotel_place}. It has {len(self.mid_rooms)} mid rooms and' \
#                f' {len(self.lux_rooms)} lux rooms.' \
#                f'The price for mid rooms is {self.mid_rooms_price} AMD for one night and the price for lux rooms ' \
#                f' is {self.lux_rooms_price} AMD for one night'
#
#     def book(self, room_type):
#         if room_type == 'mid_room':
#             for key, value in self.mid_rooms.items():
#                 if value == 'free':
#                     self.mid_rooms[key] = 'busy'
#                     return 'You have booked one mid_room'
#             return 'We don\'t have free mid_rooms'
#         elif room_type == 'lux_room':
#             for key, value in self.lux_rooms.items():
#                 if value == 'free':
#                     self.lux_rooms[key] = 'busy'
#                     return 'You have booked one lux_room'
#             return 'We don\'t have free lux_rooms'
#         return 'We dont have such kind of rooms'
#
#     def available_room_check(self, room_type):
#         if room_type == 'mid_room':
#             if 'free' in self.mid_rooms.values():
#                 return 'We have free mid_rooms.'
#             return 'We don\'t have free mid_rooms.'
#         elif room_type == 'lux_room':
#             if 'free' in self.lux_rooms.values():
#                 return 'We have free lux_rooms.'
#             return 'We don\'t have free lux_rooms.'
#
#
# class Taxi:
#     def __init__(self, name, car_type, price_for_tour):
#         self.taxi_name = name
#         self.taxi_car_type = car_type
#         self.taxi_price_for_tour = price_for_tour
#
#     def taxi_presentation(self):
#         return f'The {self.taxi_name} taxi provides tour services with  {self.taxi_price_for_tour} AMD ' \
#                f'with comfortable {self.taxi_car_type} cars.'
#
#
# class Tour(Hotel, Taxi):
#     def __init__(self, tour_name, hotel_name, place, taxi_name, car_type, taxi_price):
#         self.tour_name = tour_name
#         Hotel.__init__(self, hotel_name, place)
#         Taxi.__init__(self, taxi_name, car_type, taxi_price)
#         self.price_lux = self.lux_rooms_price + self.taxi_price_for_tour
#         self.price_mid = self.mid_rooms_price + self.taxi_price_for_tour
#
#     def tour_presentation(self):
#         return f'Hello. We offer "{self.tour_name}" tour. We have two options. {self.price_lux} AMD and {self.price_mid} AMD,' \
#                f' which includes transport with "{self.taxi_name}" company which provides {self.taxi_car_type} cars and' \
#                f'its price is {self.taxi_price_for_tour} AMD. You can stay at "{self.hotel_name}" hotel, which' \
#                f' offers lux rooms around {self.lux_rooms_price} AMD and mid rooms around {self.mid_rooms_price} AMD.'
#
#
# tour_1 = Tour('Travel Armenia', "Mariot", 'Tsaghkadzor', 'Ani', 'Mercedes Vito', 10000)
# tour_1.mid_rooms = {100: 'free', 101: 'free', 102: 'free', 103: 'free'}
# tour_1.lux_rooms = {104: 'free', 105: 'free', 106: 'free', 107: 'free'}
# print(tour_1.hotel_presentation())
# print(tour_1.tour_presentation())





