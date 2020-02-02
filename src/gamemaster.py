import numpy as np

class GAMEMASTER:
	def __init__(self, q_agent, G, start_node, gool_node, R, alpha=0.1, gamma=0.9, search_limit=10**5):
		self.q_agent = q_agent
		self.G = G
		self.start_node = start_node
		self.gool_node = gool_node
		self.R = R
		self.alpha = 0.1
		self.gamma = 0.9
		self.search_limit=search_limit

	def reset(self):
		self.state = self.start_node
		self.q_agent.reset()

	def cal_reward(self):
		return self.R[self.state]

	def isfinish(self):
		if self.state==self.gool_node:
			return True
		else:
			return False


	def update_q_table(self,q_table):
		if self.q_agent.state_before==-1:
			return
		actions = self.G[self.state]
		if len(actions)==0:
			s = 0
		else:
			t = []
			for action in actions:
				t.append(q_table.ref(self.state, action))
			s = max(t)

		q_val = (1-self.alpha)*q_table.ref(self.q_agent.state_before, self.q_agent.action_before) + self.alpha*(self.cal_reward() + self.gamma*s)
		q_table.ins(self.q_agent.state_before, self.q_agent.action_before, q_val)
		return


	def start(self, q_table, isPrint=True, isTrain=True):
		self.reset()
		cnt = 0
		while True:
			if self.isfinish():
				if isTrain:
					self.update_q_table(q_table)
				if isPrint:
					print(self.state+1)
				return

			if isPrint:
				print(self.state+1, '->',end='')

			if isTrain:
				self.update_q_table(q_table)

			if cnt>self.search_limit:
				print('\n\n < Iter search is over %d > \n' %(self.search_limit))
				return

			self.state = self.q_agent.action(q_table, self.state, self.G[self.state], isTrain=isTrain)

			cnt += 1
