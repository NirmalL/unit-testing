e = 2.71828182846

def sin(rad):
	if isinstance(rad, complex):
		raise ValueError('sin(x) requires real arguments.') 
	return (e**(rad*1j)).imag

def cos(rad):
	return (e**(rad*1j)).real

def tan(rad):
	return sin(rad)/cos(rad)

# quick tests
# print sin(1+2j)
# print sin(1)
# print isinstance(1+2j, complex)