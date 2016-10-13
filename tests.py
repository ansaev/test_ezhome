from main import sort_merge, iter_sort_merge, merge_sort
from make_test_files import make_test_files
FILE_1_PATH = '/tmp/my_test_1.txt'
FILE_2_PATH = '/tmp/my_test_2.txt'
FILE_CHECK_PATH = '/tmp/my_test_check.txt'


class TestArrayFunction:
    def test_simple_merge(self):
        assert sort_merge([1, 2, 5], [2, 3]) == [1, 2, 2, 3, 5]

    def test_empty_input(self):
        assert sort_merge([1, 2, 5], []) == [1, 2, 5]

    def test_int_input(self):
        try:
            sort_merge([1, 2, 5], 1)
        except BaseException as ex:
            assert isinstance(ex, TypeError)
            return
        assert False

    def test_set_input(self):
        try:
            sort_merge({1, 2}, [1, 2, 5])
        except BaseException as ex:
            assert isinstance(ex, TypeError)
            return
        assert False


class TestGeneratorFunction:
    def test_simple_merge(self):
        make_test_files(FILE_1_PATH, FILE_2_PATH, FILE_CHECK_PATH, 1000)
        f1 = open(FILE_1_PATH, 'r')
        f2 = open(FILE_2_PATH, 'r')
        f_check = open(FILE_CHECK_PATH, 'r')
        f1_iter = iter((int(l) for l in f1))
        f2_iter = iter((int(l) for l in f2))
        f_check_iter = iter((int(l) for l in f_check))
        res = iter_sort_merge(f1_iter, f2_iter)
        for i in res:
            assert i == f_check_iter.__next__()

    def test_empty_merge(self):
        make_test_files(FILE_1_PATH, FILE_2_PATH, FILE_CHECK_PATH, 1)
        f1 = open(FILE_1_PATH, 'r')
        f2 = open(FILE_2_PATH, 'r')
        f_check = open(FILE_CHECK_PATH, 'r')
        f1_iter = iter((int(l) for l in f1))
        f2_iter = iter((int(l) for l in f2))
        f_check_iter = iter((int(l) for l in f_check))
        res = iter_sort_merge(f1_iter, f2_iter)
        for i in res:
            assert i == f_check_iter.__next__()

    def test_big_merge(self):
        ELEMENTS = 1000000
        make_test_files(FILE_1_PATH, FILE_2_PATH, FILE_CHECK_PATH, ELEMENTS)
        f1 = open(FILE_1_PATH, 'r')
        f2 = open(FILE_2_PATH, 'r')
        f_check = open(FILE_CHECK_PATH, 'r')
        f1_iter = iter((int(l) for l in f1))
        f2_iter = iter((int(l) for l in f2))
        f_check_iter = iter((int(l) for l in f_check))
        res = iter_sort_merge(f1_iter, f2_iter)
        for res_element in res:
            check_element = f_check_iter.__next__()
            assert res_element == check_element


class TestMergeSort:
    def test_simple_sort(self):
        assert merge_sort(iter([10,12,5,2,15,3,2])) == [2,2,3, 5, 10,12,15]



