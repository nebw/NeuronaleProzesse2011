
import random
from math import exp

class SimpleClass(object):
	'''Proof of concept'''

	def __init__(self, param):
		self.property1 = param
		print "Setting value..." + str(self.property1) 

	def setter(self, param):
		print "Setting..."
		self.property1 = param

	def printer(self):
		print self.property1


def logSigm(x):
    return 1/(1+exp(x))
  
if __name__ == '__main__':
	x = 7
	print x, '\t', logSigm(x)
    
	y = random.random()
	print y, '\t', logSigm(y)

	myinstance = SimpleClass(7)
	myinstance.setter(5)
	myinstance.printer()
	