'''
@auther: shipeng
@contact: peng_shi@shannonai.com 

@version: 1.0
@time: 2018.03.03
handle coins price change ratio 
'''

import os
import json
import time
import datetime
import numpy as np
import pandas as pd
from plot_curve import plotCurve

class handleCoinSpider(object):
	def __init__(self,path,date,days1,days2):
		# self.name='hello_spider'
		self.json_path = path #os.listdir('../coins/') #json文件目录
		self.date_fil = date #'2018-02-21' #删选date_fil之前的数据
		self.day_interval_1 = days1 #182 # 间隔为半年
		self.day_interval_2 = days2 #365 # 间隔为一年
	def extract_squence(self):
		coin_daily_price_dic = self.load_coins_daily_price(self.json_path)
		price_dict = self.date_filter(coin_daily_price_dic,self.date_fil)
		half_year_ratio,one_year_ratio = self.date_selection(price_dict,self.day_interval_1,self.day_interval_2)
		plt_list = [half_year_ratio,one_year_ratio]
		self.plot_result(plt_list)
	def plot_(self,x1,y1):
		plc = plotCurve(x1,y1)
		plc.plot_lines()
	def stamp_to_date(self,date_stamp):
		time_string = time.localtime(date_stamp)
		date_string = time.strftime("%Y-%m-%d", time_string)
		return date_string
	def load_coins_daily_price(self,file_path):
		coin_daily_price = {}
		for json_file in file_path: #os.listdir():
			coin_name = json_file # json_file为货币简称
			coin_daily_price[coin_name]={} # 值为字典，(date:price)
			json_doc = '../coins/'+json_file+'/histoday.json' 
			with open(json_doc,encoding ='utf-8') as f:
				jsonf = json.load(f)
				if jsonf['Response'] != 'Success':
					continue
				for data in jsonf['Data']:
					open_price = str(data['open']) #开盘价
					price_date_stamp = data['time'] #日期(stmp格式)
					price_date = self.stamp_to_date(price_date_stamp)
					coin_daily_price[coin_name][price_date] = open_price
		return coin_daily_price
	def date_filter(self,price_dict,filter_date): # 2017您年三月之后的数据筛掉
		for each_coin,coin_dic in price_dict.items():
			to_delete=[]
			for date,price in coin_dic.items():
				if date > filter_date:
					to_delete.append(date)
			for date in to_delete:
				del price_dict[each_coin][date]
		return price_dict
	def date_selection(self,price_dict,time_delta_1,time_delta_2): # 选择间隔为time_delta的数据
		# print("lenthg: price dict::",len(price_dict))
		init_date_list = []
		half_year_list = []
		a_year_list = []
		for each_coin,coin_dic in price_dict.items(): 
			if len(coin_dic)==0:
				continue
			init_date = min(coin_dic.keys()) 
			year = int( init_date.split('-')[0] )
			month = int( init_date.split('-')[1] )
			day = int( init_date.split('-')[2] )
			init_date = datetime.datetime(year =year,month = month,day = day)
			after_half_year = init_date + datetime.timedelta(days=time_delta_1)
			after_a_year = init_date + datetime.timedelta(days=time_delta_2)
			init_date = init_date.strftime('%Y-%m-%d')[:10]
			after_half_year =after_half_year.strftime('%Y-%m-%d')[:10]
			after_a_year = after_a_year.strftime('%Y-%m-%d')[:10]
			init_price = coin_dic[init_date]
			try: # 半/一年后的数据字典的key可能为空（发币日期过晚，没有半年数据）
				ratio_half = float(coin_dic[after_half_year]) / float(init_price)
				half_year_list.append(ratio_half)
			except:
				pass
			try:
				ratio_year = float(coin_dic[after_a_year]) / float(init_price)
				a_year_list.append(ratio_year)
			except:
				pass
		return half_year_list,a_year_list
	def extract_xy(self,price_input_list): # { date:price }
		price_list = [0.001,0.2,1,10,100,10000]
		price_count = [0,0,0,0,0,0,0]
		for price in price_input_list:
			price = float(price)
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
	def plot_result(self,ratio_input_list):
		for i,data in enumerate(ratio_input_list):
			# print("change date ing")
			price_count_all = 0
			y_ratio_list=[]
			result_list=[]
			x_range,y_coins_count = self.extract_xy(data)
			for cnt in y_coins_count:
				price_count_all+=cnt
			for cnt in y_coins_count:
				# print(price_count_all)
				cnt = cnt/float(price_count_all)
				cnt = round(cnt,4)
				y_ratio_list.append(cnt)
			print('x1:',x_range,'y1:',y_ratio_list)
			x1 = [1,2,3,4,5,6,7]
			y1 = y_ratio_list
			self.plot_(x1,y1)	 # plot
			result_list.append(x_range)
			result_list.append(y_ratio_list) 
			result_arr = np.array(result_list)
			result_df = pd.DataFrame(result_arr)
			result_df.to_csv('../doc/price_ratio_'+str(i)+'.csv')

if __name__ == '__main__':
	json_file_path = os.listdir('../coins/')
	filter_date = '2018-02-21' #筛选该日期之前的数据
	day_delta_1 = 182 # 半年的价格比
	day_delta_2 = 365# 一年的价格比
	hcs = handleCoinSpider(json_file_path,filter_date,day_delta_1,day_delta_2)
	hcs.extract_squence()
	


