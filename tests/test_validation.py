import pytest

from q01 import solve

# List of test cases in the form [(input, output)]
TEST_CASES = [
    ("0. pop 0", "1 imix 0"),
    ("10. zac 0", "3 chuen 0"),
    ("10. zac 1995", "9 cimi 2801"),
    ("19. cumhu 0", "9 ahau 1"),      # last day before uayet
    ("4. uayet 0", "1 chicchan 1"),   # last valid day of uayet
    ("0. pop 4999", "8 cib 7017"),    # max valid year
    ("5. uayet 0", ""),               # impossible: uayet only has days 0-4
    ("20. pop 0", ""),                # impossible: regular month max day is 19
    ("0. pop 5000", ""),              # year >= 5000
    ("0. pop -1", ""),                # negative year
]


@pytest.mark.parametrize("input,expected", TEST_CASES)
def test_solver(input, expected):
    assert solve(input) == expected
