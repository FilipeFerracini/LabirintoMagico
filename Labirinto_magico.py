'''
Filipe Matos Ferracini, RGA 2020.1907.052-6

O programa lê primeiramente o número de testes a serem executados, seguido pela idade com que a pessoa
entra no labirinto, e a idade limite para a erva mágica ter efeito. Após isso, lê qual a abertura mágica
e qual a abertura escolhida pela pessoa. Na próxima linha lê-se o tamanho da matriz(labirinto), e logo em seguida
a sequência de linhas e colunas da matriz.
Após isto são devolvidas 2 linhas para cara um dos testes: uma linha contendo a sequência de movimentos
do ser humano pelo labirinto, outra linha contendo a nova idade que o ser humano ficou ao terminar de atravessar
o labirinto, se ele ou ela se tornou herói ou heroína, e a a idade que o ser humano tinha ao pegar a erva mágica.

São criadas e definidas funções de modo a deixar o código principal mais enxuto. Em alguns casos, no que diz respeito
à leitura e manipulação de matrizes, e para a definição de qual coluna da matriz se deseja iniciar o trajeto.
Ademais, estruturas que se repetem várias vezes, como para definir a idade a cada movimento, para definir o próprio
movimento e para se definir idade em que o aventureiro pega a erva, recebem funções próprias, a fim de simplificar
o código principal.

Para a movimentação interna, como alternativa à opção de se criar um vetor para armazenar as posições visitadas,
optei por sobrescrever a matriz, como se o labirinto se fechasse atrás do aventureiro, impossibilitando que ele voltasse
e me permitindo visualizar apenas uma opção para onde se movimentar. Como sempre se começa da face sul, em direção ao norte
o programa já inicia com essas considerações, inclusive com a variável 'caminho' tendo por valor inicial o movimento N, de
entrada no labirinto.

De forma semelhante, na saída, que sempre será pela face sul e em movimento S, uma vez que nenhum movimento é possível,
o programa tenta 'saltar para fora da matriz', ocasionando um IndexError, que é contornado por um Try/Except justamente
para finalizar o programa e imprimir a última movimentação: S.

Após isto imprime-se o requisitado e inicia outro teste, ou finaliza o programa.
'''
def create(m,n): #Função que cria uma matriz vazia do tamanho do labirinto
    matrix=[] #instancia matriz vazia
    for i in range(m): #iteração por número de linhas
        l=[None]*n #Cria lista com n posições (colunas)
        matrix+=[l] #Adiciona a linha à coluna
    return matrix #Retorna a matriz

def read(matrix,m,n): #Função que faz a leitura das posição da matriz, ou das posições do labirinto
    for i in range(m): #Iteração por número de linhas
        l=input().split() #Lê uma linhas de valores e os separa por espaços (n posições)
        for j in range(n): #iteração por número de colunas
            matrix[i][j]=int(l[j]) #Adiciona à matriz labirinto a posição lida, como inteiro

def detPosColuna(matrix,entrada,n): #Função que determina a coluna de entrada do Labirinto
    if(entrada==1): #Caso foi escolhida a primeira entrada
        for j in range(n): #Processo iterativo por número de colunas, da esquerda para a direita
            if(matrix[-1][j]!=-1): #Verifica se a posição (primeira encontrada) é diferente de -1, ou seja, se é entrada/saída
                pos=j #Caso positivo, guarda a posição da coluna na variável pos
                return pos #Retorna a variável pos
    else: #Caso foi escolhida a segunda entrada
        for j in range(-1,-n,-1): #Processo iterativo por número de colunas, da direita para a esquerda
            if(matrix[-1][j]!=-1): #Verifica se a posição (primeira encontrada) é diferente de -1, ou seja, se é entrada/saída
                pos=n+j #Caso positivo, guarda a posição da coluna na variável pos
                return pos #Retorna a variável pos

def age(matrix,posL,posC,age,imunity): #função que calcula a idade da pessoa a cada movimentação no labirinto
    if(not imunity): #Caso a pessoa não seja imune, sofre o efeito da maldição ao entrar no labirinto
        age+=matrix[posL][posC] #Soma à idade o valor da celula
        return age #retorna a nova idade
    else: #Caso a pessoa seja imuna aos efeitos da maldição, nada acontece, e ela mantém a idade
        return age #retorna a nova idade

def ageHerb(age,ageLimit,heroic): #função quando a pessoa encontra a erva, guarda a idade do momento e determina se ela é heroi
    ageHerb=age #Armazena a idade com a qual a pessoa pegou a erva
    if(age<=ageLimit): #Caso a idade da pessoa seja menor ou igual à idade Limite para se tornar heroi
        heroic=True #Ela será heroi, assim a booleana de heroi mudará de False para True
    return ageHerb,heroic #Retorna a idade com a qual a erva foi pega e o valor da variável de heroi

