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

another test case
```python
@with_setup(setupf, teardownf)
def test_sin_values():
	for x in [-2, -.1, 0, .1, 2]:
		yield check_sin_values, x
	for x in [-2j, -.1*1j, 0j, .1*1j, 2j]:
		yield check_sin_values, x
	for x in [(-2, -2), (-.1, -.1), (0, 0), (.1, .1), (2, 2)]:
		yield check_sin_values_complex, x

# def check_sin_values ...

def check_sin_values_complex(x):
	"Test for a valid complex float argument"
	p, q = x
	mysin = sin(p+complex(0,q))
	pysin = cmath.sin(p+complex(0,q))
	assert_almost_equals(mysin, pysin, places=4)
```

output
```bash
$ nosetests test_one.py --verbose
```
```
test_one.test_sin_values(-2,) ... ok
test_one.test_sin_values(-0.1,) ... ok
test_one.test_sin_values(0,) ... ok
test_one.test_sin_values(0.1,) ... ok
test_one.test_sin_values(2,) ... ok
test_one.test_sin_values(-2j,) ... ERROR
test_one.test_sin_values((-0-0.1j),) ... ERROR
test_one.test_sin_values(0j,) ... ERROR
test_one.test_sin_values(0.1j,) ... ERROR
test_one.test_sin_values(2j,) ... ERROR
test_one.test_sin_values((-2, -2),) ... ERROR
test_one.test_sin_values((-0.1, -0.1),) ... ERROR
test_one.test_sin_values((0, 0),) ... ok
test_one.test_sin_values((0.1, 0.1),) ... ERROR
test_one.test_sin_values((2, 2),) ... ERROR

============================================
ERROR: test_one.test_sin_values(-2j,)
--------------------------------------------
Traceback (most recent call last):
  File "c:\python27\lib\site-packages\nose\case.py", line 197, in runTest
    self.test(*self.arg)
  File "C:\users\nirmal\desktop\unit-testing\test_one.py", line 28, in check_sin_values
    assert_almost_equals(math.sin(x), sin(x), places=4)
TypeError: can't convert complex to float

============================================

...

--------------------------------------------
Ran 15 tests in 0.010s

FAILED (failures=9)
```

we can see that the complex numbered arguments make for completely inaccurate results in our `sin` function. we'll need to fix or rethink our code to handle such values... or we could throw an exception. to keep away from complex mathematics that's out of scope of today's subject, i'll do the latter.

```python
def sin(rad):
	if isinstance(rad, complex):
		raise ValueError('sin(x) requires real arguments.') 
	return (e**(rad*1j)).imag
```

then we'll assert the raising of the exception, since that's our (now) defined behavior.

```python
def check_sin_values_complex(x):
	"Test for a valid complex float argument"
	p, q = x
	assert_raises(ValueError, sin, p+complex(0,q))
```

this should get all the complex-number test cases to succeed.

but, the output doesn't consider our carefully crafted test descriptions. besides, we have several redundant tests. 

let's be more concise in defining test cases. the actual test cases are:

- real integers
- real floats
- zero
- negative real (both float)
- complex-typed numbers (both float)
- pure imaginary numbers (both float)
- complex-typed negative numbers (both float)

```python
@with_setup(setupf, teardownf)
def test_sin_values_int():
	"Test for a real intger argument"
	assert_almost_equals(math.sin(4), sin(4), places=4)

@with_setup(setupf, teardownf)
def test_sin_values_float():
	"Test for a real float argument"
	assert_almost_equals(math.sin(.4), sin(.4), places=4)

@with_setup(setupf, teardownf)
def test_sin_values_zero():
	"Test for a zero-valued argument"
	assert_almost_equals(math.sin(0), sin(0), places=4)

@with_setup(setupf, teardownf)
def test_sin_values_negative():
	"Test for a negative-valued argument"
	assert_almost_equals(math.sin(-.4), sin(-.4), places=4)
	assert_almost_equals(math.sin(-4), sin(-4), places=4)

@with_setup(setupf, teardownf)
def test_sin_values_imaginary_int():
	"Test for an imaginary integer argument"
	assert_raises(ValueError, sin, 4j)

@with_setup(setupf, teardownf)
def test_sin_values_imaginary():
	"Test for an imaginary float argument"
	assert_raises(ValueError, sin, .4*1j)

@with_setup(setupf, teardownf)
def test_sin_values_complex():
	"Test for a complex argument"
	assert_raises(ValueError, sin, .3+.4*1j)
	assert_raises(ValueError, sin, 3+4*1j)

@with_setup(setupf, teardownf)
def test_sin_values_complex_negative():
	"Test for a complex argument"
	assert_raises(ValueError, sin, -.3-.4*1j)
	assert_raises(ValueError, sin, -3-4*1j)
```

we have done more than one assertions for some cases, for the completeness of covering possibilities of that case. this way, if a specific sub-case fails, it's not hard to isolate it, yet we're not over-creating too-many unmanageable test-cases.

selecting, ordering and sub-case testing for test cases is a subjective matter. it depends on the fine balancing between completeness and redundant bloat of test cases. we need to utilise our knowledge of the testee functionality to make good decisions

also, unit tests are not usually ultra-complete in their coverage of all possible cases because of human errors, imagination and variation of interest. if we still encounter bugs that escape the unit tests, we must add them to the list of tests for future use.

i'm sure my understanding, interpretation and presentation of the subject matter is incomplete and error-prone. i'm open for discussion and corrections :)

// class method tests [todo]