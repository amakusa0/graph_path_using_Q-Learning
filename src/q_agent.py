import numpy as np
import random


class Q_AGENT:
	def __init__(self, eps=0.3):
		self.eps = eps
		self.action_before = -1
		self.state_before = -1
	
	def reset(self):
		self.action_before = -1
		self.state_before = -1
	
	def save_state_action(self, state, action):
		self.state_before = state
		self.action_before = action
	
	def action(self, q_table, state, actions, isTrain):
		if random.random() < self.eps and isTrain:
			action = random.sample(actions, 1)[0]
		else:
			q_val = []
			for action in actions:
				q_val.append(q_table.ref(state, action))
			
			q_val_max = max(q_val)	# max(q_val)が複数のindexである場合は，その中からランダムで選択 
			best_actions = []
			for i,v in enumerate(q_val):
				if q_val_max==v:
					best_actions.append(actions[i])
			action = random.sample(best_actions, 1)[0]
		self.save_state_action(state, action)
		return action