def direcao(matrix,posL,posC,ageDir,ageLimit,heroicDir,path,imunity,ageHerbDir): #Função que faz a movimentação da pessoa dentor do labirinto
    movement=[-1,1] #vetores de movimentação
    yMovement=[' N',' S'] #Vetores de movimentação Norte e Sul, para serem adicionados ao caminho
    xMovement=[' O',' L'] #Vetores de movimentação Oeste e Leste, para serem adicionados ao caminho
    for i in range(2): #Estrutura de repetição para verificar as posições para cima ou para baixo, para esquerda ou para direita
        if(0<=matrix[posL+movement[i]][posC]<=3): #Se a posição verificada for diferente de -1, verifica primeiro p/ N, depois p/ S
            posL+=movement[i] #soma à linha a posição do vetor movement, indicando deslocamento vertical
            ageDir=age(matrix,posL,posC,ageDir,imunity) #Chama a função age e a atribui a uma variável do escopo
            if(matrix[posL][posC]==0): #Caso a posição encontrada seja 0, ou seja, foi encontrada a erva, executa:
                ageHerbDir,heroicDir=ageHerb(ageDir,ageLimit,heroicDir) #Chama a função ageHerb, para registrar a idade em que a erva foi pega e se é heroi
            path+=yMovement[i] #adiciona ao caminho a direção vertical executada
            matrix[posL][posC]=-1 #Substitui o valor da célula por -1, a fim de que não seja podssível retornar
            return posL, posC, ageDir, heroicDir, path, ageHerbDir #Retorna a nova posição de linha e de coluna, a idade, a variável de heroi, o caminho e a idade da erva
        
        elif(0<=matrix[posL][posC+movement[i]]<=3): #Se a posição verificada for diferente de -1, verifica primeiro p/ O, depois p/ L
            posC+=movement[i] #soma à linha a posição do vetor movement, indicando deslocamento horizontal
            ageDir=age(matrix,posL,posC,ageDir,imunity) #Chama a função age e a atribui a uma variável do escopo
            if(matrix[posL][posC]==0): #Caso a posição encontrada seja 0, ou seja, foi encontrada a erva, executa:
                ageHerbDir,heroicDir=ageHerb(ageDir,ageLimit,heroicDir) #Chama a função ageHerb, para registrar a idade em que a erva foi pega e se é heroi
            path+=xMovement[i] #adiciona ao caminho a direção horizontal executada
            matrix[posL][posC]=-1 #Substitui o valor da célula por -1, a fim de que não seja podssível retornar
            return posL, posC, ageDir, heroicDir, path, ageHerbDir #Retorna a nova posição de linha e de coluna, a idade, a variável de heroi, o caminho e a idade da erva

teste=int(input()) #quantidade de testes
for test in range(teste): #Faz os testes
    imune=False #Zera a imunidade, para nova atribuição
    heroi=False #Zera se a pessoa é herói, para nova atribuição
    idadeErva=None #Zera a idade em que a pessoa pega a erva, para nova atribuição
    caminho="N" #Zera o caminho, para nova atribuição (O movimento inicial sempre começa pela face sul)
    idade, idadeLimite=input().split() #lê a idade de quem entra e a idade limite para pegar a erva e se tornar herói
    idade=int(idade) #transforma a idade de string para int
    idadeLimite=int(idadeLimite) #transforma a idade limite de string para int
    entradaMagica, entradaEscolhida=input().split() #lê qual entrada é a mágica e qual é a entrada que a pessoa entrou
    
    if(int(entradaEscolhida)==int(entradaMagica)): #Caso as entradas sejam iguais
        imune=True #A pessoa se torna imune à maldição da idade
    
    m,n=input().split() #Lê as dimensões do labirinto
    m=int(m) #Transforma m de string p/ inteiro
    n=int(n) #Transforma n de string p/ inteiro
    labirinto=create(m,n) #Chama a função create, que cria uma matriz vazia de mxn
    read(labirinto,m,n) #Chama a função read, que lê os valores de cada posição do labirinto
    
    posLinha=m-1 #Declara a Linha na qual a pessoa entra na montanha (sempre face sul)
    posColuna=detPosColuna(labirinto,int(entradaEscolhida),n) #Chama função para determinar a coluna de entrada do labirinto
    
    if(not imune): # Caso a pessoa não seja imune, sofre o efeito da maldição ao entrar no labirinto
        idade+=labirinto[posLinha][posColuna] #Soma à idade o valor da celula
    labirinto[posLinha][posColuna]=-1 #Substitui o valor da célula por -1, a fim de que não seja podssível retornar
    
    while(True): #Inicia teste de movimentação interna ao labirinto
        try: #Tentar ir para uma das 4 direçãoes (N,S,L,O), procurando uma célula que não seja negativa
            posLinha,posColuna,idade,heroi,caminho,idadeErva=\
                  direcao(labirinto,posLinha,posColuna,idade,idadeLimite,heroi,caminho,imune,idadeErva) #Chama a função de movimentação
        except IndexError: #Caso não consiga encontrar, será dado um IndexError, com isso, saímos do labirinto
            caminho+=" S" #Adiciona a movimentação final, Sul, para sair do labirinto
            break #Finaliza o loop de movimentação
    
    print(caminho) #Imprime o trajeto realizado pela pessoa
    if(heroi==True): #Caso a condição da idade seja satisfeita, e a pessoa se tornou heroi, então
        print(idade,'S',idadeErva) #Imprime a idade com que saiu do labirinto, que virou heroi e a idade que pegou a erva
    else: #Caso contrário
        print(idade,'N',idadeErva) #Imprime a idade com que saiu do labirinto, que não virou heroi e a idade que pegou a erva