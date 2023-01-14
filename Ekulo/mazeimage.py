from PIL import Image
import random as r
dn=32

ch = open("Ekulo/Paramètre/chemin.txt","r")
chemin = str(ch.read())
ch.close()

#On apelle la texture Wall_a
Wall_a=Image.open(chemin+"/Wall_a.png")

#On apelle la texture Floor
Floor=Image.open(chemin+"/Floor.png")

#On apelle la texture Ground
Ground=Image.open(chemin+"/Ground.png")

#On apelle la texture Ground_shadow
Ground_shadow=Image.open(chemin+"/Ground_shadow.png")

#on définit la couleur de l'image que l'on veut créer
fond=(0,0,0)

def ground(ab,ordo,im):
    for fg in range(dn):
        for ffg in range(dn):
            coord=((ab+fg),(ordo+ffg))
            coord_get=(fg,ffg)
            couleur=Ground.getpixel(coord_get)
            im.putpixel(coord, couleur)

    
def wall(ab,ordo,im):
    for fw in range(dn):
        for ffw in range(dn):
            coord=((ab+fw),(ordo+ffw))
            coord_get=(fw,ffw)
            couleur=Wall_a.getpixel(coord_get)
            im.putpixel(coord, couleur)
    

def floor (ab,ordo,im):
    for fw in range(dn):
        for ffw in range(dn):
            coord=((ab+fw),(ordo+ffw))
            coord_get=(fw,ffw)
            couleur=Floor.getpixel(coord_get)
            im.putpixel(coord, couleur)

def shadowground(ab,ordo,im):
    for fg in range(dn):
        for ffg in range(dn):
            coord=((ab+fg),(ordo+ffg))
            coord_get=(fg,ffg)
            couleur=Ground_shadow.getpixel(coord_get)
            im.putpixel(coord, couleur)

def load_maze(laby):
    #len(laby)=hauteur
    #len(laby[0])=largeur
    #on définit la taille de l'image que l'on veut créer
    taille=(len(laby[0])*dn,len(laby)*dn)
    #c'est cette ligne qui fabrique l'image
    im=Image.new("RGB", taille, fond)
    for f in range(len(laby)):
        for ff in range(len(laby[0])):
            ab=ff*dn
            ordo=f*dn
            
            if laby[f][ff]==1:
                if f<len(laby)-1:
                    if laby[f+1][ff]==1:
                        floor(ab,ordo,im)
                    else:
                        wall(ab,ordo,im)
                else:
                    wall(ab,ordo,im)

            elif laby[f][ff]==0 or laby[f][ff]==3:

                if laby[f][ff-1]==1:
                    shadowground(ab,ordo,im)
                else:
                    ground(ab,ordo,im)
        
    title = "Ekulo/imageload/" + str(r.randint(1,20)) + ".png"
    # et enfin on enregistre cette image
    im.save(title,quality=95)
    return title

def load_maze_home(laby):
    #len(laby)=hauteur
    #len(laby[0])=largeur
    #on définit la taille de l'image que l'on veut créer
    taille=(len(laby[0])*dn,len(laby)*dn)
    #c'est cette ligne qui fabrique l'image
    im=Image.new("RGB", taille, fond)
    for f in range(len(laby)):
        for ff in range(len(laby[0])):
            ab=ff*dn
            ordo=f*dn
            
            if laby[f][ff]==1:
                if f<len(laby)-1:
                    if laby[f+1][ff]==1:
                        black(ab,ordo,im)
                    else:
                        black(ab,ordo,im)
                else:
                    black(ab,ordo,im)

            elif laby[f][ff]==0:

                if laby[f][ff-1]==1:
                    white(ab,ordo,im)
                else:
                    white(ab,ordo,im)

    viewtt = r.randint(0,100)
    title = "imageload/home/" + str(viewtt) + ".png"
    # et enfin on enregistre cette image
    im.save(title,quality=95)
    return title

def white(ab,ordo,im):
    for fg in range(dn):
        for ffg in range(dn):
            coord=((ab+fg),(ordo+ffg))
            couleur=(255,255,255)
            im.putpixel(coord, couleur)

def black(ab,ordo,im):
    for fg in range(dn):
        for ffg in range(dn):
            coord=((ab+fg),(ordo+ffg))
            couleur=(38,38,43)
            im.putpixel(coord, couleur)



            
            
            
