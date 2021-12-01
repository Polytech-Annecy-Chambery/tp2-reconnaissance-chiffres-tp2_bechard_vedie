from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):
        im_bin = Image()
        im_bin.set_pixels(np.zeros((self.H, self.W), dtype=np.uint8))
        for i in range(len(im_bin.pixels)):
            for j in range(len(im_bin.pixels[0])):
                if self.pixels[i][j]<=S:
                    im_bin.pixels[i][j]=0
                else:
                    im_bin.pixels[i][j]=255
        return im_bin


    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
        im_loc=Image()
        l_max=0
        l_min=self.H-1
        c_max=0
        c_min=self.W-1
        for l in range(len(self.pixels)):
            for c in range(len(self.pixels[0])):
                if l<l_min:
                    if self.pixels[l][c]==0:
                        l_min=l
                elif l>=l_max:
                    if self.pixels[l][c]==0:
                        l_max=l
                if c<c_min:
                    if self.pixels[l][c]==0:
                        c_min=c
                elif c>=c_max:
                    if self.pixels[l][c]==0:
                        c_max=c
        im_loc.set_pixels(self.pixels[l_min:l_max,c_min:c_max])
        return im_loc

    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):
        newImage=Image()
        pixels_resized=resize(self.pixels,(new_H,new_W),0)
        newImage.set_pixels(np.uint8(pixels_resized*255))
        return newImage


    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
        compte=0
        similitu=0
        for l in range(len(self.pixels)):
            for c in range(len(self.pixels[0])):
                compte=compte+1
                if self.pixels[l][c]==im.pixels[l][c]:
                    similitu=similitu+1
        return (similitu/compte)
                
                

