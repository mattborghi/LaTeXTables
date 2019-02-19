from pytexit import py2tex


def main():
	equation = 'x = 2*sqrt(2*pi*k*T_e/m_e)*(DeltaE/(k*T_e))**2*a_0**2'
	sth = py2tex(equation)
	print("The old equation is: %s" % equation)
	print("The new one is: %s" % sth)


if __name__ == '__main__':
	main()

