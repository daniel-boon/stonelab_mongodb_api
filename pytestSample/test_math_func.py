from math_func import StudentDB
import pytest
db = None

# @pytest.mark.number
# def test_add():
#     assert math_func.add(7,3) == 10
#     assert math_func.add(7) == 9
#     assert math_func.add(5, 3), '------------'

# @pytest.mark.number
# def test_product():
#     assert math_func.product(5,5) == 25
#     assert math_func.product(5) == 10
#     assert math_func.product(7) == 14

# @pytest.mark.strings
# def test_add_strings():
#     result = math_func.add('Hello',' World')
#     assert result == 'Hello World'
#     assert type(result) is str
#     assert 'Hello' in result
    
# @pytest.mark.strings
# def test_product_strings():
#     assert math_func.product('Hello ', 3)=='Hello Hello Hello '
#     result = math_func.product('Hello ')
#     assert result == 'Hello Hello '
#     assert type(result) is str
#     assert 'Hello' in result

def setup_module(module):
    print('-----------setup-----------')
    global db
    db=StudentDB()
    db.connect('pytestSample/data.json')

def teardown_module(module):
    ('-----------teardown-----------')
    db.close()


def test_scott_data():
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'

def test_mark_data():
    scott_data = db.get_data('Mark')
    assert scott_data['id'] == 2
    assert scott_data['name'] == 'Mark'
    assert scott_data['result'] == 'fail'
