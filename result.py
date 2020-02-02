import sys
import random
import numpy as np
from src.gamemaster import GAMEMASTER
from src.q_table import Q_TABLE
from src.q_agent import Q_AGENT
from src.utils import  load_input, load_qtable

def main():
	# コマンドライン引数
	args = sys.argv
	if len(args)<2:
		print('set dirname')
		print('>> main.py [dirname]')
		sys.exit()


	N, START_NODE, GOOL_NODE, R, G = load_input(args[1])
	epoch, q_table = load_qtable(args[1])
	q_agent = Q_AGENT()


	# G, Rの出力
	print('\n>> G')
	print('NODE |     R    |   g')
	for i,g in enumerate(G):
		print('%4d | %8f | '%(i+1, R[i]), g)



	# q_tableの出力
	print('\n>> q_table')
	for n, r in sorted(q_table.table.items()):
		print('%d -> %d | %f'%(n[0]+1, n[1]+1, r))


	# ルートの出力
	print('\n>> path')
	gamemaster = GAMEMASTER(q_agent, G, START_NODE, GOOL_NODE, R)
	gamemaster.start(q_table, isPrint=True, isTrain=False)

	print()

if __name__=='__main__':
	main()
