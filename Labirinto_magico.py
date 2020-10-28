def create(m,n):
    matrix=[]
    for i in range(m):
        l=[None]*n
        matrix+=[l]
    return matrix

def read(matrix,m,n):
    for i in range(m):
        l=input().split()
        for j in range(n):
            labirinto[i][j]=int(l[j])

def detPosColuna(matrix,entrada,n):
    if(entrada==1):
        for j in range(n):
            if(matrix[-1][j]!=-1):
                pos=j
                return pos
    else:
        for j in range(-1,-n,-1):
            if(matrix[-1][j]!=-1):
                pos=n+j
                return pos

def age(matrix,posL,posC,age,imunity):
    if(not imunity):
        age+=matrix[posL][posC]
        return age
    else:
        return age

def ageHerb(matrix,posL,posC,age,ageLimit,heroic):
    ageHerb=age
    if(age<=ageLimit):
        heroic=True
    return ageHerb,heroic

teste=int(input())

for test in range(teste):

    imune=False
    heroi=False
    caminho="N"
    idade, idadeLimite=input().split()
    idade=int(idade)
    idadeLimite=int(idadeLimite)
    entradaMagica, entradaEscolhida=input().split() 
    
    if(int(entradaEscolhida)==int(entradaMagica)):
        imune=True
    
    m,n=input().split()
    m=int(m)
    n=int(n)
    
    labirinto=create(m,n)
    read(labirinto,m,n)
    
    posLinha=m-1
    posColuna=detPosColuna(labirinto,int(entradaEscolhida),n)
    
    if(not imune):
        idade+=labirinto[posLinha][posColuna]
    labirinto[posLinha][posColuna]=-1
    
    while(True):
        try:
            if(0<=labirinto[posLinha-1][posColuna]<=3):
                posLinha-=1
                idade=age(labirinto,posLinha,posColuna,idade,imune)
                if(labirinto[posLinha][posColuna]==0):
                    idadeErva,heroi=ageHerb(labirinto,posLinha,posColuna,idade,idadeLimite,heroi)
                caminho+=" N"
                labirinto[posLinha][posColuna]=-1
                
            elif(0<=labirinto[posLinha+1][posColuna]<=3):
                posLinha+=1
                idade=age(labirinto,posLinha,posColuna,idade,imune)
                if(labirinto[posLinha][posColuna]==0):
                    idadeErva,heroi=ageHerb(labirinto,posLinha,posColuna,idade,idadeLimite,heroi)
                caminho+=" S"
                labirinto[posLinha][posColuna]=-1
        
            elif(0<=labirinto[posLinha][posColuna-1]<=3):
                posColuna-=1
                idade=age(labirinto,posLinha,posColuna,idade,imune)
                if(labirinto[posLinha][posColuna]==0):
                    idadeErva,heroi=ageHerb(labirinto,posLinha,posColuna,idade,idadeLimite,heroi)
                caminho+=" O"
                labirinto[posLinha][posColuna]=-1
        
            elif(0<=labirinto[posLinha][posColuna+1]<=3):
                posColuna+=1
                idade=age(labirinto,posLinha,posColuna,idade,imune)
                if(labirinto[posLinha][posColuna]==0):
                    idadeErva,heroi=ageHerb(labirinto,posLinha,posColuna,idade,idadeLimite,heroi)
                caminho+=" L"
                labirinto[posLinha][posColuna]=-1
            
        except IndexError:
            caminho+=" S"
            break
    
    print(caminho)
    if(heroi==True):
        print(idade,'S',idadeErva)
    else:
        print(idade,'N',idadeErva)