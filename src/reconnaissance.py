from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    image=image.binarisation(S)
    image=image.localisation()
    chiffre=0
    simili=0
    for i in range(len(liste_modeles)):
        image1=liste_modeles[i]
        image=image.resize(image1.H,image1.W)
        resultat_image=image.similitude(image1)
        if resultat_image>simili:
            simili=resultat_image
            chiffre=i
    return chiffre

