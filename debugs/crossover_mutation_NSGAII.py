import numpy as np
import math
import copy
from numba import jit, int32, int64

@jit
def contains(x, list) :
    
    for i in list :
        if x == i :
            return True
    return False

def separate_ox_crossover(keep_vector, old_vector) :

    return 
    
def gera_cromossomo(max_ap, max_pos):

    ''' Gera cromossomos de forma aleatoria de acordo com as entradas.
        max_ap = quantidade de bits para representar a quantidade de ap alocada
        max_pos = quantidade de pontos na matriz que representa as posicoes para alocar ap
    '''

    #cria o vetor de quantidade de access point
    genes = np.array((), np.int64)
    for i in range(max_ap) :
        aux = np.random.normal(0.5, 0.2, 1)
        if (aux > 0.5) :
            genes = np.append(genes, 1)
        else : 
            genes = np.append(genes, 0)

    #cria vetor de permutacao das posicoes dos access point e adiciona no genes
    genes = np.concatenate((genes,np.random.permutation(max_pos)))

    return genes

def crossover(bits_AP, point_cross, p1_ox_cross, p2_ox_cross, genes1, genes2) :
    
    '''Realiza o cruzamento de dois cromossomos
    bits_AP = quantidade de bits que representa a quantidade de ap
    point_cross = ponto onde ocorrera o crossover de 1 ponto na quantidade de ap
    p1_ox_cross = primeiro ponto do crossover ox aplicado na permutacao das posicoes
    p2_ox_cross = segundo ponto do crossover ox aplicado na permutacao das posicoes
    genes1 = cromossomo do primeiro genitor
    genes2 = cromossomo do segundo genitor
    '''

    #pega apenas os bits de quantidade de access point
    genes1_ap = genes1[:bits_AP]
    genes2_ap = genes2[:bits_AP]
    
    #pega o vetor de permutacoes das posicoes
    genes1_pos = genes1[bits_AP:]
    genes2_pos = genes2[bits_AP:]

    #crossover de um ponto na quantidade de access point
    offspring1 = np.concatenate((genes1_ap[:point_cross],genes2_ap[point_cross:]))
    offspring2 = np.concatenate((genes2_ap[:point_cross],genes1_ap[point_cross:]))

    #crossover OX no vetor de permutacoes
    #offspring 1 
    aux_keep = genes1_pos[p1_ox_cross:p2_ox_cross]

    #separa os elementos que serao reposicionados
    aux_new = np.setdiff1d(genes2_pos, aux_keep, assume_unique=True)
    vet_offspring1 = np.array([],dtype=np.int64)
    for i in aux_new :
        if len(vet_offspring1) == p1_ox_cross :
            vet_offspring1 = np.append(vet_offspring1, aux_keep)
            vet_offspring1 = np.append(vet_offspring1,i)
        else :
            vet_offspring1 = np.append(vet_offspring1,i)

    #offspring 2 
    aux_keep = genes2_pos[p1_ox_cross:p2_ox_cross]
    
    #separa os elementos que serao reposicionados
    aux_new = np.setdiff1d(genes1_pos, aux_keep,assume_unique=True)
    vet_offspring2 = np.array([],dtype=np.int64)
    for i in aux_new :
        if len(vet_offspring2) == p1_ox_cross :
            vet_offspring2 = np.append(vet_offspring2, aux_keep)
            vet_offspring2 = np.append(vet_offspring2,i)
        else :
            vet_offspring2 = np.append(vet_offspring2,i)
    
    #remontagem dos cromossomos
    offspring1 = np.concatenate((offspring1, vet_offspring1))
    offspring2 = np.concatenate((offspring2, vet_offspring2))

    return [offspring1, offspring2]


gene = []

for i in range(0,2) :
    gene.append(gera_cromossomo(5,195000) )

print(gene)


filhos = []
#gene.append( np.array([1,0,1,1,0,1,2,3,4,5],dtype=np.int64) )
#gene.append( np.array([0,0,1,0,1,5,4,3,2,1],dtype=np.int64) )

filhos += crossover(5,3,60000,130000,gene[0],gene[1])

print(gene[0])
print(gene[1])
print()    
print(filhos[0])
print(filhos[1])


'''


filhos = crossover(17,9,80000,130000,gene1,gene2)
print(gene1)
print(filhos[0])
print(gene2)
print(filhos[1])



for i in range(0,100) :
    gera_cromossomo(17,195000)


    No trabalho do samuel para o bloco A são gerados 195000 pontos, como teste vou usar esse valor para
    os testes e validação dos crossover e mutacao.


bits_for_enviroment = math.ceil(math.log(195000,2))

cromossomo = np.random.permutation(195000)
'''

'''

cromossomo = [0 for i in range(0,5)]
cromossomoNP = np.array(cromossomo, dtype=np.int32)

cromossomoNP2 = np.copy(cromossomoNP)

cromossomoNP[2] = 1
cromossomoNP[0] = 1
cromossomoNP2[1] = 1
cromossomoNP2[1] = 1

vet1 = np.array([3,5,4,2,1],dtype=np.int32)
vet2 = np.array([2,4,3,1,5],dtype=np.int32)

print(vet1)
print(cromossomoNP)

cromossomoNP = np.concatenate((cromossomoNP,vet1))
cromossomoNP2 = np.concatenate((cromossomoNP2,vet2))

resultado  = crossover(10, 1, 2, 4, cromossomoNP, cromossomoNP2)

print(resultado[0])
print(resultado[1])


    Na codificação do cromossomo, indique quantos bits tem a parte da quantidade de aps, pq dai 
    a segunda parte é só fazer 2 elevado à quantidade de bits e colocar as posições onde os aps
    vão ser posicionados imaginando q a matriz seja um vetor gigante.
    Todas as possiveis posições de aps do vetor devem ser preenchidas com alguma posição válida. Porém,
    para representar uma solução, deve se olhar quantos aps estão sendo usados, na primeira parte do 
    cromossomo,e pegar as primeiras posições do vetor de posições do ap, de acordo com a quantidade
    informada na primeira parte do cromossomo. 
'''