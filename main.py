from CompanyList import CompanyListManager
from APIManager import APIManager
from PlotManager import PlotManager
import pandas
import numpy

def generate_df(response, selection, interval):
	# generate empty dataframe
	data_frame = pandas.DataFrame([])

	# selection is passed as a string
	sel = int(selection)
	
	if sel == 1: # see if the selection was 1 with an interval being passed
		key = APIManager.RESPONSE_KEYS[0] + " (" + interval + "min)"
	elif sel == 2 or sel == 3: # see if the selection was 2 or 3 as they have the same key in response
		key = APIManager.RESPONSE_KEYS[1] 
	else:
		key = APIManager.RESPONSE_KEYS[sel - 2] # else select one of the RESPONSE_KEYS based on what position its in the list (sel - 2 maps to the correct RESPONSE_KEYSS)
	
	# lists to be passed to dataframe
	display_keys = []
	display_values = []

	# iterate through outer dict to extract dates (and times)
	for key, val in response[key].items():
		display_keys.append('Date (and Time)')
		key = key.replace('-', '/')
		display_values.append(key)

		# inner loop to iterate through inner dicts to get information (open price, close price, etc)
		for key, val in val.items():
			display_keys.append(key[3::].title()) # make the column names look like titles and strip off first 3 chars (1. open, 2. close, etc)
			display_values.append(float(val)) # number values
		
		# generate temp dataframe and append the current extracted values
		temp_df = pandas.DataFrame([display_values], columns=list(display_keys))
		data_frame = data_frame.append(temp_df, ignore_index=True)

		# clear lists
		display_keys = []
		display_values = []

	return data_frame

	

def main():
	# company list manager
	CLM = CompanyListManager.CompanyListManager()

	# api manager
	API = APIManager()

	# company list fetch returns a Dataframe
	companies = CLM.get_company_list()
	# print(companies)

	# print("""
	# Welcome to Trader. You can search 8 different time periods for any IPOed company of your choice.
	# """)

	company = input('Enter a company abbreviation: ')
	
	while True:

		print('\nWhat would you like to see about {}?'.format(company))
		print('1. Intradaily time series')
		print('2. Daily time series')
		print('3. Daily time series adjusted')
		print('4. Weekly time series')
		print('5. Weekly time series adjusted')
		print('6. Monthly time series')
		print('7. Monthly time series adjusted')
		#print('8. Batch stock quotes')

		selection = int(input('\n-----> '))

		if selection == 1:
			time_interval = input('What time interval do you want to see (Enter 1, 5, 15, 30, 60): ')
			response = API.get_stock_info(company, selection, time_interval)
		else:
			time_interval = None
			response = API.get_stock_info(company, selection, None)

		data_frame = generate_df(response, selection, time_interval)
		#print(data_frame)

		# plot manager with dataframe
		PLOT = PlotManager(data_frame)

		point = input("What would you like to see a graph of? (Enter 'o' for open, 'h' for high, 'l' for low, 'c' for close, 'v' for volume): ")
		time_start = input('Enter a time to start: ')
		time_end = input('Enter the time to end: ')

		PLOT.plot(point, 0, 12)
		
		



# run main
if __name__ == '__main__':
	main()	


