import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict, Union


class Noeud():
    def __init__(self, identifiant_unique: int, nom: str, droits_acces: str):
        self.identifiant_unique = identifiant_unique
        self.nom = nom
        self.droits_acces = droits_acces
        self.date_creation = datetime.now()
        self.date_derniere_modification = datetime.now()

    @abstractmethod
    def open(self):
        pass
    def afficher(self):
        print(self.nom)

    def allInfo(self) :
        return "Id:" +str(self.identifiant_unique) + " \n Nom : " + self.nom + "\n Droits d'accès : " + self.droits_acces + "\n Date de création : " + str(self.date_creation) + "\n Date de dernière modification : " + str(self.date_derniere_modification)

class Repertoire(Noeud):
    def __init__(self, identifiant_unique: int, nom: str, droits_acces: str):
        super().__init__(identifiant_unique, nom, droits_acces)
        self.enfants = []

    def open(self) -> List[Noeud]:
        for i in self.enfants:
            print(i.allInfo())
        return self.enfants
    
    def allInfo(self):
            return  str(Noeud.allInfo(self))

class Lecteur(ABC):
    @abstractmethod
    def associer_lecteur(self, fichier):
        #if not isinstance(fichier, Fichier):
            #raise ValueError("Le paramètre doit être une instance de la classe Fichier")
             #fichier.lecteur = self
        pass
    def play(self):
        print("Lecture en cours")
        pass

class LecteurMultimedia(Lecteur):
    def associer_lecteur(self, fichier):
        fichier.lecteur = self

    def lecture(self):
        pass

    def pause(self):
        pass

    def avancer(self):
        pass

    def reculer(self):
        pass

class LecteurDocument(Lecteur):
    def associer_lecteur(self, fichier):
        fichier.lecteur = self

    def zoom(self):
        pass

class Fichier(Noeud):
    def __init__(self, identifiant_unique: int, nom: str, droits_acces: str, lecteur: Lecteur):
        Noeud.__init__(self, identifiant_unique, nom, droits_acces)
        self.enfants = []
        self.lecteur = lecteur

    def open(self):
        self.lecteur.associer_lecteur(self)
        self.lecteur.play()
    
    def allInfo(self):
        return  str(Noeud.allInfo(self))
class FichierAudio(Fichier):
    def __init__(self, identifiant_unique: int, nom: str, droits_acces: str, lecteur: LecteurMultimedia):
        super().__init__(identifiant_unique, nom, droits_acces,lecteur)
        self.lecteur = lecteur

    def open(self):
        self.lecteur.play()
        

class Audio(FichierAudio):
    def open(self):
        self.lecteur.play()
        

class Video(FichierAudio):
    def open(self):
        self.lecteur.play()
        

class FichierDoc(Fichier):
    def __init__(self, identifiant_unique: int, nom: str, droits_acces: str, lecteur: LecteurDocument):
        super().__init__(identifiant_unique, nom, droits_acces,lecteur)
        self.lecteur = lecteur

    def open(self):
        self.lecteur.play()
        
    def allInfo(self):
        return  str(Noeud.allInfo(self))
    
class pdf(FichierDoc):
    def __init__(self, identifiant_unique: int, nom: str, droits_acces: str, lecteur: LecteurDocument):
        super().__init__(identifiant_unique, nom, droits_acces, lecteur)
        self.lecteur = lecteur

    def open(self):
        self.lecteur.play()
       

class Image(FichierDoc):
    def __init__(self, identifiant_unique: int, nom: str, droits_acces: str, lecteur: LecteurDocument):
        super().__init__(identifiant_unique, nom, droits_acces, lecteur)
        self.lecteur = lecteur
    def open(self):
        self.lecteur.play()
    

class Peripherique(Noeud):
    def __init__(self, identifiant_unique: int, nom: str, droits_acces: str, monte: bool = False):
        super().__init__(identifiant_unique, nom, droits_acces)
        self.enfants = []
        self.monte = monte

    def open(self) -> List[Noeud]:
        if self.monte:
            for i in self.enfants:
                print(i.allInfo())
            return self.enfants
        else : 
            raise ValueError("Le périphérique n'est pas monté")

    def monter(self):
        self.monte = True

    def demonter(self):
        self.monte = False

    def allInfo(self):
        return  str(Noeud.allInfo(self))

class Unix:
    def __init__(self):
        self.noeuds = {}

    def ajouter_noeud(self, noeud: Noeud):
        if noeud.identifiant_unique in self.noeuds:
            raise ValueError("Ce noeud existe déjà")
        self.noeuds[noeud.identifiant_unique] = noeud

    def obtenir_noeud(self, identifiant_unique: int) :
        if identifiant_unique not in self.noeuds:
            raise ValueError("Ce noeud n'existe pas")
        return self.noeuds[identifiant_unique]
    
    def afficher_arborescence(self):
           for noeud in self.noeuds.values():
                noeud.afficher()

