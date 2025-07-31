import requests
import os


prefix_url = 'https://github.com/inodb/datahub/raw/a0d36d77b242e32cda3175127de73805b028f595/tcga/pathology_reports'
postfix_url = '?download='
dest = './reports/'


names = open('./names.txt','r').readlines()

names = [s.replace('\n','') for s in names]

for filename in names:
    url = f'{prefix_url}/{filename}{postfix_url}'    
    newname = dest+filename.split('.')[0]+'.pdf'
    if not os.path.exists(newname):
        try:
            response = requests.get(url)
        except:
            continue
        if response.status_code == 200:
            with open(newname, "wb") as file:
                file.write(response.content)
        else:
            print(f"Error: {response.status_code}")


    