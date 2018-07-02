measure_tasks = ['I', 'Z0', 'Z1', 'Z0Z1', 'X0X1', 'Y0Y1']

MIN_R = 0.7
MAX_R = 0.7

SHOTS = 1024

THETAS = 10

IBM_BACKEND = True

from math import pi

thetas = []
for i in range(THETAS):
	thetas.append(i * 2.0 * pi / THETAS)

class Atom_config:
	def __init__(self, r, coefs):
		self.r = r
		self.coefs = coefs