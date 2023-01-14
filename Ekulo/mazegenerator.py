from math import*
import random as r
from pprint import pprint
from PIL import Image
import sys

def init_maze(h,w):
    # On commence par rendre impair h et w
    if(w%2 == 0):
        w+=1
    if(h%2 == 0):
        h+=1
    # On initialize deux labyrinthes
    maze = []
    maze_prime = []
    # On initialize ry, rx mr qui serve à detecter une sur deux fois que passe la boucle
    ry=1
    rx=0
    mr = -1 # mr est à -1 pour qu'il passe à 0 la première fois
    for y in range(h):
        maze_prime.append([])
        if(ry==0):
            ry = 1
        else:
            ry = 0
            maze.append([])
            mr+=1
        rx=0
        for x in range(w):
            if(ry==0):
                if(rx == 0):
                    maze[mr].append([y,x,1])
                    maze_prime[y].append(1)
                    rx=1
                else:
                    maze_prime[y].append(1)
                    rx=0
            else:
                maze_prime[y].append(1)
    V=[]# V est la pile avec les cellules visité
    C=[random_case_maze(maze)]# On ajoute à C une cellule au hasard
    return maze,maze_prime,C,V

def random_case_maze(mazev):
    ry=r.randint(0,len(mazev)-1)
    rx=r.randint(0,len(mazev[0])-1)
    return ry,rx

def present(y,x,T):
    p=0
    for i in range(len(T)):
        if(T[i-1] == (y,x)):
            p=1
    return p

def  get_pos_maze(maze,C,V):
    N = True
    S = True
    E = True
    O = True
    y,x = C[-1]
    pos = []
    yl = maze[y][x][0] 
    xl = maze[y][x][1]
    Cc = []
    if( y-1 < 0 or present(y-1,x,C)==1 or present(y-1,x,V)==1):
        #Nord
        N = False
    else:
        pos.append((y-1,x))
        Nc = (yl-1,xl)
        Cc.append(Nc)
    if( y+1 > len(maze)-1 or present(y+1,x,C)==1 or present(y+1,x,V)==1):
        #Sud
        S = False
    else:
        pos.append((y+1,x))
        Sc = (yl+1,xl)
        Cc.append(Sc)
    if( x-1 < 0 or present(y,x-1,C)==1 or present(y,x-1,V)==1):
        #Est
        E = False
    else:
        pos.append((y,x-1))
        Ec = (yl,xl-1)
        Cc.append(Ec)
    if( x+1 > len(maze[0])-1 or present(y,x+1,C)==1 or present(y,x+1,V)==1):
        #Ouest
        O = False
    else:
        pos.append((y,x+1))
        Oc = (yl,xl+1)
        Cc.append(Oc)
    pos_final = False
    if(len(pos) > 0):
        ran = r.randint(0,len(pos)-1)
        pos_final = pos[ran]
        Cc=Cc[ran]
    return pos_final,Cc

def maze_generator(maze,maze_prime,C,V,step):
    pos,Cc = get_pos_maze(maze,C,V)
    if(pos != False):
        C.append(pos)
        #crée le lien
        yl = Cc[0]
        xl = Cc[1]
        maze_prime[yl][xl] = 0
        y = maze[pos[0]][pos[1]][0]
        x = maze[pos[0]][pos[1]][1]
        maze_prime[y][x] = 0
        step+=1
        #print("---------------------step : ",step,"-------------------------------")
        maze_generator(maze,maze_prime,C,V,step)
    elif(len(C) == 1):
        quit
    else:
        V.append(C[-1])
        del(C[-1])
        step+=1
        #print("---------------------step : ",step,"-------------------------------")
        maze_generator(maze,maze_prime,C,V,step)
    return

def finish(maze):
    for i in range(len(maze)):
        maze[i-1].insert(0,1)
        maze[i-1].append(1)
    maze.insert(0,[1]*len(maze[1]))
    maze.append([1]*len(maze[1]))
    x=r.randint(int(len(maze)*0.5),int(len(maze[0])-3))
    y=r.randint(int(len(maze)*0.5),int(len(maze)-3))
    if maze[y][x] == 1:
        x,y = x+1,y
        if maze[y][x] == 1:
            x,y = x,y+1
            if maze[y][x] == 1:
                x,y = x+1,y+1
    maze[y][x] = 3
    return maze

def create_maze(x,y):
    sys.setrecursionlimit(1000000)
    maze,maze_prime,C,V = init_maze(x,y)
    maze_generator(maze,maze_prime,C,V,0)
    return finish(maze_prime)
