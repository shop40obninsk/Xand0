import random
import numpy as np

def free_places(mass):
    free_places_mass=[]
    for i in range(len(mass)):
        for j in range(len(mass[i])):
            if mass[i][j]==2:
                free_places_mass.append([i,j])
    return free_places_mass

class Engine:
    def __init__(self,User_figure):
        self.place=[
            [2,2,2],
            [2,2,2],
            [2,2,2]
            ]
        self.User_figure=User_figure
        if User_figure==0:
            self.Mashine_figure = 1
        else:
            self.Mashine_figure = 0

    def User_step(self,X,Y):
        if self.place[X][Y]==2:
            self.place[X][Y]=self.User_figure
            return True
        else: return False

    def Mashine_step(self):
        random_place=free_places(self.place)[random.randint(0,len(free_places(self.place))-1)]
        self.place[random_place[0]][random_place[1]]=self.Mashine_figure

    def Check_win(self):
        for i in self.place:
            if i.count(1)==len(i):
                return 1
            if i.count(0)==len(i):
                return 0

        for i in np.transpose(np.array(self.place)):
            if i.tolist().count(1)==len(i):
                return 1
            if i.tolist().count(0)==len(i):
                return 0


        diagonal1=np.diag(np.array(self.place)).tolist()
        diagonal2 = np.diag(np.rot90(np.array(self.place))).tolist()

        if diagonal1.count(1)==len(diagonal1):
            return 1
        if diagonal1.count(0)==len(diagonal1):
            return 0

        if diagonal2.count(1) == len(diagonal2):
            return 1
        if diagonal2.count(0) == len(diagonal2):
            return 0
        return 2

    def show_place(self):
        g=""
        for i in range(len(self.place)):
            s = '|'
            for j in range(len(self.place[i])):
                if self.place[i][j]!=2:
                    if str(self.place[i][j])=="0":
                        s += "0" + "|"
                    else:
                        s += "x" + "|"
                else:
                    s+="  |"
            g+=str(s)+"\n"
        print(g.replace("  "," "))
        return g
    def get(self):
        return self.place