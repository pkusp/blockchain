import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style

class plotCurve(object):
	def __init__(self,x,y):
		self.name = 'plotCurve'
		self.x1 = x
		self.y1 = y
	def plot_lines(self):
		# x1=self.x1
		# y1=self.y1
		# import numpy as np
		# import matplotlib.pyplot as plt

		# Tasks=["2","3","4","6"]
		# for task in Tasks:
		colors=["red","green","blue","black","orange","grey","purple","saddlebrown","maroon","tomato"]
		Markers=["o","^","s","p","D","v","*","<","+",">"]
		fig, ax = plt.subplots()
		# nupdates = 93587 / 32


		# file1 = open('task'+task+'_modelFP_sbsz32_mbsz32_lr0.2_decay1_decint1000_thr50_allcandn_eps0.5balancenNhop1.result',"r")
		# file2 = open('task'+task+'_modelFP_sbsz320_mbsz32_lr0.2_decay1_decint1000_thr50_allcandn_eps0.5balancenNhop1.result',"r")
		# file3 = open('task'+task+'_modelFP_sbsz3200_mbsz32_lr0.2_decay1_decint1000_thr50_allcandn_eps0.5balancenNhop1.result',"r")
		# file4 = open('task'+task+'_modelFP_sbsz32000_mbsz32_lr0.2_decay1_decint1000_thr50_allcandn_eps0.5balancenNhop1.result',"r")
		# file5 = open('task'+task+'_modelFP_sbsz93568_mbsz32_lr0.2_decay1_decint1000_thr50_allcandn_eps0.5balancenNhop1.result',"r")
				
		# lines1 = file1.readlines()
		# data1 = np.loadtxt(lines1)
		# lines2 = file2.readlines()
		# data2 = np.loadtxt(lines2)
		# lines3 = file3.readlines()
		# data3 = np.loadtxt(lines3)
		# lines4 = file4.readlines()
		# data4 = np.loadtxt(lines4)
		# lines5 = file5.readlines()
		# data5 = np.loadtxt(lines5)
		# fig, ax = plt.subplots()
		# x1 = data1[3:122:4,0] / (1.0 * nupdates)
		# y1 = data1[3:122:4,1]
		# x2 = data2[3:122:4,0] / (1.0 * nupdates)
		# y2 = data2[3:122:4,1]
		# x3 = data3[3:122:4,0] / (1.0 * nupdates)
		# y3 = data3[3:122:4,1]
		# x4 = data4[3:122:4,0] / (1.0 * nupdates)
		# y4 = data4[3:122:4,1]
		# x5 = data5[3:122:4,0] / (1.0 * nupdates)
		# y5 = data5[3:122:4,1]
		ax.plot(self.x1, self.y1, '-', linewidth=4, markersize=10, color=colors[2], marker=Markers[0])
		# ax.plot(x2, y2, '-', linewidth=4, markersize=10, color=colors[1], label='batch 320', marker=Markers[1])
		# ax.plot(x3, y3, '-', linewidth=4, markersize=10, color=colors[2], label='batch 3200', marker=Markers[2])
		# ax.plot(x4, y4, '-', linewidth=4, markersize=10, color=colors[3], label='batch 32000', marker=Markers[3])
		# ax.plot(x5, y5, '-', linewidth=4, markersize=10, color=colors[4], label='full dataset', marker=Markers[4])
		# plt.ylim([0, 1])
		plt.ylabel('projects price ratio change', fontsize=20)
		plt.xlabel('price:(0.001-10000)', fontsize=20)
		plt.legend(loc='lower right', fontsize=18)
		plt.grid(True)
		plt.axis('tight')
		#ax.set_xticks(np.arange(0,21,5))
		ax.tick_params(axis='x', labelsize=18)
		ax.tick_params(axis='y', labelsize=18)
		# plt.title('FP (eps=0.5) Varying Batch Size Task'+'0',fontsize=22)
		fig.savefig('../doc/projects_price'+'0'+'.pdf', format='PDF', bbox_inches='tight')
		plt.gcf().autofmt_xdate()
		# plt.gca().locator_params('x',nbins = 6)
		# plt.locator_params("x", nbins = 2)
		plt.show()

if __name__ == '__main__':
	x=[1,2,3,4]
	y=[2,3,2,3]
	plc = plotCurve(x,y)
	plc.plot_lines()

