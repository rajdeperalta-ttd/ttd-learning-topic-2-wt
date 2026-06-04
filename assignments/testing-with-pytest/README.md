# 📘 Assignment: Testing Your Code with pytest

## 🎯 Objective

Learn how to write automated tests using `pytest` to verify that your Python functions work correctly, including handling normal inputs and edge cases.

## 📝 Tasks

### 🛠️ Write Your First Test

#### Description
Open `starter-code.py` and look at the provided `add` and `is_even` functions. Write a test file called `test_functions.py` that contains at least one test for each function.

#### Requirements
Completed program should:

- Create a file named `test_functions.py`
- Import `add` and `is_even` from `starter-code.py`
- Define a test function `test_add` that calls `add` and uses `assert` to check the result
- Define a test function `test_is_even` that calls `is_even` and uses `assert` to check the result
- All tests pass when running `pytest test_functions.py`


### 🛠️ Test Multiple Cases

#### Description
Extend your test file to cover more than just a single "happy path" input — test edge cases like zero, negative numbers, and odd numbers.

#### Requirements
Completed program should:

- Add additional assertions (or separate test functions) for `add` covering negative numbers and zero
- Add additional assertions (or separate test functions) for `is_even` covering odd numbers, zero, and negative even numbers
- All tests still pass when running `pytest test_functions.py`


### 🛠️ Test for Errors (Stretch Goal)

#### Description
The `divide` function in `starter-code.py` raises a `ValueError` when dividing by zero. Write a test that confirms this behavior using `pytest.raises`.

#### Requirements
Completed program should:

- Import `divide` from `starter-code.py`
- Define a test function `test_divide_by_zero` that uses `pytest.raises(ValueError)` to assert that calling `divide(10, 0)` raises a `ValueError`
- All tests pass when running `pytest test_functions.py`

```python
# Example usage of pytest.raises
import pytest

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```
