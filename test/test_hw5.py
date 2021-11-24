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

# 5. count_simba

from pink.hw5 import count_simba

def test_count_simba():
    x = ["Simba and Nala are lions.", "I laugh in the face of danger.", "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]
    output = count_simba(x)
    expected_output = 2
    assert output == expected_output

