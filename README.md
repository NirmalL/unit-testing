# Unit Testing (experiments)

### Nose (Python 2)

library of interfaces

```python
def sin(rad):
	pass

def cos(rad):
	pass

def tan(rad):
	pass
```

test bootstrap with a sample testcase func

```python
from one import sin, cos, tan
import math

from nose.tools import *

def setupf():
	"Set up the instance for testing"
	pass

def teardownf():
	"Tear down the instance"
	pass

@with_setup(setupf, teardownf) # decorator
def test_sin_float():
	"Test for valid a float argument"
	assert False
```
this is set to fail, as we haven't checked anything yet

assertion of output value
```python
@with_setup(setupf, teardownf) # decorator
def test_sin_float():
	"Test for a valid float argument"
	assert math.sin(.1) == sin(.1)
```

precision issues
```python
@with_setup(setupf, teardownf) # decorator
def test_sin_float():
	"Test for a valid float argument"
	assert_almost_equals(math.sin(.1), sin(.1), places=4)
```

still not implemented
```python
e = 2.71828182846

def sin(rad):
	return (e**(rad*1j)).imag
```

run
```bash
nosetests .\test_one.py --verbose
```

more test cases for sine
```python
@with_setup(setupf, teardownf)
def test_sin_float():
	"Test for a valid float argument"
	assert_almost_equals(math.sin(.1), sin(.1), places=4)

@with_setup(setupf, teardownf)
def test_sin_int():
	"Test for a valid float argument"
	assert_almost_equals(math.sin(2), sin(2), places=4)

@with_setup(setupf, teardownf)
def test_sin_float_negative():
	"Test for a valid negative float argument"
	assert_almost_equals(math.sin(-.1), sin(-.1), places=4)

@with_setup(setupf, teardownf)
def test_sin_float_negative():
	"Test for a valid negative int argument"
	assert_almost_equals(math.sin(-2), sin(-2), places=4)

@with_setup(setupf, teardownf)
def test_sin_zero():
	"Test for a valid negative float argument"
	assert_almost_equals(math.sin(0), sin(0), places=4)
```

duplication and redundancy --> test generators

basic python list

```python
def test_sin_values():
	for x in [-2, -.1, 0, .1, 2]:
		yield check_sin_values, x

@with_setup(setupf, teardownf)
def check_sin_values(x):
	"Test for a valid float argument"
	assert_almost_equals(math.sin(.1), sin(.1), places=4)
```

even something like `range(-2, 2, 0.4)` (.4 steps)

if there's no consequenses or effects of repeated calling on the func,
setup only once
```python
@with_setup(setupf, teardownf)
def test_sin_values():
	for x in [-2, -.1, 0, .1, 2]:
		yield check_sin_values, x

def check_sin_values(x):
	"Test for a valid float argument"
	assert_almost_equals(math.sin(.1), sin(.1), places=4)
```

class method tests [todo]