import numpy as np
import random
import pickle

class Q_TABLE:
	def __init__(self, table=None):
		if table==None:
			self.table = {}
		else:
			self.table = table

	def to_list(self, x):
		if isinstance(x, int):
			x = [x]
		elif isinstance(x, tuple):
			x = list(x)
		elif isinstance(x, np.ndarray):
			x = list(x.rehsape(-1))
		return x

	def join_state_action(self, state, action):
		state = self.to_list(state)
		action = self.to_list(action)
		return tuple(state+action)

	def ref(self, state, action):
		state_action = self.join_state_action(state, action)
		if state_action not in self.table:
			return 0
		else:
			return self.table[state_action]

	def ins(self, state, action, q_val):
		state_action = self.join_state_action(state, action)
		self.table[state_action] = q_val

