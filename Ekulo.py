
""" ------------------ Ekulo------------------''''''
                    réaliser par
                Florent MOULON
                Maxime TERRASSE
                Aymen BELKASMI
''''''------------------------------------------"""

# //-------------------------------------------// head
import time
from math import *
import random as r
from pprint import pprint
import sys
sys.path.append("Ekulo")
from mazegenerator import *
from PIL import *
import tkinter as tk
import pygame as py
import os
from mazeimage import *

page = "home"

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()
#,py.FULLSCREEN
screen = py.display.set_mode((screen_width, screen_height),py.FULLSCREEN)
background_color = (38, 38, 43)
screen.fill(background_color)

py.display.flip()



# //-------------------------------------------// body

#print(create_maze_back(int(screen_height/32)-1,int(screen_width/32)-1)))
#fond = py.image.load(load_maze(create_maze(int(screen_height/32-1),int(screen_width/32-1)))).convert()
#ttt = load_maze_home(create_maze(int(2080/32),int(3760/32)))

def detect_col(pos,img,pos_img):
    size = img.get_size()
    x,y = pos
    x1,y1 = pos_img
    x2 = size[0] + pos_img[0]
    y2 = size[1] + pos_img[1]
    if (x >= x1 and x <= x2 and y >= y1 and y <= y2):
        return True
    else : 
        return False

py.font.init()
font_game = py.font.SysFont("calibri", 45)
font_level = py.font.SysFont("calibri", int(screen_height/3))
font_score = py.font.SysFont("impact", int(screen_height/7))
font_time = py.font.SysFont("arial", int(screen_height/9))
page_etat_change = False
titlehome = py.transform.scale(py.image.load(chemin+"/background.tif").convert_alpha(), (int(3760/4),int(1719/4)))
fondhome = py.transform.scale(py.image.load(chemin+"/background1.tif").convert_alpha(), (int((screen_height*3760)/2080), screen_height))
ground_set= py.transform.scale(py.image.load(chemin+"/ground_set.png").convert_alpha(), ((screen_width, screen_height)))
son = py.transform.scale(py.image.load(chemin+"/sound.png").convert_alpha(), (32, 32))
parametre = py.transform.scale(py.image.load(chemin+"/setting.png").convert_alpha(), (32, 32))
homeicon = py.transform.scale(py.image.load(chemin+"/homeicon.png").convert_alpha(), (32, 32))
portalicon = py.transform.scale(py.image.load(chemin+"/portalicon.png").convert_alpha(), (45, 46))
title_border = 0
b_w = int(255*1)
b_h = int(95*1)
b_espacement = 10
b_jouer = py.transform.scale(py.image.load(chemin+"/butom play.png").convert_alpha(), (b_w, b_h))
b_creatif = py.transform.scale(py.image.load(chemin+"/butom create.png").convert_alpha(), (b_w, b_h))
b_tuto = py.transform.scale(py.image.load(chemin+"/butom exit.png").convert_alpha(), (b_w, b_h))

win=False
gameover=False

