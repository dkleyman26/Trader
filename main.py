from CompanyList import CompanyListManager
from APIManager import APIManager
import pandas
import numpy
import matplotlib.pyplot as plt

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
		display_values.append(key)

		# inner loop to iterate through inner dicts to get information (open price, close price, etc)
		for key, val in val.items():
			display_keys.append(key[3::].title()) # make the column names look like titles and strip off first 3 chars (1. open, 2. close, etc)
			display_values.append(val)
		
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
	api = APIManager()

	# company list fetch returns a Dataframe
	companies = CLM.get_company_list()

	# print("""
	# Welcome to Trader. You can search 8 different time periods for any IPOed company of your choice.
	# """)

	# company = input('Enter a company abbreviation: ')
	
	while True:

		print('What would you like to see?')
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
			response = api.get_stock_info('AAPL', selection, time_interval)
		else:
			time_interval = None
			response = api.get_stock_info('AAPL', selection, None)

		data_frame = generate_df(response, selection, time_interval)
		print(data_frame)

if __name__ == '__main__':
	main()	


