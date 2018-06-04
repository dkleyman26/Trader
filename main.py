from CompanyList import CompanyListManager
from APIManager import APIManager
import pandas
import numpy

def main():
	# company list manager
	CLM = CompanyListManager.CompanyListManager()

	# company list fetch returns a Dataframe
	companies = CLM.get_company_list()

	# api manager
	api = APIManager()
	







if __name__ == '__main__':
	main()	





		# FUNCTIONS = ('TIME_SERIES_INTRADAY', 'TIME_SERIES_DAILY', 'TIME_SERIES_DAILY_ADJUSTED', 'TIME_SERIES_WEEKLY','TIME_SERIES_WEEKLY_ADJUSTED', 'TIME_SERIES_MONTHLY', 'TIME_SERIES_MONTHLY_ADJUSTED', 'BATCH_STOCK_QUOTES')


		# stock = api.get_stock_info('AAPL', 2, None)