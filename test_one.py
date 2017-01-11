from one import sin, cos, tan
from nose.tools import *
import math


def setupf():
	"Set up the instance for testing"
	pass

def teardownf():
	"Tear down the instance"
	pass

# sin

# @with_setup(setupf, teardownf)
# def test_sin_values():
# 	for x in [-2, -.1, 0, .1, 2]:
# 		yield check_sin_values, x
# 	for x in [(-2, 0), (-.1, 0), (0, 0), (.1, 0), (2, 0)]:
# 		yield check_sin_values_complex, x
# 	for x in [(-2, -2), (-.1, -.1), (0, 0), (.1, .1), (2, 2)]:
# 		yield check_sin_values_complex, x

# def check_sin_values(x):
# 	"Test for a valid float argument"
# 	assert_almost_equals(math.sin(x), sin(x), places=4)

# def check_sin_values_complex(x):
# 	"Test for an exception on complex float argument"
# 	p, q = x
# 	assert_raises(ValueError, sin, p+complex(0,q))

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