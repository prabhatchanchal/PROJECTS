import requests as rq 
from bs4 import BeautifulSoup
data = None
with open('password_dump.txt') as file:
	data = file.read()
names = [i.split(':')[0] for i in data.split('\n')]
hashes = [i.split(':')[1] for i in data.split('\n')]
web1 = 'https://md5.gromweb.com/?md5='

file = open('crecked_password.txt','w')
for name,has in zip(names,hashes):
	page = rq.get(web1+has)
	soup = BeautifulSoup(page.content, 'html.parser')
	
	try:
		file.write(name+':'+has+':'+soup.select('em')[1].text+'\n')
	except:
		file.write(name+':'+has+':'+'Not Found\n')
file.close()

