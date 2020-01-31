import sys
from tqdm import tqdm
from src.gamemaster import GAMEMASTER
from src.q_table import Q_TABLE
from src.q_agent import Q_AGENT
from src.utils import  load_input, load_qtable, save_qtable



# コマンドライン引数
args = sys.argv
if len(args)<3:
	print('set dirname and epoch')
	print('>> train.py [dirname] [epoch]')
	sys.exit()

epoch = int(float(args[2]))


N, START_NODE, GOOL_NODE, R, G = load_input(args[1])
already_learned_epoch, q_table = load_qtable(args[1])
print('epoch already:  %d'%already_learned_epoch)


# 学習
q_agent = Q_AGENT()
gamemaster = GAMEMASTER(q_agent, G, START_NODE, GOOL_NODE, R)
for i in tqdm(range(epoch)):
	# epoch数が増えると，q_tableが大きくなる．1epochの計算時間が長くなる．
	# プログレスバーはあくまで目安．
	gamemaster.start(q_table, isPrint=False, isTrain=True)


#q_tableの保存
save_qtable(args[1], epoch + already_learned_epoch, q_table)


print('epoch finish: %d'%(already_learned_epoch+epoch))