class Application(tk.Tk):
    def __init__(self, système):
        super().__init__()
        self.title("Interface graphique")
        self.système = système

        self.create_widgets()
        self.mainloop() 

    def create_widgets(self):
        self.listbox = tk.Listbox(self)
        self.listbox.grid(row=1, column=3)
        self.geometry("800x500")
        self.config(bg="white")
        self.label = tk.Label(self, text="UNIX", bg="white", fg="black", font=("Arial", 27))
        self.listbox.bind('<<ListboxSelect>>', lambda event: self.afficher_infos())    
        self.label.grid(row=0, column=8)
        self.button_open = tk.Button(self, text="Open", command=self.open_noeud)
        self.button_open.grid(row=2, column=8)

        #bouton quitter 
        self.bouton_quitter = tk.Button(self, text='Quitter', command=self.destroy)
        self.bouton_quitter.grid(row=9, column=8)

        # Ajout des nœuds à la liste
        for identifiant, noeud in self.système.noeuds.items():
            self.listbox.insert(tk.END, noeud.nom)

    def afficher_infos(self, event=None):
        # Récupérer l'indice de l'élément sélectionné
        if self.listbox.curselection() != () :
            index = self.listbox.curselection()[0] + 1 
            N = self.système.noeuds[index]
            message = N.allInfo()
             #if hasattr(self, 'label_message'):
                #self.label_message.destroy()  # Supprimer l'ancien message
            self.label_message = tk.Label(self, text=message)
            self.label_message.grid(row=8,column=8)

    def open_noeud(self):
        # Récupération de l'indice du nœud sélectionné dans la liste
        index = self.listbox.curselection()
        if index:
            index = index[0]
            noeud_nom = self.listbox.get(index)

            # Recherche du nœud correspondant dans le système
            for identifiant, noeud in self.système.noeuds.items():
                if noeud.nom == noeud_nom:
                    if isinstance(noeud, Repertoire):
                        # Ouvrir un répertoire en affichant ses enfants
                        enfants = noeud.open()
                        if enfants != []:
                            for enfant in enfants:
                                print(enfant.allInfo())
                        else:
                            raise Exception("Le répertoire est vide")
                    elif isinstance(noeud, Fichier):
                        # Ouvrir un fichier en utilisant le lecteur associé
                        lecteur = noeud.open()
                        if lecteur is not None:
                            print("Lecteur associé : ", lecteur)
                        else:
                            raise Exception ("Le fichier n'a pas de lecteur associé")
                    elif isinstance(noeud, Peripherique):
                        # Ouvrir un périphérique monté en affichant ses enfants
                        if noeud.monte:
                            enfants = noeud.open()
                            if enfants :
                                for enfant in enfants:
                                    print(enfant.allInfo())
                            else :
                                raise Exception("Le périphérique est vide")
                        else:
                            raise Exception("Le périphérique n'est pas monté")
                    else:
                        raise Exception("Le type du nœud n'est pas reconnu")
        else:
            raise Exception("Il n'y a pas de noeud à cet emplacement")
        
if __name__ == '__main__':
    Système = Unix()

    
    # Question 2 
    LecteurMultimedia1 = LecteurMultimedia()
    test = FichierAudio(10, "Cours", "read", LecteurMultimedia1)
    LecteurMultimedia1.associer_lecteur(test)
    repertoire1 = Repertoire(1, "Repertoire Musique ", "read")
    fichier1 = Fichier(2, "Cours Musique ", "read", LecteurDocument())
    FichierAudio1 = FichierAudio(3, "Devoirs Musique ", "read", LecteurMultimedia1)
    FichierDoc1 = FichierDoc(4, "APP", "read", LecteurMultimedia1)
    Peripherique1 = Peripherique(5, "Cours POO", "read", True)
    Image1 = Image(7, "Java", "read", LecteurDocument())
    Fichier2 = Fichier(8, "Cours ", "read", LecteurMultimedia1)
    Fichier3 = Fichier(9, "Devoirs ", "read", LecteurDocument())


    repertoire1.enfants.append(FichierAudio(2, "Cours", "read", LecteurMultimedia1))
    repertoire1.enfants.append(FichierAudio(3, "Devoirs", "read", LecteurMultimedia1))
    fichier1.enfants.append(FichierDoc(4, "APP", "read", LecteurDocument()))

    Système.ajouter_noeud(repertoire1)
    Système.ajouter_noeud(fichier1)
    Système.ajouter_noeud(FichierAudio1)
    Système.ajouter_noeud(FichierDoc1)
    Système.ajouter_noeud(Peripherique1)
    Système.ajouter_noeud(test)

    noeud = Système.obtenir_noeud(1)

    Système.afficher_arborescence()

    #question 3

    app = Application(Système)