vit_sprite = 15
x_maze = 10
y_maze = 10
vit_maze = 6
py.key.set_repeat(20, 5)
Level = 1
Score = 0
charging_phase = 0
size_icon_crea = [32,32]
desert_ico = py.transform.scale(py.image.load("Ekulo/imageload/desert.png").convert_alpha(), (128,128))
castle_ico = py.transform.scale(py.image.load("Ekulo/imageload/castle.png").convert_alpha(), (128,128))
plus1 = py.transform.scale(py.image.load(chemin+"/plus.png").convert_alpha(), size_icon_crea)
plus2 = py.transform.scale(py.image.load(chemin+"/plus.png").convert_alpha(), size_icon_crea)
plus3 = py.transform.scale(py.image.load(chemin+"/plus.png").convert_alpha(), size_icon_crea)
plus4 = py.transform.scale(py.image.load(chemin+"/plus.png").convert_alpha(), size_icon_crea)
moins4 = py.transform.scale(py.image.load(chemin+"/moins.png").convert_alpha(), size_icon_crea)
moins1 = py.transform.scale(py.image.load(chemin+"/moins.png").convert_alpha(), size_icon_crea)
moins2 = py.transform.scale(py.image.load(chemin+"/moins.png").convert_alpha(), size_icon_crea)
moins3 = py.transform.scale(py.image.load(chemin+"/moins.png").convert_alpha(), size_icon_crea)
button_plus_crea = [plus1,plus2,plus3,plus4]
button_moins_crea = [moins1,moins2,moins3,moins4]
title_crea = ["Player speed ( pixel ) :","labyrinth width ( Ua ) :","labyrinth height ( Ua ) :","time ( s ) :"]
value_crea = [6,10,10,20]
value_lim_crea = [(5,11),(6,300),(6,300),(10,300)]
pos_base_crea = 200
inter_crea = 160
space_w_crea = 40
go_phase = 1
time_check=False
game_temps=30

txtHS = open("Ekulo/Paramètre/Hight score.txt","r")
H_score = int(txtHS.read())
txtHS.close()

py.mixer.init()
music = py.mixer.music.load(chemin+"/musique.mp3")
py.mixer.music.play()
sonphase=1

# //-------------------------------------------// event

