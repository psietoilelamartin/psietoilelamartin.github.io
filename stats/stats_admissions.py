from creation_dicos import *


# Statistiques de la forme
# Filière, Proposition, réponse donnée
t = open("stats_admissions_2024.csv",'r',encoding="utf-8")
t.readline()
l=t.readlines()
t.close()

L = [(e.strip()).split(';') for e in l]

for e in L :
    if e[1] != '':
        dico_compte[(e[0],dico_banques[e[1]])]+=1
    elif e[2]=='PAS DE VOEUX' or e[2]=='PAS DE PROPOSITION' :
        dico_compte[(e[0],'PAS DE VOEUX')]+=1


####
# 1. Ordre des écoles : XENS, Mines Ponts, Centrale, Mines Telecom, CCINP puis autre.
# 2. Couleurs différentes pour BCPST
# 3. PC 2024 : 2 Mines-Télécoms, 11 CCINP Physique; 10 CCINP Chimie, 6 autres, total 29
# 4. Autre ?  INSA ?
# 5. Petit changement : en PC/PC*, 5 élèves ont été dans une école Mines-Ponts au lieu de 4 (Brogi, Boisson, Frustié, Poinot, Zennadi). Peut-être parce que IMT Atlantique est dans Mines-Ponts et pas Mines-telecom ?  Côté INSA, deux admissibles sur Mines-Ponts (sans doute admis à IMT Atlantique et peut-être aux Mines de St Etienne, je ne sais pas) ont préféré aller à l'INSA qui attire en effet des élèves de bon niveau avec la situation géographique. Peut-être Bastien a-t-il donc raison mais il y a déjà pas mal de catégories...
# 6. ATtention à autres
#
####


import matplotlib.pyplot as plt
import numpy as np


#### En fait chaque filière à sa spécificité...
def make_pie_PSI(dico_compte):
    # Pour les PSI on met Arts et Métiers dans centrale
    dico_filiere = {}
    vals = []
    legende = []
    for k,v in dico_compte.items():
        if k[0] == 'PSI' and k[1] != 'Agro Veto' and k[1] != 'G2E':
            # TO DO GERER LES ARTS ET METIERS DANS CCP
            # if k[1] == 'Arts Et Métiers' :
            #     On met les A&M dans Centrale
            #     dico_filiere['Concours Centrale-Supélec']=v
            #     vals.append([v,v/3])
            #     legende.append(k[1])legende.append(k[1])
            # elif k[1] == 'Concours Centrale-Supélec' :
            #     dico_filiere['Concours Centrale-Supélec']+=v
            #     vals.append([v,v/3])
            #     legende.append(k[1])
            dico_filiere[k[1]]=v
            vals.append([v,v/3])
            legende.append(k[1])


    vals = np.array(vals)
    fig, ax = plt.subplots(figsize=(12, 8))
    size = 0.3

    outer_colors = plt.cm.tab10(np.linspace(0, 1, len(vals))[::-1])  # Couleurs pour l'extérieur
    # inner_colors = plt.cm.tab20c(np.linspace(0, 1, vals.size))  # Couleurs pour l'intérieur


    ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,labels = legende,
        wedgeprops=dict(width=size, edgecolor='w'))

    # ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
    #        wedgeprops=dict(width=size, edgecolor='w'))

    #ax.legend()


    ax.set(aspect="equal", title='Résultats PSI - 2024')
    #plt.show()
    return dico_filiere
a = make_pie_PSI(dico_compte)
plt.show()