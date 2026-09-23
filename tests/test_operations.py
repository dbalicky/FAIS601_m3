import pytest
from typing import Union
from app.operations import Operations as ops

Num = Union[int, float]

@pytest.mark.parametrize(
    "x, y, expected",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-2, 3, 1),
        (1.5, 3.2, 4.7),
        (-2.5, 4.5, 2.0)
    ],
    ids=[
        "add_two_positive_integers",
        "add_two_zeroes",
        "add_negative_and_positive_integer",
        "add_two_positive_floats",
        "add_negative_and_positive_float"
    ]
)
def test_addition(x: Num, y: Num, expected: Num) -> None:
    result = ops.add(x, y)
    assert result == expected, f"Expexcted result for adding {x} and {y} is {expected}, but got {result}"

@pytest.mark.parametrize(
    "x, y, expected",
    [
        (-3, 5, -8),
        (0, 0, 0),
        (-4, -3, -1),
        (2.5, 3.5, -1.0),
        (-1.5, -3.0, 1.5),
        (2.5, -0.5, 3.0)
    ],
    ids=[
        "subtract_positive_integer_from_negative_integer",
        "subtract_two_zeroes",
        "subtract_two_negative_integers",
        "subtract_two_positive_floats",
        "subtract_two_negative_floats",
        "subtract_negative_float_from_positive_float"
    ]
)
def test_subtraction(x: Num, y: Num, expected: Num) -> None:
    result = ops.sub(x, y)
    assert result == expected, f"Expexcted result for adding {x} and {y} is {expected}, but got {result}"

@pytest.mark.parametrize(
    "x, y, expected",
    [
        (2, 5, 10),
        (0, 0, 0),
        (-4, -3, 12),
        (2.5, 3.0, 7.5),
        (-1.5, -4.0, 6.0),
        (2.0, -3.0, -6.0)
    ],
    ids=[
        "multiply_two_positive_integers",
        "multiply_two_zeroes",
        "multiply_two_negative_integers",
        "multiply_two_positive_floats",
        "multiply_two_negative_floats",
        "multiply_negative_float_and_positive_float"
    ]
)
def test_multiplication(x: Num, y: Num, expected: Num) -> None:
    result = ops.mult(x, y)
    assert result == expected, f"Expexcted result for adding {x} and {y} is {expected}, but got {result}"

@pytest.mark.parametrize(
    "x, y, expected",
    [
        (6, 3, 2),
        (-4, -2, 2),
        (4.5, 3.0, 1.5),
        (-3.0, -1.0, 3.0),
        (2.0, -2.0, -1.0),
        (0, -2.0, 0)
    ],
    ids=[
        "divide_two_positive_integers",
        "divide_two_negative_integers",
        "divide_two_positive_floats",
        "divide_two_negative_floats",
        "divide_positive_float_by_negative_float",
        "divide_zero_by_negative_float"
    ]
)
def test_division(x: Num, y: Num, expected: Num) -> None:
    result = ops.div(x, y)
    assert result == expected, f"Expexcted result for adding {x} and {y} is {expected}, but got {result}"

@pytest.mark.parametrize(
    "x, y",
    [
        (1, 0),
        (-1, 0),
        (0, 0)
    ],
    ids=[
        "divide_positive_integer_by_zero",
        "divide_negative_integer_by_zero",
        "divide_zero_by_zero"
    ]
)
def test_division_by_zero(x: Num, y: Num) -> None:

    with pytest.raises(ValueError, match="Division by zero is not allowed") as excinfo:
        ops.div(x,y)

    assert "Division by zero is not allowed" in str(excinfo.value), \
        f"Expexcted error message: 'Division by zero is not allowed', but got '{excinfo.value}'"