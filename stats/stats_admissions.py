from creation_dicos import *

t = open("stats_admissions_2024.csv",'r')
t.readline()
l=t.readlines()
t.close()

L = [(e.strip()).split(';') for e in l]

for e in L :
    if e[4] != '':
        dico_compte[(e[3],dico_banques[e[4]])]+=1
    elif e[5]=='PAS DE VOEUX' or e[5]=='PAS DE PROPOSITION' :
        dico_compte[(e[3],'PAS DE VOEUX')]+=1

