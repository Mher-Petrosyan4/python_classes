v = 'Python'
# #ex 1
# for i in range(10):
#     print('*' * i)
#
# #ex 2
# num = input('Enter the number: ')
# count_of_even = 0
# for i in num:
#     if int(i) % 2 == 0:
#         count_of_even += 1
#
# print('{} >>>> {}'.format(num, count_of_even))
#
#
# #ex 3
# for i in range(1, 10):
#     print('{} + {} = {}'.format(i, i + 1, (i + i + 1)))
#
#
# #ex 4
# first_str = input('Enter smth\n')
# filtered_str = first_str[0:len(first_str):2]
# new_str = ''
# for i in filtered_str:
#     new_str += i
# print(new_str)
# #

#
# first_str = input('Enter smth\n')
# new_str = ''
# for i in range(0, len(first_str)):
#     if i % 2 != 0:
#         continue
#     new_str += first_str[i]
# print(new_str)
#
#
# #ex 5
# num = int(input('Enter a number\n'))
# new_list = []
# for i in range(1, (num // 2) + 1):
#     if num % i == 0:
#         new_list.append(i)
# print(new_list)
#
# num = int(input('Enter a number\n'))
# for i in range(1, (num // 2) + 1):
#     if num % i == 0:
#         print(i)
#
#
#
