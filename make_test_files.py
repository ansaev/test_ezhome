import random
from sys import argv


def make_test_files(file_name_1, file_name_2, file_name_check, items):
    f1 = open(file_name_1, 'w')
    f2 = open(file_name_2, 'w')
    f_check = open(file_name_check, 'w')
    prev_element = None
    for i in range(items):
        if not prev_element:
            item = i
        else:
            item = prev_element + random.randint(0, 3)
        if random.randint(1, 2) == 1:
            f1.write(str(item) + '\n')
        else:
             f2.write(str(item) + '\n')
        f_check.write(str(item) + '\n')
        prev_element = item

if __name__ == "__main__":
    make_test_files(argv[1], argv[2], argv[3], int(argv[4]))