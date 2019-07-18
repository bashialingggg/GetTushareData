import tushare as ts
import pandas as pd
#获取api
ts.set_token('a1b8fca80c8d74d07a0225147bcd79e6a96163bd2f9f370a9914adf8')
pro = ts.pro_api()
pd.set_option('display.max_columns',1000)
df = pro.bo_daily(date='20190211')
#df = df[df['rank']<=8]
df.rename(columns = {'data':'日期','name':'影片名称'
        ,'avg_price':'平均票价','day_amount':'当日票房（万）','total':'累计票房（万）'
        ,'list_day':'上映天数','p_pc':'场均人次','wom_index':'口碑指数','up_ratio':'环比变化 （%）','rank':'排名'},inplace=True)
#df.to_csv(r'/Users/xiesimao/py/tusharedata/moviedata/bo_daily_{}.csv'.format('20190210'),sep=',',index=False,encoding='utf_8_sig')
print(df)
'''
date	str	Y	日期
name	str	Y	影片名称
avg_price	float	Y	平均票价
day_amount	float	Y	当日票房（万）
total	float	Y	累计票房（万）
list_day	int	Y	上映天数
p_pc	int	Y	场均人次
wom_index	float	Y	口碑指数
up_ratio	float	Y	环比变化 （%）
rank	int	Y	排名'''