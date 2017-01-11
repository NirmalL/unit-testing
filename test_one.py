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

@with_setup(setupf, teardownf)
def test_sin_values():
	for x in [-2, -.1, 0, .1, 2]:
		yield check_sin_values, x
	for x in [(-2, -2), (-.1, -.1), (0, 0), (.1, .1), (2, 2)]:
		yield check_sin_values_imag, x

def check_sin_values(x):
	"Test for a valid float argument"
	assert_almost_equals(math.sin(.1), sin(.1), places=4)

def check_sin_values_imag(x):
	"Test for a valid imaginary float argument"
	p, q = x
	assert_almost_equals(math.sin(complex(p, q)), sin(complex(p, q)), places=4)