import os,random

for i in range (20):
    d = str(i) + 'days ago'
    rand = random.randrange(1,12)
    with open('test.txt','a') as file:
        file.write('iuhuyen'+'\n')
    os.system('git add .')
    os.system('git commit --date=" 2018-' +str(rand) + '-'+d+'" -m 1')
    os.system('git push -u origin master -f')