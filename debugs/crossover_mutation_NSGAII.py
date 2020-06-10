import numpy as np
import math
import copy
from numba import jit, int32, int64
  
def gera_cromossomo(bits_ap, max_pos):

    ''' Gera cromossomos de forma aleatoria de acordo com as entradas.
        bits_ap = quantidade de bits para representar a quantidade de ap alocada
        max_pos = quantidade de pontos na matriz que representa as posicoes para alocar ap
    '''

    #cria o vetor de quantidade de access point
    gene = np.array((), np.int64)
    for i in range(bits_ap) :
        aux = np.random.normal(0.5, 0.2, 1)
        if (aux > 0.5) :
            gene = np.append(gene, 1)
        else : 
            gene = np.append(gene, 0)

    #cria vetor de permutacao das posicoes dos access point e adiciona no gene
    gene = np.concatenate((gene,np.random.permutation(max_pos)))

    return gene

def crossover(bits_AP, point_cross, p1_ox_cross, p2_ox_cross, gene1, gene2) :
    
    '''Realiza o cruzamento de dois cromossomos
        bits_AP = quantidade de bits que representa a quantidade de ap
        point_cross = ponto onde ocorrera o crossover de 1 ponto na quantidade de ap
        p1_ox_cross = primeiro ponto do crossover ox aplicado na permutacao das posicoes
        p2_ox_cross = segundo ponto do crossover ox aplicado na permutacao das posicoes
        gene1 = cromossomo do primeiro genitor
        gene2 = cromossomo do segundo genitor
    '''

    #pega apenas os bits de quantidade de access point
    gene1_ap = gene1[:bits_AP]
    gene2_ap = gene2[:bits_AP]
    
    #pega o vetor de permutacoes das posicoes
    gene1_pos = gene1[bits_AP:]
    gene2_pos = gene2[bits_AP:]

    #crossover de um ponto na quantidade de access point
    offspring1 = np.concatenate((gene1_ap[:point_cross],gene2_ap[point_cross:]))
    offspring2 = np.concatenate((gene2_ap[:point_cross],gene1_ap[point_cross:]))

    #crossover OX no vetor de permutacoes
    #offspring 1 - pega a parte do vetor que continuara imutavel
    aux_keep = gene1_pos[p1_ox_cross:p2_ox_cross]

    #separa os elementos que serao reposicionados
    aux_new = np.setdiff1d(gene2_pos, aux_keep, assume_unique=True)
    
    #cria novo vetor reposicionando as posicoes que nao serao mantidas
    vet_offspring1 = np.array([],dtype=np.int64)
    vet_offspring1 = np.append(vet_offspring1,aux_new[:p1_ox_cross])
    vet_offspring1 = np.append(vet_offspring1,aux_keep)
    vet_offspring1 = np.append(vet_offspring1,aux_new[p1_ox_cross:])    
    
    #offspring 2 - pega a parte do vetor que continuara imutavel
    aux_keep = gene2_pos[p1_ox_cross:p2_ox_cross]
    
    #separa os elementos que serao reposicionados
    aux_new = np.setdiff1d(gene1_pos, aux_keep,assume_unique=True)
    
    #cria novo vetor reposicionando as posicoes que nao serao mantidas
    vet_offspring2 = np.array([],dtype=np.int64)
    vet_offspring2 = np.append(vet_offspring2,aux_new[:p1_ox_cross])
    vet_offspring2 = np.append(vet_offspring2,aux_keep)
    vet_offspring2 = np.append(vet_offspring2,aux_new[p1_ox_cross:])
    
    #remontagem dos cromossomos
    offspring1 = np.concatenate((offspring1, vet_offspring1))
    offspring2 = np.concatenate((offspring2, vet_offspring2))

    return [offspring1, offspring2]

def reciprocal_exchange_mutation(bits_ap, first_pt, second_pt, gene) :
    
    '''Realiza a mutacao fazendo switch entre duas posicoes do vetor de permutacao
        first_pt = primeira posicao do switch
        second_pt = segunda posicao do switch
        gene = solucao que recebera a mutacao
    '''

    aux = gene[bits_ap+first_pt]
    gene[bits_ap+first_pt] = gene[bits_ap+second_pt]
    gene[bits_ap+second_pt] = aux 
    
    return gene

def displacement_mutation(bits_ap, position, lenght, offset, gene):
    
    '''Desloca algumas posicoes para a diretira de acordo com o offset
        position = posicao onde comeca o deslocamento
        lenght = quantidade de posicoes para deslocar
        offset = tamanho do deslocamento
    '''
    
    gene_aux = gene[bits_ap:]

    gene_new = np.array([], dtype=np.int64)
    gene_new = np.append(gene_new, gene[:bits_ap])
    gene_new = np.append(gene_new, gene_aux[:position])
    gene_new = np.append(gene_new, gene_aux[position+lenght:position+lenght+offset])
    gene_new = np.append(gene_new, gene_aux[position:position+lenght])
    gene_new = np.append(gene_new, gene_aux[position+lenght+offset:])
    
    print(gene_new[110004])
    

def bit_flip_mutation():
    pass


#genes = np.array([0,1,1,1,2,3,4,5], np.int64)
#genes = [0,1,1,1,2,3,4,5]
#genes = []
#genes.append(gera_cromossomo(5,195000))

#reciprocal_exchange_mutation(3,1,3,genes)
#displacement_mutation(5,80000,20000,10000, genes[0])

print(genes)


'''
gene = []

for i in range(0,100) :
    gene.append(gera_cromossomo(5,195000))



filhos = []
#gene.append( np.array([1,0,1,1,0,1,2,3,4,5],dtype=np.int64) )
#gene.append( np.array([0,0,1,0,1,5,4,3,2,1],dtype=np.int64) )

for i in range(0,75) :
    filhos += crossover(5,2,80000,130000,gene[i],gene[np.random.randint(49)])


print(gene[0])
print(gene[1])
print()    
print(filhos[0])

print(filhos[1])
'''

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

[0,1,1,3,5,4,2,1]

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