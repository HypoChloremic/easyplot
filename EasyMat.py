"""This package will attempt to simplify the process of graphing with 
matplot, automating much of the process"""


import matplotlib.pyplot as plt


class EasyPlot:
	"""This will attempt to simplify the process of making plots with 
	matplotlib """
	def __init__(self, *args, **kwargs):
		self.args = args
		self.kwargs = kwargs

		if self.args:
			if len(self.args) == 2: self.x,self.y = args
			else: pass
		
		else:
			raise ValueError



	def __enter__(self):
		self.v2 = plt.figure()
		self.variable = self.v2.add_subplot(111)

	# ty type, val value and tb traceback
	def __exit__(self, ty, val, tb):
		pass

		
if __name__ == '__main__':
			x = [1,2,3,4]
			y = [1,2,3,4]
			a = EasyPlot(x,y)
			with a:
				pass