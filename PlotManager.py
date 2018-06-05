import matplotlib.pyplot as plt

class PlotManager: 

	data_frames = []

	def __init__(self, data_frame):
		self.data_frames.append(data_frame)
	
	def plot(self, point, time_start, time_end):
		for i in range(0, len(self.data_frames)):
			if point == 'o':
				data = self.data_frames[i]['Open']
			elif point == 'h':
				data = self.data_frames[i]['High']
			elif point == 'l':
				data = self.data_frames[i]['Low']
			elif point == 'c':
				data = self.data_frames[i]['Close']
			elif point == 'v':
				data = self.data_frames[i]['Volume']		

		data = data[time_start + 1:time_end + 1]
		delta_time = list(range(time_start, time_end)) # must use list() because need to convert it to be an iterator

		# plot data
		plt.plot(delta_time, data)
		plt.xticks([12, 24, 36, 48, 48+24])		
		plt.show()	

	def add_additional_frame(self, data_frame):
		self.data_frames.append(data_frame)