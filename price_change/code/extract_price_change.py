
import os
import json
import time
import collections
import datetime
from datetime import timedelta
# from DataFrame import DataFrame
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
import pandas as pd
import numpy as np



def plot_lines(x1,y1):

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
	ax.plot(x1, y1, '-', linewidth=4, markersize=10, color=colors[2], marker=Markers[0])
	# ax.plot(x2, y2, '-', linewidth=4, markersize=10, color=colors[1], label='batch 320', marker=Markers[1])
	# ax.plot(x3, y3, '-', linewidth=4, markersize=10, color=colors[2], label='batch 3200', marker=Markers[2])
	# ax.plot(x4, y4, '-', linewidth=4, markersize=10, color=colors[3], label='batch 32000', marker=Markers[3])
	# ax.plot(x5, y5, '-', linewidth=4, markersize=10, color=colors[4], label='full dataset', marker=Markers[4])
	plt.ylim([0, 1])
	plt.ylabel('projects price ratio change', fontsize=20)
	plt.xlabel('price:(0.001-10000)', fontsize=20)
	plt.legend(loc='lower right', fontsize=18)
	plt.grid(True)
	plt.axis('tight')
	#ax.set_xticks(np.arange(0,21,5))
	ax.tick_params(axis='x', labelsize=18)
	ax.tick_params(axis='y', labelsize=18)
	# plt.title('FP (eps=0.5) Varying Batch Size Task'+'0',fontsize=22)
	fig.savefig('../projects_price'+'0'+'.pdf', format='PDF', bbox_inches='tight')
	plt.gcf().autofmt_xdate()
	# plt.gca().locator_params('x',nbins = 6)
	# plt.locator_params("x", nbins = 2)

	plt.show()
# from pylab import *
# ico_date_maping = { } # 存放{日期-公司}对，同一日期若存在多个公司则存为list

def stamp_to_date(date_stamp):
	time_string = time.localtime(date_stamp)
	# print(time_string)
	date_ = time.strftime("%Y-%m-%d", time_string)
	# year = int( date_.split('-')[0] )
	# month =int( date_.split('-')[1] )
	# date = year + month
	# day =int( date_.split('-')[2] )
	# day = 1
	# if year<2000: # 2000年以前的数据是异常值
	# 	continue
	# if year>=2018 and month >1: # 去掉201802数据
	# 	continue
	# print(year,month,day)
	# date_ = datetime.date(year =year,month = month,day = day)

	return date_


	
def load_coins_daily_price(file_path):
	# ico_date_maping = { } # 存放{日期-公司}对，同一日期若存在多个公司则存为list
	coin_daily_price = {}
	for json_file in file_path: #os.listdir():
		coin_name = json_file # json_file为货币简称
		coin_daily_price[coin_name]={} # 值为字典，(date:price)

		json_doc = '../coins/'+json_file+'/histoday.json' 
		# if not json_file.endswith("json"):
		#	 continue
		with open(json_doc,encoding ='utf-8') as f:
			jsonf = json.load(f)
			# print(jsonf.keys())
			if jsonf['Response'] != 'Success':
				continue
			for data in jsonf['Data']:
				open_price = str(data['open']) #开盘价
				# open_price = str(data['high']) #开盘价
				# open_price = str(data['low']) #开盘价
				# open_price = str(data['close']) #开盘价


				price_date_stamp = data['time'] #日期(stmp格式)
				price_date = stamp_to_date(price_date_stamp)
				# if coin_name not in coin_daily_price:
				# 	coin_daily_price[coin_name]=[]
				# print(type(open_price),type(price_date))
				coin_daily_price[coin_name][price_date] = open_price
				# coin_daily_price[coin_name].append(zip(price_date,open_price))

				# print(coin_name,price_date,open_price)
				# print(coin_daily_price[coin_name])
	return coin_daily_price

json_path = os.listdir('../coins/')
coin_daily_price = load_coins_daily_price(json_path)
# print(coin_daily_price)

# assert 1==2
def date_filter(price_dict,filter_date): # 2017您年三月之后的数据筛掉
	# filtered_dic  = {}
	# to_delete = []
	for each_coin,coin_dic in price_dict.items():
		# print(each_coin,coin_dic)
		to_delete=[]
		for date,price in coin_dic.items():
			if date > filter_date:
				to_delete.append(date)
				# del price_dict[each_coin][date] # 删除该日期
			# else:
			# 	print(date)

		for date in to_delete:
			del price_dict[each_coin][date]
	return price_dict
