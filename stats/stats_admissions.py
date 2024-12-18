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




# On va commencer par les PSI

dico_filiere = {}
vals = []
legende = []
for k,v in dico_compte.items():
    if k[0] == 'PSI':
        dico_filiere[k[1]]=v
        vals.append([v,1])
        legende.append(k[1])



import matplotlib.pyplot as plt
import numpy as np

vals = np.array(vals)

vals = np.array([[  0,   1],
       [ 78,   1],
       [ 54,   1],
       [ 24,   1],
       [102,   1],
       [ 84,   1],
       [108,   1]])

legende = ['Concours Polytechnique - ENS', 'Concours Mines-Telecom', 'Concours Mines-Ponts', 'Arts Et Métiers', 'Concours Centrale-Supélec', 'Concours CCINP', 'Autres']

fig, ax = plt.subplots(figsize=(12, 8))

size = 0.3

outer_colors = plt.cm.tab10(np.linspace(0, 1, len(vals)))  # Couleurs pour l'extérieur
inner_colors = plt.cm.tab20c(np.linspace(0, 1, vals.size))  # Couleurs pour l'intérieur



wedges, texts, autotexts = ax.pie(
    vals.sum(axis=1), radius=1, colors=outer_colors, labels=legende,
    autopct=lambda pct: f"{int(round(pct * vals.sum() / 100, 0))}",  # Valeurs pourcentage et somme
    wedgeprops=dict(width=size, edgecolor='w')
)


#Exteriur
# ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
#        wedgeprops=dict(width=size, edgecolor='w'),)
#Intérieur
# ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
#         wedgeprops=dict(width=size, edgecolor='w'))

ax.legend()
ax.set(aspect="equal", title='Résultats PSI/PSI* - 2024')
plt.show()


# fig, ax = plt.subplots()
#
# size = 0.3
# vals = np.array([[60., 32.], [37., 40.], [29., 10.]])
#
# tab20c = plt.color_sequences["tab20c"]
# outer_colors = [tab20c[i] for i in [0, 4, 8]]
# inner_colors = [tab20c[i] for i in [1, 2, 5, 6, 9, 10]]
#
# ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
#        wedgeprops=dict(width=size, edgecolor='w'))
#
# # ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
#        # wedgeprops=dict(width=size, edgecolor='w'))
#
# ax.set(aspect="equal", title='Résultats PSI/PSI* - 2024')
# plt.show()
