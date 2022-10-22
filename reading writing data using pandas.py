import pandas as pd 
import numpy as np 

temp = pd.Series(28 + 10*np.random.randn(10))
print(temp.describe())
print('\n----------------------\n')
print(temp.info())

# import io
# import requests
# url="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
# s=requests.get(url).content
# c=pd.read_csv(io.StringIO(s.decode('utf-8')))

EmployeeRecords = [{'EmployeeID':451621, 'EmployeeName':'Preeti Jain', 'DOJ':'30-Aug-2008'},
{'EmployeeID':123621, 'EmployeeName':'Ashok Kumar', 'DOJ':'25-Sep-2016'},
{'EmployeeID':451589, 'EmployeeName':'Johnty Rhodes', 'DOJ':'04-Nov-2016'}]

import json
emp_records_json_str = json.dumps(EmployeeRecords)
df = pd.read_json(emp_records_json_str, orient='records', convert_dates=['DOJ'])
print(df)





