import numpy as np

cromossomo = [0 for i in range(0,10)]
cromossomoNP = np.array(cromossomo, dtype=np.int64)

def crossover(bits_AP, point_cross, genes1, genes2) :
    
    '''Realiza o cruzamento de dois cromossomos'''

    #pega apenas os bits de quantidade de access point
    genes1_ap = genes1[:bits_AP]
    genes2_ap = genes2[:bits_AP]

    offspring1 = np.concatenate([genes1_ap[:point_cross],genes2_ap[point_cross:]])
    offspring2 = np.concatenate([genes2_ap[:point_cross],genes1_ap[point_cross:]])



    print(genes1_ap)
    print(genes2_ap)
    print()
    print(offspring1)
    print(offspring2)

cromossomoNP2 = np.copy(cromossomoNP)

cromossomoNP[2] = 1
cromossomoNP[0] = 1
cromossomoNP2[1] = 1
cromossomoNP2[1] = 1

crossover(3, 1, cromossomoNP, cromossomoNP2)

'''
    Na codificação do cromossomo, indique quantos bits tem a parte da quantidade de aps, pq dai 
    a segunda parte é só fazer 2 elevado à quantidade de bits e colocar as posições onde os aps
    vão ser posicionados imaginando q a matriz seja um vetor gigante.
    Todas as possiveis posições de aps do vetor devem ser preenchidas com alguma posição válida. Porém,
    para representar uma solução, deve se olhar quantos aps estão sendo usados, na primeira parte do 
    cromossomo,e pegar as primeiras posições do vetor de posições do ap, de acordo com a quantidade
    informada na primeira parte do cromossomo. 
'''