"""
File: weather_master.py
Name:Yin Jun (Ingrid) Zeng
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

EXIT = -100


def main():
	"""
	This function will continually ask user for input.
	It ends when the user enter the EXIT number.
	Users will find out the highest temperature and the lowest temperature, calculate average temperature,
	count number of days that colder then 16 degree of temperature from all inputted data.
	"""
	print('stanCode \"Weather Master 4.0\"!')
	n = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
	total = n  # Total of all input data
	c = 1  # Counting number of data inputted
	if n < 16:  # Counting number of data that under 16
		c_cold_days = 1
	else:
		c_cold_days = 0
	maximum = n  # Highest temperature
	minimum = n  # Lowest temperature
	if n == EXIT:
		print('No temperatures were entered.')  # No data inputted
	else:
		while True:
			n = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
			if n == EXIT:
				break
			elif n > maximum:
				total += n
				maximum = n
				c += 1
				if n < 16:
					c_cold_days += 1
			elif n < maximum:
				total += n
				minimum = n
				c += 1
				if n < 16:
					c_cold_days += 1
		print('Highest temperature = ' + str(maximum))
		print('Lowest temperature = ' + str(minimum))
		print('Average = ' + str(total/c))
		print(str(c_cold_days) + ' cold day(s)')


if __name__ == "__main__":
	main()
