import pytest

from q20 import solve

# List of test cases in the form [(input, output)]
# Ideally there should be 10 test cases
TEST_CASES = [
    (2187, True),      # 27 * 81 = 2187
    (126, False),      # odd number of digits
    (1122, False),     # even digits but no valid fangs
    (536539, True),    # 953 * 563 = 536539
    (125460, True),    # 204 * 615 = 125460
    (1260, True),      # 21 * 60 = 1260
    (6880, True),      # 80 * 86 = 6880
    (100, False),      # odd number of digits
    (1000, False),     # only fang pairs both end with 0
    (9999, False),     # 99 * 99 = 9801 ≠ 9999
]


@pytest.mark.parametrize("number,expected", TEST_CASES)
def test_validation(number, expected):
    assert solve(number) == expected
