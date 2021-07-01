
import ast
from bs4 import BeautifulSoup
import requests
import json

def make_dictionary(soup):
    lib = {}
    title = soup.find('title')
    lib['Pekerjaan']=title.text #jobtitle
    see = soup.findAll('span', attrs={'class': 'FYwKg _1GAuD C6ZIU_1 _6ufcS_1 _27Shq_1 _2CELK_1 _2WTa0_1'})
    lib['Perusahaan']=see[2].text #company
    see_also_section = soup.findAll('span', attrs={'class': 'FYwKg _1GAuD C6ZIU_1 _6ufcS_1 _27Shq_1 _29m7__1'})
    lib['text']=see_also_section[8].text #salary
    lib['Tempat']=see_also_section[7].text #place
    lib['jobdesc']=see_also_section[-2].text #jobdesc
    lib['about']=see_also_section[-1].text #about
    one = soup.findAll('span', attrs={'class': 'FYwKg _1GAuD C6ZIU_1 _6ufcS_1 _27Shq_1 sQuda_1 _2WTa0_1'})
    two = soup.findAll('span', attrs={'class': 'FYwKg _1GAuD C6ZIU_1 _6ufcS_1 _27Shq_1 _29m7__1 _2WTa0_1'})
    item ={}
    try:
        item = {one[0].text:two[0].text, 
                one[1].text:two[1].text,
                one[2].text:two[2].text,
                one[3].text:two[3].text,
                one[4].text:two[4].text,
                one[5].text:two[5].text,
                one[6].text:two[6].text,
                one[7].text:two[7].text}
        kamus = {**lib, **item}
        return kamus
    except:
        pass
    

a_list = [] 
with open('file8.txt', 'r') as f:
    mylist = ast.literal_eval(f.read())

print("Job Start")
num = 0
for link in mylist:
    html_doc = requests.get(link).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    try:
        kamus=make_dictionary(soup)
        dictionary_copy = kamus.copy()
        a_list.append(dictionary_copy)
    except:
        pass
    num +=1
    print(num)


with open('jobstreet-6.json', 'w') as fp:
    json.dump(a_list, fp)
print("Job Finished")