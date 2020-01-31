import sys
import os
import pickle
from .q_table import Q_TABLE


def load_input(dirname):
	"""
	'input.txt' ファイルの読み込み．
	return
		[N, M, START_NODE, GOOL_NODE, R, G]
	"""

	file_name = './save/'+dirname+'/input.txt'
	with open(file_name, mode='r') as f:
		for i,s_line in enumerate(f):
			if i==0:
				N, START_NODE, GOOL_NODE = map(int, s_line.split())
				START_NODE -= 1
				GOOL_NODE -= 1
				G = [[] for _ in range(N)]
			elif i==1:
				R = [float(x) for x in s_line.split()]
			else:
				a,b = map(lambda x: int(x)-1, s_line.split())
				G[a].append(b)


	return [N, START_NODE, GOOL_NODE, R, G]



def load_qtable(dirname):
	"""
	q_table を読み込む
	"""
	table = {}
	epoch = 0
	q_table_path = './save/'+dirname+'/q_table.pickle'
	if os.path.isfile(q_table_path):
		with open(q_table_path, mode='rb') as f:
			epoch, table = pickle.load(f)

	return epoch, Q_TABLE(table=table)


def save_qtable(dirname, epoch, q_table):
	"""
	q_table を保存する．
	"""
	with open('./save/'+dirname+'/q_table.pickle', mode='wb') as f:
		pickle.dump([epoch, q_table.table], f)
