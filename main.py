import re


imput_filename = 'baza.txt'
result_filename = 'result.txt'

imputfile= open(imput_filename,'r')
resultfile = open(result_filename,'w')



mybazza = imputfile.read()
loofor = r'https...\w+.\w+.\w+.\w+.\d+.' 
results = re.findall(loofor, mybazza)
x = 1
for item in results:

    c = '№'+str(x)+' '+str(item)+ '\n'
    x += 1
    resultfile.write(c)
imputfile.close()
resultfile.close()

def hi_gerls(name):
    return 'hi '+ str(name)


listr = ['Oly','Kate','Masha']
s = list(map(hi_gerls,listr))
print(s)
res = [hi_gerls(c) for c in listr]
print(res)



