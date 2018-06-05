import requests
import json

class APIManager:

	# url builders
	API_KEY = 'apikey=RV3BY4C59I6A7BNV'
	API_BASE = 'https://www.alphavantage.co/query?'

	# functions to be used in url
	FUNCTIONS = ('TIME_SERIES_INTRADAY', 'TIME_SERIES_DAILY', 'TIME_SERIES_DAILY_ADJUSTED', 'TIME_SERIES_WEEKLY','TIME_SERIES_WEEKLY_ADJUSTED', 'TIME_SERIES_MONTHLY', 'TIME_SERIES_MONTHLY_ADJUSTED', 'BATCH_STOCK_QUOTES')

	# api response has different keys corresponding to different api calls
	RESPONSE_KEYS = ("Time Series", "Time Series (Daily)", "Weekly Time Series", "Weekly Adjusted Time Series", "Monthly Time Series", "Monthly Adjusted Time Series", "Stock Quotes" )

	# private function to build url
	def __build_url(self, function, symbol, interval, output_size):
		if interval == None: # check if request is intradaily request
			return self.API_BASE + function + '&' + symbol + '&' + self.API_OUTPUT_SIZE + '&' + self.API_KEY
		else:
			return self.API_BASE + function + '&' + symbol + '&' + interval + '&' + self.API_OUTPUT_SIZE + '&' + self.API_KEY

	# fetch the url and check for erros
	def __fetch(self, url):
		# get response
		response = requests.get(url)

		if response.status_code == 200: # SUCCESS
			return json.loads(response.content.decode('utf-8'))
		elif response.status_code == 400: 
			print('FETCH ERROR')
		elif response.status_code == 500:
			print('FETCH ERROR')		

	# intradaily takes an interval so the interval param is a int either 1, 5, 15, 30 or 60
	# call gets an integer as a function param and integer or None as interval param
	def get_stock_info(self, symbol, function, interval):
		self.API_FUNCTION = 'function=' + self.FUNCTIONS[function - 1] # 0 is the first intradaily request function
		self.API_SYMBOL = 'symbols=' + symbol if function == 8 else 'symbol=' + symbol # for batch quotes symbols= is needed
		self.API_INTERVAL = None if interval is None else 'interval=' + str(interval) + 'min' # None should be passed if interval isnt needed

		# get input if the user would like to see the full or shortned list (only works for intradaily and daily)
		list_size = 'f' # start with full list
		if function <= 3:
			list_size = input("Type 'c' for a compact list of only 100 inputs, or press any other key to see the full list: ") 
		self.API_OUTPUT_SIZE = 'outputsize=compact' if list_size is 'c' else 'outputsize=full'

		# build and return url
		url = self.__build_url(self.API_FUNCTION, self.API_SYMBOL, self.API_INTERVAL, self.API_OUTPUT_SIZE)
		print(url)
		return self.__fetch(url)
