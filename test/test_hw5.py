# I changed all print() in hw5 to return to be able to do output == expected_output
# I don't know how to test read_data when the data exists
# pytest --cov=hw5 --cov-fail-under 80

# 1. car_at_light
from pink.hw5 import car_at_light

def test_car_at_light_red():
    x = "red"
    output = car_at_light(x)
    expected_output = "stop"
    assert output == expected_output

def test_car_at_light_green():
    x = "green"
    output = car_at_light(x)
    expected_output = "go"
    assert output == expected_output

def test_car_at_light_yellow():
    x = "yellow"
    output = car_at_light(x)
    expected_output = "wait"
    assert output == expected_output

def test_car_at_light_black():
    x = "black"
    output = car_at_light(x)
    expected_output = "Undefined instruction for color: "+ x
    assert output == expected_output

# 2. safe_subtract

from pink.hw5 import safe_subtract

def test_safe_subtract():
    x = 1
    y = 3
    output = safe_subtract(x,y)
    expected_output = 2
    assert output == expected_output

def test_safe_subtract_none():
    x = [1]
    y = 3
    output = safe_subtract(x,y)
    expected_output = 'None'
    assert output == expected_output

# 3. retrieve_age

from pink.hw5 import retrieve_age_lbyl

def test_retrieve_age_lbyl():
    x = dict({'name': 'John', 'last_name': 'Doe', 'birth': 1987})
    output = retrieve_age_lbyl(x)
    expected_output = "John is 34 years old"
    assert output == expected_output

def test_retrieve_age_lbyl_miss():
    x = dict({'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'})
    output = retrieve_age_lbyl(x)
    expected_output = "Some keys are missing"
    assert output == expected_output

from pink.hw5 import retrieve_age_eafp

def test_retrieve_age_eafp():
    x = dict({'name': 'John', 'last_name': 'Doe', 'birth': 1987})
    output = retrieve_age_eafp(x)
    expected_output = "John is 34 years old"
    assert output == expected_output

def test_retrieve_age_eafp_miss():
    x = dict({'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'})
    output = retrieve_age_eafp(x)
    expected_output = "Some keys are missing"
    assert output == expected_output

# 4. read_data

from pink.hw5 import read_data

def test_read_data_miss():
    x = 'testfile.csv'
    output = read_data(x)
    expected_output = 'Error: File does not appear to exist.'
    assert output == expected_output

# 6. count_simba

from pink.hw5 import count_simba

def test_count_simba():
    x = ["Simba and Nala are lions.", "I laugh in the face of danger.", "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]
    output = count_simba(x)
    expected_output = 2
    assert output == expected_output

# 7. get_day_month_year

from pink.hw5 import get_day_month_year
import pandas as pd
from pandas.testing import assert_frame_equal

def test_get_day_month_year():
    x = ["2021-11-12", "2018-12-25", "2017-11-16", "2019-10-27"]
    output=get_day_month_year(x)
    expected_output = pd.DataFrame({'year': ['2021', '2018', '2017', '2019'],
                                    'month': ['11', '12', '11', '10'],
                                    'day': ['12','25','16','27']})
    assert_frame_equal(output, expected_output)

# 8. compute_distance

from pink.hw5 import compute_distance

def test_compute_distance():
    example = [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
    output = compute_distance(example)
    expected_output = [31.13186522205169,157.005827868894]
    assert output == expected_output

# 8. sum_general_int_list
    
from pink.hw5 import sum_general_int_list

def test_sum_general_int_list():
    example = [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]
    output = sum_general_int_list(example)
    expected_output =48
    assert output == expected_output