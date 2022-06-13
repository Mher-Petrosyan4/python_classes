import os

current_directory = os.getcwd()
path_1 = 'Dir1'
path_2 = 'Dir2'
path_3 = 'Dir3'
path_4 = 'Dir4'
with open('File.txt', 'w') as f:
    pass
os.makedirs(f'{path_1}/{path_2}')
os.chdir(f'{path_1}')
os.makedirs(f'{path_3}/{path_4}')
os.chdir('..')
cur_dir = True
user_answer = input('Do you want to delete created paths?: ')
while cur_dir:
    path = os.listdir()
    if path:
        try:
            os.rmdir(path[0])
        except OSError:
            os.chdir(path[0])
    else:
        os.chdir('..')
        if os.getcwd() == current_directory:
            os.remove('File.txt')
            os.rmdir(f'{path_1}')
            cur_dir = False






