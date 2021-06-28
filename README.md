# Test Driven Development

TDD is a software development practice that focusess
on coding, testing (unit testing) and refactoring.

![TDD Diagram](https://www.xenonstack.com/images/insights/2020/04/test-driven-development-tools-best-practices-xenonstack.png)

- **Step 1**: Write tests to fail
- **Step 2**: write code that passes the test
- **Step 3**: Refactor the code/clean code/eliminate redundancies

## Testing

### unittest
Creating test cases are accomplished by subclassing `unittest.TestCase`
```python
import unittest

class Calctest(unittest.TestCase):
        def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)
```

`python -m unittest`
`python -m unittest discover -v`

## py.test
Install:
`$ pip install pytest`
