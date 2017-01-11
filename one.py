e = 2.71828182846

def sin(rad):
	return (e**(rad*1j)).imag

def cos(rad):
	return (e**(rad*1j)).real

def tan(rad):
	sin(rad)/cos(rad)