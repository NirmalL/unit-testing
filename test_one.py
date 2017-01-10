import datetime

class Formatter:
	def format_date(self, inp, outp):
		return datetime.datetime.strptime('10/05/2012', '%d/%m/%Y').strftime('%Y-%m-%d')


def test():
	instance = Formatter()
	try:
		var = instance.format_date()
		
	finally:
		pass