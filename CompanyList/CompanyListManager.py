import pandas
import numpy as np

class CompanyListManager:
	csv_data = pandas.read_csv('CompanyList/companylist.csv')

	# generate company list from csv
	def get_company_list(self):

		symbols = []
		names = []
		ipo_year = []

		for symbol, name, ipo in zip(self.csv_data['Symbol'], self.csv_data['Name'], self.csv_data['IPOyear']):
			try:
				new_ipo = int(ipo)
			except: 
				new_ipo = 0 

			# no ipo year
			if new_ipo == 0:
				continue

			symbols.append(symbol)
			names.append(name)
			ipo_year.append(new_ipo)

		# build pandas dataframe to be passed
		return pandas.DataFrame({'Symbol': symbols, 'Name': names, 'IPO Year': ipo_year})	

