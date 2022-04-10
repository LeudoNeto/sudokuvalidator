class Checador:
    def __init__(self,x=0,y=0,bloco=1):
        self.x = x
        self.y = y
        self.bloco = bloco

    def checarbloco(self,board):
        blocoatual = []
        for x in range(0,3):
            for y in range(0,3):
                if board[y+self.y][x+self.x] not in blocoatual:
                    blocoatual.append(board[y+self.y][x+self.x])
        if len(blocoatual) < 9 or 0 in blocoatual:
            return False
        else:
            return True
    
    def proximobloco(self):
        if self.bloco not in [3,6]:
            self.x += 3
        elif self.bloco == 9:
            pass
        else:
            self.y += 3
            self.x -= 6
        self.bloco += 1

def valid_solution(board):
    checador = Checador()
    resposta = True
    for x in range(0,9):
        if not checador.checarbloco(board):
            resposta = False
        checador.proximobloco()
    for x in board:
        y = []
        for z in x:
            if z not in y:
                y.append(z)
        if len(y) < 9:
            resposta = False
    for x in range(0,9):
        y = []
        for z in board:
            if z[x] not in y:
                y.append(z[x])
        if len(y) < 9:
            resposta = False
    return resposta