continuer = True
while continuer:
    py.display.flip()
    click = False
    UP,LEFT,RIGHT,DOWN = False,False,False,False
    for event in py.event.get():
        if event.type == py.QUIT:
            continuer = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                continuer = False
            if event.key == py.K_UP:
                UP = True    
            if event.key == py.K_RIGHT:
                RIGHT = True    
            if event.key == py.K_LEFT:
                LEFT = True    
            if event.key == py.K_DOWN:
                DOWN = True    
            
        if event.type == py.MOUSEBUTTONUP:
            click = True
    if page_etat_change == True:
        screen.fill(background_color)
    
    if page == "chargement":
        #code pour le jeu ------------------------------------ /;/
        #chargement
        if charging_phase == 0:
            screen.fill(background_color)
            screen.blit(font_level.render("Level "+str(Level),True,(255,255,255)),(40,int(screen_height/4)))
            screen.blit(font_score.render("score "+str(Score),True,(255,255,255)),(60,int(screen_height/4+screen_height/5+100)))
            screen.blit(font_game.render("Temps : +"+str(vit_maze+4)+"s",True,(255,255,255)),(60,screen_height-65))

            charging_phase=1
        else:
            if time_check==False:
                game_temps+=vit_maze+4
                #-((25*(Level**4))/24)+((115*(Level**3))/12)-((695*(Level**2))/24)+((485*Level)/12)
                #int(-((17*((x_maze+y_maze)**5))/10063872)+((755*((x_maze+y_maze)**4))/(718848))-((34835*((x_maze+y_maze)**3))/(314496))+((212125*((x_maze+y_maze)**2))/(44928))-((1157251*(x_maze+y_maze))/(13104))+(8075/13))
            time_check=False
            win=False
            gameover=False
            maze_matrice = create_maze(x_maze,y_maze)
            y_cel_maze=len(maze_matrice)
            x_cel_maze=len(maze_matrice[0])
            ddd = int(screen_height/7)
            maze_img = py.transform.scale(py.image.load(load_maze(maze_matrice)).convert(),(x_cel_maze*ddd,y_cel_maze*ddd))
            sizeblock = maze_img.get_size()[0]/x_cel_maze
            x_pos_maze = int((screen_width/2)-(1.5*sizeblock))
            y_pos_maze = int((screen_height/2)-(1.5*sizeblock))
            w_k,h_k = (maze_img.get_size()[0]/x_cel_maze)-50,(maze_img.get_size()[1]/x_cel_maze)-50
            w_k,h_k = int(sizeblock*0.75),int(sizeblock*0.75)
            tileset = py.transform.scale(py.image.load(chemin+"/knight.png").convert_alpha(), (int(w_k*4),int(h_k*4)))
            w,h = tileset.get_size()
            tilew,tileh = int(w//4),int(h//4)
            image = [[tileset.subsurface(x,y,tilew,tileh) for x in range(0,w,tilew)] for y in range(0,h,tileh)]
            direction = 0
            img_id = 0
            Pile = []
            img_delay = 0
            tpressed = 0
            img_portal=0
            img_portal_id=0
            portal = py.transform.scale(py.image.load(chemin+"/p"+str(img_portal+1)+".png").convert_alpha(), (int(sizeblock), int(sizeblock)))
            
            for xxx in range(len(maze_matrice[0])):
                for yyy in range(len(maze_matrice)):
                    if maze_matrice[yyy][xxx] == 3:
                        coor_portal = (yyy+0.5,xxx+0.5)
            def colide(w,h,sw,sh,xp,yp,win):
                prx1 = int((int((((sw/2)-xp)-(w/2))+20))/sizeblock)
                prx2 = int((int((((sw/2)-xp)+(w/2))-20))/sizeblock)
                pry = int((int((((sh/2)-yp)+(h/2))-5))/sizeblock)
                if maze_matrice[pry][prx1] == 0 and maze_matrice[pry][prx2] == 0:
                    return True,win
                elif maze_matrice[pry][prx1] == 3 or maze_matrice[pry][prx2] == 3:
                    win = True
                    return True,win
                else:
                    return False,win
            time.sleep(1)
            screen.fill(background_color)
            debut_temps = time.time()
            charging_phase=0
            page = "game"
                
    if page == "home":
        #code pour l'acceuil --------------------------------- /;/
        
        if click:
            if detect_col(py.mouse.get_pos(),b_jouer,(int(screen_width/2)-int(b_w/2),titlehome.get_size()[1]+(title_border*2))):
                page_etat_change = True
                page = "chargement"
            if detect_col(py.mouse.get_pos(),b_creatif, (int(screen_width/2)-int(b_w/2),titlehome.get_size()[1]+(title_border*2)+b_h+b_espacement)):
                page_etat_change = True
                page = "creatif"
            if detect_col(py.mouse.get_pos(),b_tuto, (int(screen_width/2)-int(b_w/2),titlehome.get_size()[1]+(title_border*2)+(b_h*2)+(b_espacement*2))):
                page_etat_change = True
                continuer = False
            if detect_col(py.mouse.get_pos(),son,(screen_width-104,20)):
                if sonphase==1:
                    son = py.transform.scale(py.image.load(chemin+"/soundoff.png").convert_alpha(), (32, 32))
                    py.mixer.music.pause()
                    sonphase = 0
                else:
                    son = py.transform.scale(py.image.load(chemin+"/sound.png").convert_alpha(), (32, 32))
                    py.mixer.music.unpause()
                    sonphase=1
            if detect_col(py.mouse.get_pos(),parametre,(screen_width-52,20)):
                page = "setting"
                
        screen.blit(fondhome, (0,0))
        screen.blit(b_jouer, (int(screen_width/2)-int(b_w/2),titlehome.get_size()[1]+(title_border*2)))
        screen.blit(b_creatif, (int(screen_width/2)-int(b_w/2),titlehome.get_size()[1]+(title_border*2)+b_h+b_espacement))
        screen.blit(b_tuto, (int(screen_width/2)-int(b_w/2),titlehome.get_size()[1]+(title_border*2)+(b_h*2)+(b_espacement*2)))
        screen.blit(titlehome, (int(screen_width/2)-int(titlehome.get_size()[0]/2),0+title_border))
        screen.blit(son, (screen_width-104,20))
        screen.blit(parametre, (screen_width-52,20))
        screen.blit(font_game.render("Hight score : "+str(H_score),True,(255,255,255)),(20,screen_height-60))
               
    if page == "game":
        #code pour le jeu ------------------------------------ /;/
        actuel_temps = time.time()
        chrono = actuel_temps-debut_temps
        colide_check,win = colide(w_k,h_k,screen_width,screen_height,x_pos_maze,y_pos_maze,win)
        if win:
            x_maze+= 2
            y_maze+= 2
            Level+=1
            game_temps = round(game_temps-chrono)
            Score+= r.randint(300,350)
            if vit_maze < 10:
                vit_maze+= 1
                vit_sprite+=2
            page_etat_change = True
            page="chargement"

        if gameover or round(game_temps-chrono) == 0:
            game_temps=15
            if Score > H_score:
                H_score = Score
            page="gameover"
            
        if colide_check:
            if UP:
                screen.blit(maze_img, (x_pos_maze,y_pos_maze-vit_maze))
                y_pos_maze = y_pos_maze+vit_maze
                Pile.append((x_pos_maze,y_pos_maze-vit_maze))
                direction = 3
                tpressed = 1
            elif DOWN:
                screen.blit(maze_img, (x_pos_maze,y_pos_maze+vit_maze))
                y_pos_maze = y_pos_maze-vit_maze
                Pile.append((x_pos_maze,y_pos_maze+vit_maze))
                direction = 0
                tpressed = 1
            elif LEFT:
                screen.blit(maze_img, (x_pos_maze+vit_maze,y_pos_maze))
                x_pos_maze = x_pos_maze+vit_maze
                Pile.append((x_pos_maze-vit_maze,y_pos_maze))
                direction = 1
                tpressed = 1
            elif RIGHT:
                screen.blit(maze_img, (x_pos_maze-vit_maze,y_pos_maze))
                x_pos_maze = x_pos_maze-vit_maze
                Pile.append((x_pos_maze+vit_maze,y_pos_maze))
                direction = 2
                tpressed = 1
            else:
                screen.blit(maze_img, (x_pos_maze,y_pos_maze))
        else:
            screen.blit(maze_img, (Pile[len(Pile)-1]))
            x_pos_maze,y_pos_maze = Pile[len(Pile)-1]
        
        img_portal_id+=1
        if img_portal_id == vit_sprite:
            if img_portal == 3:
                img_portal=0
            else:
                img_portal+=1
            portal = py.transform.scale(py.image.load(chemin+"/p"+str(img_portal)+".png").convert_alpha(), (int(sizeblock), int(sizeblock)))
            img_portal_id = 0
        screen.blit(portal,(int(x_pos_maze+((coor_portal[1]-0.5)*sizeblock)),int(y_pos_maze+((coor_portal[0]-0.5)*sizeblock))))
        if tpressed == 1:
            img_delay+=1
            if img_delay == vit_sprite:
                if img_id == 3 and img_delay:
                    img_id=0
                else:
                    img_id+=1
                img_delay = 0
            tpressed = 0
        screen.blit(image[direction][img_id],(int(screen_width/2)-w_k/2,int(screen_height/2)-h_k/2))

        screen.blit(son, (screen_width-104,20))
        screen.blit(homeicon, (screen_width-52,20))
        screen.blit(portalicon, (0,0))
        screen.blit(font_game.render(" "+str(round(sqrt((coor_portal[1]-(((screen_width/2)-x_pos_maze)/sizeblock))**2+(coor_portal[0]-(((screen_height/2)-y_pos_maze)/sizeblock))**2),2))+" m",True,(192,57,43),(38,38,43)),(45,0))
        screen.blit(font_time.render(str(round(game_temps-chrono))+" s",True,(255,255,255),(38,38,43)),(screen_width/2-80,0))
        
        if click:
            if detect_col(py.mouse.get_pos(),homeicon, (screen_width-52,20)):
                page_etat_change = True
                gameover = True
            if detect_col(py.mouse.get_pos(),son,(screen_width-104,20)):
                if sonphase==1:
                    son = py.transform.scale(py.image.load(chemin+"/soundoff.png").convert_alpha(), (32, 32))
                    py.mixer.music.pause()
                    sonphase = 0
                else:
                    son = py.transform.scale(py.image.load(chemin+"/sound.png").convert_alpha(), (32, 32))
                    py.mixer.music.unpause()
                    sonphase=1
        

    if page == "setting":
        #code pour la demo partie 1 -------------------------- /;/
        coin = (100,100)
        
        screen.blit(ground_set,(0,0))
        screen.blit(homeicon,  (screen_width-coin[0]-32,coin[1]))
        screen.blit(font_game.render("Setting :",True,(255,255,255)),coin)
        screen.blit(font_game.render("Texture pack : (toute modification demandera un redemarrage avant de fonction)",True,(255,255,255)),(coin[0]+40,coin[1]+100))
        value_set = ["desert","castle"]
        icon_set = [desert_ico,castle_ico]
        for i in range(len(value_set)):
            screen.blit(icon_set[i],(coin[0]+80+i*(128+30),coin[1]+160))
        if click:
            if detect_col(py.mouse.get_pos(),icon_set[0], (coin[0]+80+0*(128+30),coin[1]+160)):
                chemin="Ekulo/texture pack/"+value_set[0]
                page = "home"
            if detect_col(py.mouse.get_pos(),icon_set[1], (coin[0]+80+1*(128+30),coin[1]+160)):
                chemin="Ekulo/texture pack/"+value_set[1]
                page = "home"
            if detect_col(py.mouse.get_pos(),homeicon, (screen_width-coin[0]-32,coin[1])):
                page_etat_change = True
                page = "home"
            
    if page == "creatif":
        #code pour le creatif -------------------------------- /;/
        screen.blit(font_game.render("Creative mode    (this is Beta version)",True,(255,255,255)),(60,60))
        screen.blit(homeicon, (screen_width-52,20))

        for i in range(4):
            screen.blit(font_game.render(title_crea[i],True,(255,255,255)),(60+space_w_crea,(pos_base_crea-size_icon_crea[1]-inter_crea/4)+(inter_crea*1)*i))
            screen.blit(button_moins_crea[i],(60+space_w_crea*2,pos_base_crea+(inter_crea*1)*i))
            screen.blit(button_plus_crea[i],(60+space_w_crea*2+size_icon_crea[0]+10,pos_base_crea+(inter_crea*1)*i))
            screen.blit(font_game.render(str(value_crea[i]),True,(255,255,255)),(60+space_w_crea*2+(size_icon_crea[0]+10)*2,pos_base_crea+(inter_crea*1)*i))
        screen.blit(b_jouer, (60+space_w_crea,pos_base_crea+(inter_crea)*3.5))
        
        if click:
            if detect_col(py.mouse.get_pos(),homeicon, (screen_width-52,20)):
                page_etat_change = True
                page = "home"
            for i in range(4):
                if value_crea[i] <= value_lim_crea[i][1] and detect_col(py.mouse.get_pos(),button_plus_crea[i],(60+space_w_crea*2+size_icon_crea[0]+10,pos_base_crea+(inter_crea*1)*i)):
                    value_crea[i] += 1
                if value_crea[i] >= value_lim_crea[i][0] and detect_col(py.mouse.get_pos(),button_moins_crea[i],(60+space_w_crea*2,pos_base_crea+(inter_crea*1)*i)):
                    value_crea[i] -= 1
            if detect_col(py.mouse.get_pos(),b_jouer,(60+space_w_crea,pos_base_crea+(inter_crea)*3.5)):
                x_maze= value_crea[2]
                y_maze= value_crea[1]
                Level=1
                Score=0
                time_check=True
                game_temps=value_crea[3]
                vit_maze= value_crea[0]
                page_etat_change = True
                page="chargement"
                
    
    if page == "gameover":
        #code pour la demo partie 1 -------------------------- /;/
        if go_phase==1:
            #gameover
            vit_maze = 6
            screen.fill(background_color)
            screen.blit(font_score.render("Game over",True,(214, 48, 49)),(int(screen_width/2-(800/2)),int(screen_height/2-(200))))
            screen.blit(font_score.render("score "+str(Score),True,(255,255,255)),(int(screen_width/2-(800/2))+60,int(screen_height/2-(150))))
            go_phase=0
        else:
            Level = 1
            Score = 0
            time.sleep(4)
            go_phase=1
            page="home"

os.remove("Ekulo/Paramètre/chemin.txt")
os.remove("Ekulo/Paramètre/Hight score.txt")
open("Ekulo/Paramètre/Hight score.txt", "w").write(str(H_score))
open("Ekulo/Paramètre/chemin.txt", "w").write(chemin)
py.quit()

#//------------------------------------------// Code source
"""
                screen.blit(perso, (perso_coo[0],perso_coo[1]))
                screen.blit(fond, (0,0))
                print(screen.get_at((20, 20)))
                perso = py.image.load(chemin+"/perso.png").convert_alpha()
                perso_coo = [0,0]
                perso_vit = 10
                py.key.set_repeat(1,20)
                fond = py.image.load(load_maze(create_maze(int(screen_height/32)-1,int(screen_width/32)-1))).convert()
                title = load_maze(create_maze(x,y))
"""
"""
                if event.key == py.K_LEFT:
                    screen.blit(perso, (perso_coo[0]-perso_vit,perso_coo[1]))
                    perso_coo[0]=perso_coo[0]-perso_vit
                    screen.fill(background_color)
                if event.key == py.K_RIGHT:
                    screen.blit(perso, (perso_coo[0]+perso_vit,perso_coo[1]))
                    perso_coo[0]=perso_coo[0]+perso_vit
                    screen.fill(background_color)
                if event.key == py.K_UP:
                    screen.blit(perso, (perso_coo[0],perso_coo[1]-perso_vit))
                    perso_coo[1]=perso_coo[1]-perso_vit
                    screen.fill(background_color)
                if event.key == py.K_DOWN:
                    screen.blit(perso, (perso_coo[0],perso_coo[1]+perso_vit))
                    perso_coo[1]=perso_coo[1]+perso_vit
                    screen.fill(background_color)
"""
"""
        print(colide(w_k,h_k,screen_width,screen_height,x_pos_maze,y_pos_maze))
        if colide(w_k,h_k,screen_width,screen_height,x_pos_maze,y_pos_maze):
            if DOWN:
                screen.blit(maze_img, (x_pos_maze,y_pos_maze-vit_maze))
                y_pos_maze = y_pos_maze-vit_maze
                Pile.append((x_pos_maze,y_pos_maze-vit_maze))
            elif UP:
                screen.blit(maze_img, (x_pos_maze,y_pos_maze+vit_maze))
                y_pos_maze = y_pos_maze+vit_maze
                Pile.append((x_pos_maze,y_pos_maze+vit_maze))
            elif LEFT:
                screen.blit(maze_img, (x_pos_maze+vit_maze,y_pos_maze))
                x_pos_maze = x_pos_maze+vit_maze
                Pile.append((x_pos_maze-vit_maze,y_pos_maze))
            elif RIGHT:
                screen.blit(maze_img, (x_pos_maze-vit_maze,y_pos_maze))
                x_pos_maze = x_pos_maze-vit_maze
                Pile.append((x_pos_maze+vit_maze,y_pos_maze))
            else:
                screen.blit(maze_img, (x_pos_maze,y_pos_maze))
                screen.blit(knight,(int(screen_width/2)-w_k/2,int(screen_height/2)-h_k/2))
        else:
            screen.blit(maze_img, (Pile[len(Pile)-1]))
            x_pos_maze,y_pos_maze = Pile[len(Pile)-1]
            screen.blit(knight,(int(screen_width/2)-w_k/2,int(screen_height/2)-h_k/2))
"""



