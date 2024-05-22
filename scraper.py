print("Born Again !!!")

import urllib
from bs4 import BeautifulSoup
import requests

url = "https://www.naukri.com/jobapi/v3/search?"
header = {'noOfResults' : '20' , 'urlType' : 'search_by_keyword', 'keyword' :'python' ,'pageNo' :'1' , 'k' : 'python', 'seoKey': 'python-jobs', 'src': 'jobsearchDesk'}

print(header)
result = requests.get(url , headers=header).json()

print(result)