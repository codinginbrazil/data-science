import matplotlib.pyplot as plt


PATH_DATA =  'data/bra_population/'
PATH_GRAPH = 'view/graph/bra_population/'

x=y=[]

''' source: DataSUS
    http://tabnet.datasus.gov.br/cgi/tabcgi.exe?ibge/cnv/projpopbr.def
'''
dt = open(
    PATH_DATA+"populacao_brasileira_1980-2016.csv"
    ).readlines() 

for i in range(len(dt)):
    if i != 0:
        attribute = dt[i].split(";")
        x.append(int(attribute[0]))
        y.append(int(attribute[1]))

plt.plot(x,y)
plt.bar(x,y)

plt.title("Crescimento da População Brasileira 1980-2016")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")

plt.savefig(PATH_GRAPH+"1980-2016-line-plus-bar.pdf")
