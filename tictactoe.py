import random

class RPSai:
    """ A game of rock paper scissors
                                        """
    def __init__(self):
        self.history = []

    def opponentMove(self,move):
        if move == "R":
            self.history.append(move)
        elif move == "P":
            self.history.append(move)
        elif move == "S":
            self.history.append(move)
        else:
           return "ERROR"

    def beatMove(self,move):
        if move == "R":
            return "P"
        elif move == "P":
            return "S"
        elif move == "S":
            return "R" 

    def predictMove(self):
        often = {}
        for i in self.history:
            if i in often:
                often[i] += 1
            else:
                often[i] = 1
        order = sorted(often, key=lambda k:often[k])
        return order[-1]

    def playMove(self):
        a = self.predictMove()
        self.beatMove(a)

    def playMovePro(self):
        Rcount = 0
        Scount = 0
        Pcount = 0
        Rcount1 = 0
        Scount1 = 0
        Pcount1 = 0

        if len(self.history) < 6:
        
            if len(self.history) == 0: #If nothing is played by opponent, play random
                self.beatMove(random.choice(["R","P","S"]))

        #If there is only one item then play a move that beats the one move
            elif len(self.history) == 1:
                self.beatMove(self.history[1])
        
            elif len(self.history) == 2: #Plays randomly
                self.beatMove(random.choice(["R","P","S"]))

            elif len(self.history) == 3:
            #Checks if only one move is being played
                for move in self.history:
                    if move == "P":
                        Pcount += 1
                    elif move == "S":
                        Scount += 1
                    else:
                        Rcount += 1       
                if len(self.history) == Pcount:
                    self.beatMove("P")
                elif len(self.history) == Rcount:
                    self.beatMove("R")
                elif len(self.history) == Scount:
                    self.beatMove("S")
                
         #Checks if thereis a common pattern where a is the last three terms in list  
                a = self.history[-3] + self.history[-2] + self.history[-1]
                if a == "RPS":
                    self.beatMove("R")
                elif a == "SRP":
                    self.beatMove("S")
                elif a == "PSR":
                    self.beatMove("P")
                elif a == "PRS":
                    self.beatMove("P")
                elif a == "SPR":
                    self.beatMove("S")
                elif a == "RSP":
                    self.beatMove("R")

            elif len(self.history) == 4: #Different patterns when list is  4 elements long
                a = self.history[-4] + self.history[-3] + self.history[-2] + self.history[-1]
                if a == "RPSR":
                    self.beatMove("P")
                elif a == "SRPS":
                    self.beatMove("R")
                elif a == "PSRP":
                    self.beatMove("S")
                elif a == "PRSP":
                    self.beatMove("R")
                elif a == "SPRS":
                    self.beatMove("P")
                elif a == "RSPR":
                    self.beatMove("S")
            else:
                often = {}
                for i in self.history:
                    if i in often:
                        often[i] += 1
                    else:
                        often[i] = 1
                order = sorted(often, key=lambda k:often[k])
                self.beatMove(random.choice(["R","P","S",order[-1]])) 
        

        elif 6 <= len(self.history) < 190:
            #Checks if everything is common in list
            for move in self.history:
                if move == "P":
                    Pcount1 += 1
                elif move == "S":
                    Scount1 += 1
                else:
                    Rcount1 += 1       
            if len(self.history) == Pcount1:
                self.beatMove("P")
            elif len(self.history) == Rcount1:
                self.beatMove("R")
            elif len(self.history) == Scount1:
                self.beatMove("S")
                
        #Checks different types of patterns
            for i in "RSP":
                if i + i + i + i + i + i == self.history[-6] + self.history[-5] + self.history[-4] + self.history[-3] + self.history[-2] + self.history[-1]:
                    if i + i + i + i + i + i == "RRRRRR" or i + i + i + i + i + i == "PPPPPP" or i + i + i + i + i + i == "SSSSSS":
                        self.beatMove(self.history[-1])
                for j in "RSP":
                    if i + j + i + j + i + j == self.history[-6] + self.history[-5] + self.history[-4] + self.history[-3] + self.history[-2] + self.history[-1]:
                        if i + j + i + j + i + j == "RPRPRP" or i + j + i + j + i + j == "RSRSRS" or i + j + i + j + i + j == "SPSPSP" or i + j + i + j + i + j == "SRSRSR" or i + j + i + j + i + j == "PSPSPS" or i + j + i + j + i + j == "PRPRPR":
                            self.beatMove(self.history[-6])
                    elif i + i + j + j + i + i == self.history[-6] + self.history[-5] + self.history[-4] + self.history[-3] + self.history[-2] + self.history[-1]:
                        if i + i + j + j + i + i == "SSRRPP" or i + i + j + j + i + i == "PPSSRR" or i + i + j + j + i + i == "RRPPSS":
                            self.beatMove(self.history[-6])
                        elif i + i + j + j + i + i == "SSPPRR" or i + i + j + j + i + i == "RRSSPP" or i + i + j + j + i + i == "PPRRSS":
                            self.beatMove(self.history[-6])
                    elif i + i + i + j + j + j == self.history[-6] + self.history[-5] + self.history[-4] + self.history[-3] + self.history[-2] + self.history[-1]:
                        if i + i + i + j + j + j == "RRRPPP" or i + i + i + j + j + j == "RRRSSS" or i + i + i + j + j + j == "PPPRRR" or i + i + i + j + j + j == "PPPSSS" or i + i + i + j + j + j == "SSSRRR" or i + i + i + j + j + j == "SSSPPP":  
                            self.beatMove(self.history[-6])
                    for k in "RSP":
                        if i + j + k + i + j + k == self.history[-6] + self.history[-5] + self.history[-4] + self.history[-3] + self.history[-2] + self.history[-1]:
                            if i + j + k + i + j + k == "RPSRPS" or i + j + k + i + j + k == "SRPSRP" or i + j + k + i + j + k == "PSRPSR":
                                self.beatMove(self.history[-6])
                            elif i + j + k + i + j + k == "RSPRSP" or i + j + k + i + j + k == "PRSPRS" or i + j + k + i + j + k == "SPRSPR":
                                self.beatMove(self.history[-6])
            else:
                often = {}
                for i in self.history:
                    if i in often:
                        often[i] += 1
                    else:
                        often[i] = 1
                order = sorted(often, key=lambda k:often[k])
                self.beatMove(random.choice(["R","P","S",order[-1]]))
        else:
            self.beatMove(random.choice(["R","P","S"]))
                
        




















        
        
        
            
