import string


def fun1(path_to_file):
    file = open(path_to_file, 'w')
    return file


def fun2(file_to_close):
    file_to_close.close()


def fun3(file_to_save_data, my_string):
    my_final_string = [i for i in my_string if not i.islower()]
    file_to_save_data.write(''.join(my_final_string))