price_dict = date_filter(coin_daily_price,'2018-02-21')
# print("price dict:::",price_dict)
def date_selection(price_dict,time_delta): # 选择间隔为time_delta的数据
	print("lenthg: price dict::",len(price_dict))
	# print(price_dict.keys())
	count = 0
	count_with_value = 0
	init_date_dict = {}
	half_year_dic={}
	a_year_dict={}
	init_date_list = []
	half_year_list = []
	a_year_list = []
	for each_coin,coin_dic in price_dict.items(): 
		# print('count ++')# each_coin是一个dic([date:price])
		if len(coin_dic)==0:
			count = count+1
			# print('empty value + +')
			continue
		# print("check coin_dic:",each_coin,coin_dic)
		# assert 1==2
		count_with_value+=1
		# print('vaule ++')
		init_date = min(coin_dic.keys()) 
		# print("init date::",init_date)
		# if float(coin_dic[init_date]) > 10000:
		# 	print(init_date,each_coin, coin_dic[init_date])
		# print("sorted dic::",sorted(coin_dic))
		# print('min keys:',init_date)

		year = int( init_date.split('-')[0] )
		month =int( init_date.split('-')[1] )
			# date = year + month
		day =int( init_date.split('-')[2] )
			# day = 1
		# print(year,month,day)
		init_date = datetime.datetime(year =year,month = month,day = day)

		after_half_year = init_date + timedelta(days=182)
		after_a_year = init_date + timedelta(days=365)
		init_date = init_date.strftime('%Y-%m-%d')[:10]
		after_half_year =after_half_year.strftime('%Y-%m-%d')[:10]
		after_a_year = after_a_year.strftime('%Y-%m-%d')[:10]
		# print(init_date,after_half_year,after_a_year)
		# assert 1==2
		# print(init_date,after_half_year,after_a_year)
		# print('price list::',coin_dic[init_date],coin_dic[after_half_year],coin_dic[after_a_year])
			# init_date_list.append(coin_dic[init_date])
		# print(coin_dic)
		init_price = coin_dic[init_date]

		# print(coin_dic[after_half_year])
		try:
			# print(init_price,coin_dict[after_half_year])
			ratio_half = float(coin_dic[after_half_year]) / float(init_price)
			half_year_list.append(ratio_half)
			# print(init_price,after_half_year)
		except:
			pass
		try:
			ratio_year = float(coin_dic[after_a_year]) / float(init_price)
			a_year_list.append(ratio_year)
			# print(init_price,after_a_year)
			# print(each_coin)
		except:
			# print(each_coin)
			pass

		'''
		if init_date not in init_date_dict:
			init_date_dict[init_date] = []
		if after_half_year not in half_year_dic:
			half_year_dic[after_half_year] = []
		if after_a_year not in a_year_dict:
			a_year_dict[after_a_year] = []


		init_date_dict[init_date].append(coin_dic[init_date]) # date:price
		try:
			half_year_dic[after_half_year].append(coin_dic[after_half_year])
		except:

			print(each_coin)
			# print('after half year',after_half_year)
			# return
			# break
		try:
			a_year_dict[after_a_year].append(coin_dic[after_a_year])
		except:
			print(each_coin)
		'''

			# print('after a year',after_a_year)
			# print('after_a_year data::',coin_dic[after_a_year])
			# return
			# break

	return half_year_list,a_year_list
half_year_ratio,one_year_ratio = date_selection(price_dict,0)
# print('count::',count)
# print('count value:',cw)
# # assert 1==2
# print('init::\n',init) # 只有几条数据？？
# print('half:\n',half)
# print('one::',one)

def extract_xy(price_input_list): # { date:price }
	price_list = [0.001,0.2,1,10,100,10000]
	price_count = [0,0,0,0,0,0,0]
	# print("price item::",price_dict.items())
	# print(price_input_list)
	for price in price_input_list:
		# if len(price)==0:
			
		# 	# print("price::",price)
		# 	continue
		# print(price)
		price = float(price)
		# print("price is::",price)
		if price < 0:
			continue
		elif price < price_list[0]:
			price_count[0] += 1
		elif price < price_list[1]:
			price_count[1] += 1
		elif price < price_list[2]:
			price_count[2] += 1
		elif price < price_list[3]:
			price_count[3] += 1
		elif price < price_list[4]:
			price_count[4] += 1
		elif price< price_list[5]:
			price_count[5] += 1
		else:
			price_count[6] += 1
			print("the high price is:",price)
	return price_list,price_count

def plot_result(ratio_input_list):

	for i,data in enumerate(ratio_input_list):
		print("change date ing")
		price_count_all = 0

		x1,y1 = extract_xy(data)
		for cnt in y1:
			price_count_all+=cnt
		y=[]
		for cnt in y1:
			print(price_count_all)
			cnt = cnt/float(price_count_all)
			cnt = round(cnt,4)
			y.append(cnt)
		y1=y
		print('x1:',x1,'y1:',y1)

		# x1=['0.001','0.1','1','10','100','10000','100000']
		x1 = [1,2,3,4,5,6,7]
		# y1=y

		arr=[]
		arr.append(x1)
		arr.append(y1) 
		arr = np.array(arr)
		arr_df = pd.DataFrame(arr)
		arr_df.to_csv('../price_ratio_'+str(i)+'.csv')

	# def plot_curve(a):
	# 	xs = []
	# 	ys = []
	# 	for data in a:
	# 		# if time<'20000101':
	# 		# 	continue
	# 		print(data)
	# 		time=data[0]
	# 		cap=data[1][0]/data[1][1]
	# 		# print(time)
	# 		xs.append(time)
	# 		ys.append(cap)
	# 	return xs,ys
	# x1,y1 = plot_curve(a)
		
		plot_lines(x1,y1)	

plt_list = [half_year_ratio,one_year_ratio]
plot_result(plt_list)



