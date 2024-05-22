print("Born Again !!!")

import urllib
import requests

def get_jobs_data():

    url = "https://www.google.co.in"
    url2 =  "https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_keyword&searchType=adv&keyword=python&pageNo=1&k=python&seoKey=python-jobs&src=jobsearchDesk&latLong=27.885568_78.0763136"
    param = {'noOfResults' : '20' , 'urlType' : 'search_by_keyword', 'keyword' :'python' ,'pageNo' :'1' , 'k' : 'python', 'seoKey': 'python-jobs', 'src': 'jobsearchDesk'}
    header = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246", 'appid' :'109', 'systemid':'Naukri'} 

    try:
        result = requests.get(url2, headers=header, params=param).json()
        return (result)
    except Exception as e:
        return e