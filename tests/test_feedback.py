from score_calculator import calculate_average

def test_average():
    assert calculate_average([3, 4, 5]) == 4.0

def test_average_empty():
    assert calculate_average([]) == 0
