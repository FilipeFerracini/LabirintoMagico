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

def direcao(matrix,posL,posC,ageDir,ageLimit,heroicDir,path,imunity,ageHerbDir):
    movement=[-1,1]
    yMovement=[' N',' S']
    xMovement=[' O',' L']
    for i in range(2):
        if(0<=matrix[posL+movement[i]][posC]<=3):
            posL+=movement[i]
            ageDir=age(matrix,posL,posC,ageDir,imunity)
            if(matrix[posL][posC]==0):
                ageHerbDir,heroicDir=ageHerb(matrix,posL,posC,ageDir,ageLimit,heroicDir)
            path+=yMovement[i]
            matrix[posL][posC]=-1
            return matrix, posL, posC, ageDir, heroicDir, path, ageHerbDir
        
        elif(0<=matrix[posL][posC+movement[i]]<=3):
            posC+=movement[i]
            ageDir=age(matrix,posL,posC,ageDir,imunity)
            if(matrix[posL][posC]==0):
                ageHerbDir,heroicDir=ageHerb(matrix,posL,posC,ageDir,ageLimit,heroicDir)
            path+=xMovement[i]
            matrix[posL][posC]=-1
            return matrix, posL, posC, ageDir, heroicDir, path, ageHerbDir

teste=int(input())
for test in range(teste):
    imune=False
    heroi=False
    idadeErva=None
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
            labirinto,posLinha,posColuna,idade,heroi,caminho,idadeErva=\
                  direcao(labirinto,posLinha,posColuna,idade,idadeLimite,heroi,caminho,imune,idadeErva)
            
        except IndexError:
            caminho+=" S"
            break
    
    print(caminho)
    if(heroi==True):
        print(idade,'S',idadeErva)
    else:
        print(idade,'N',idadeErva)
