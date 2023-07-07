import random
import math
import tkinter as tk
from tkinter import ttk
    
class Personnage:

    def __init__(self, nom, x=0 ,y=0, pv=100):
        self.__nom = nom
        self.__pv = pv
        self.est_mort = self.statut()
        self.__x = x
        self.__y = y
        self.__norme = 0 


    def get_pv(self):
            return self.__pv
    
    def set_pv(self, pv):
        self.__pv = pv
        self.statut()

    def get_position(self):
        return self.__x, self.__y
    
    def set_position(self, x, y):
        self.__x = x
        self.__y= y
    
    def norme(self):
        self.__norme = math.sqrt((self.__x)**2+(self.__y)**2)
        norme_actuelle = self.__norme
        return round(norme_actuelle,3)
    
    def statut(self):
        if self.__pv > 0 :
            self.est_mort =   False
        elif self.__pv <= 0 :
           self.est_mort =  True
    
    def allInfo(self) :
        return "Nom :" +self.__nom+ " \n Type : <' " + str(type(self))[17:] + "\n PV : " +str(self.__pv) + " \n Position " +  str((self.__x, self.__y)) + "\n Vivant  : " + str(not self.est_mort) 
    
    def distance(self, p1):
		    return math.sqrt((self.__x-p1.__x)**2+(self.__y-p1.__y)**2)


class Combattant:
  
    def attaquer(self):
         def attaquer(self, personnage: Personnage):
            try :
                if personnage.get_pv() > 0 :
                    newpv  = personnage.get_pv() - self.__pa
                    personnage.set_pv(newpv) 
                else :
                    print("Le personnage est mort")
            except :
                print("Le personnage est mort")     
    
class Guérisseur:
   
    def soigner(self, autre_personnage : Personnage):
            try :
                if autre_personnage.get_pv() > 0 :
                    newpv = autre_personnage.get_pv() + self.__ps
                    autre_personnage.set_pv(newpv) 
                else :
                    print("Le personnage est mort")
            except :
                print("Le personnage est mort") 
    
class Guerrier(Personnage, Combattant):
        
        def __init__(self, nom, pv, pa,x,y):
            Personnage.__init__(self, nom, x, y, pv)
            self.__pa = pa

        def get_pa(self):
            return self.__pa
        
        def attaquer(self, personnage: Personnage):
            try :
                if personnage.get_pv() > 0 and self.get_pv() > 0 :
                    newpv  = personnage.get_pv() - self.__pa
                    personnage.set_pv(newpv) 
                else :
                    print("Le personnage est mort")
            except :
                print("Le personnage est mort")            
        
        def allInfo(self):
            return  str(Personnage.allInfo(self))+ " \n PA : " +str(self.get_pa())+ " \n "
    
  
class GuerrierFou(Guerrier):
         
    def __init__(self,nom,pa,x,y,pv):
        Personnage.__init__(self,nom,x,y,pv)
        Guerrier.__init__(self,nom,pv,pa,x,y)
        
    def attaquer(self,cible : Personnage):
        if self.get_pv() < 10 :
            self.__pa += 10
            newpv = cible.get_pv() - self.__pa
        else :
            newpv = cible.get_pv() - self.__pa

    def allInfo(self):
            return  str(Personnage.allInfo(self))+ " \n PA : " +str(self.get_pa())

class Archer(Guerrier):
         
    def __init__(self,nom,x,y,pv,pa):
        Guerrier.__init__(self,nom,pv,pa,x,y)

         #self et autre_personnage sont les args
    def tirer_flèche(self,autre_personnage : Personnage):
        try :
            if self.distance(autre_personnage) > 0 :
                self.attaquer(autre_personnage)
            else :
                return 0
        except :
            print("Le personnage est mort")
    def allInfo(self):
            return  str(Personnage.allInfo(self))+ "\n PA : " +str(self.get_pa())
          
class Soigneur(Personnage, Guérisseur):

        def __init__(self, nom,x,y,pv,ps):
            Personnage.__init__(self,nom,x,y,pv)
            self.__ps = ps
    
        def get_ps(self):
            return self.__ps
        
        def soigner(self, autre_personnage : Personnage):
            try :
                if autre_personnage.get_pv() > 0 and self.get_pv() > 0:
                    newpv = autre_personnage.get_pv() + self.__ps
                    autre_personnage.set_pv(newpv) 
                else :
                    print("Le personnage est mort")
            except :
                print("Le personnage est mort") 
    
        def allInfo(self):
            return   str(Personnage.allInfo(self))+ "\n PS : " +str(self.get_ps())
        

class Mage( Soigneur):

    def __init__(self,nom,x,y,pv,ps):
        #Personnage.__init__(self, nom, x, y, pv)
        Soigneur.__init__(self,nom,x,y,pv,ps)
        Personnage.statut(self)

    def soigner(self, autre_personnage):
        try :
            if autre_personnage.get_pv() > 0 and self.get_pv() > 0  :
                newpv = autre_personnage.get_pv() + self.__ps
                autre_personnage.set_pv(newpv) 
            else :
                print("Le personnage est mort")
        except :
            print("Le personnage est mort")
    
    def allInfo(self):
        return   str(Personnage.allInfo(self))+ " \n PS : " +str(self.get_ps()) 

class Infirmière(Soigneur):
    def __init__(self,nom,x,y,pv,ps):
        #Personnage.__init__(self,nom,pv)
        Soigneur.__init__(self,nom,ps,x,y,pv)
        
    def soigner(self, autre_personnage):
        try :
            if autre_personnage.get_pv() > 0 and self.get_pv() > 0  :
                newpv = autre_personnage.get_pv() + 2*self.__ps
                autre_personnage.set_pv(newpv) 
            else :
                print("Le personnage est mort")
        except :
            print("Le personnage est mort")
            
    def allInfo(self):
        return   str(Personnage.allInfo(self))+ " \n PS :" +str(self.get_ps())

class Paladin(Combattant, Soigneur):
    def __init__(self,nom, pa, ps,x,y,pv):
        #Personnage.__init__(self, nom)
        Soigneur.__init__(self,nom,ps,x,y,pv)
        Guerrier.__init__(self,nom,pa)

    def attaquer(self, personnage: Personnage):
        try :
            if personnage.get_pv() > 0 and self.get_pv() > 0 :
                newpv  = personnage.get_pv() - self.__pa
                personnage.set_pv(newpv) 
        except :
            print("Le personnage est mort")
    
    def soigner(self, autre_personnage : Personnage):
        try :
            if autre_personnage.get_pv() > 0 and self.get_pv() > 0  :
                newpv = autre_personnage.get_pv() + self.__ps
                autre_personnage.set_pv(newpv) 
            else :
                print("Le personnage est mort")
        except :
            print("Le personnage est mort")

    def allInfo(self):
        return  str(Personnage.allInfo(self))+ " \n PS : " +str(self.get_ps())+ " \n PA : " +str(self.get_pa())
    
    
class Fée(Guerrier,Soigneur):

    def __init__(self,nom,x,y,pv,ps,pa):
        Personnage.__init__(self,nom)
        Soigneur.__init__(self,nom,x,y,pv,ps)
        Guerrier.__init__(self,nom,pv,pa,x,y)
        
      
    def attaquer(self, personnage: Personnage):
            try :
                if personnage.get_pv() > 0 and self.get_pv() > 0 and self.get_pv() > 0 :
                    n = random.randint(1, 2)
                    if n == 1 :
                        newpv  = personnage.get_pv() - self.get_pa()
                        personnage.set_pv(newpv)
                    else :
                        newpv = personnage.get_pv() + self.get_pv()
                        personnage.set_pv(newpv)
            except :
                print("Le personnage est mort")
                 

    def soigner(self, autre_personnage):
            try :
                if autre_personnage.get_pv() > 0 and self.get_pv() > 0 :
                    n= random.randint(1, 2)
                    if n == 1 :
                        newpv = autre_personnage.get_pv() + self.get_pv()
                        autre_personnage.set_pv(newpv)
                    else :
                        newpv = autre_personnage.get_pv() + 2*self.get_pv()
                        autre_personnage.set_pv(newpv)
            except :
                print("Le personnage est mort")
    
    def allInfo(self):
        return  str(Personnage.allInfo(self))+ " \n PS : " +str(self.get_ps()) + " \n PA : " +str(self.get_pa())
    
class Jeu :
        def __init__(self):
            self.personnages = []

        def ajouter_personnage(self, personnage):
            self.personnages.append(personnage)

        def afficher_personnages(self):
            for personnage in self.personnages:
                personnage.afficher()

        def creer_personnage(self,classe,**kwargs):
                
                if  classe == "Guerrier" :
                    personnage=Guerrier(**kwargs)
                elif  classe == "Soigneur" :
                    personnage=Soigneur(**kwargs)
                elif  classe == "GuerrierFou" :
                    personnage=GuerrierFou(**kwargs)
                elif  classe == "Archer" :
                    personnage=Archer(**kwargs)
                elif  classe == "Fée" :
                    personnage=Fée(**kwargs)
                elif  classe == "Mage" :
                    personnage=Mage(**kwargs)
                elif  classe == "Infirmière":
                    personnage=Infirmière(**kwargs)
                elif classe == "Paladin" :
                    personnage=Paladin(**kwargs)
                return personnage
        
        def deplacer_personnage(self,i, dx, dy):
            x,y = self.personnages[i].get_position()
            new_x, new_y = x + dx, y + dy
            self.personnages[i].set_position(new_x, new_y)
        
        def attaquer_personnage(self, index_attaquant, index_cible):
            attaquant = self.personnages[index_attaquant]
            cible = self.personnages[index_cible]
            attaquant.attaquer(cible)

        def soigner_personnage(self, index_soignant, index_cible):
            soignant = self.personnages[index_soignant]
            cible = self.personnages[index_cible]
            soignant.soigner(cible)

        def afficher_infos(self,index:int ):
            personnage = self.personnages[index]
            print(personnage.allInfo())


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.mon_jeu = Jeu()
        self.mon_jeu.ajouter_personnage(self.mon_jeu.creer_personnage(nom="Damien", classe="Guerrier", x=0, y=0, pv=100, pa=100))
        self.mon_jeu.ajouter_personnage(self.mon_jeu.creer_personnage(nom="Amalia", classe="Soigneur", x=0, y=0,pv=100,ps=10))
        self.mon_jeu.ajouter_personnage(self.mon_jeu.creer_personnage(nom="Julia", classe="Mage", x=0, y=0,pv=100,ps=10))
        self.mon_jeu.ajouter_personnage(self.mon_jeu.creer_personnage(nom="Soukaina", classe="Mage", x=0, y=0,pv=100,ps=10))
        self.mon_jeu.ajouter_personnage(self.mon_jeu.creer_personnage(nom="Thomas", classe="Archer", x=0, y=0,pv=100, pa=10))
        self.mon_jeu.ajouter_personnage(self.mon_jeu.creer_personnage(nom="Souleyman", classe="Fée", x=0, y=0,pv=100, pa=10,ps=10))
        self.mon_jeu.ajouter_personnage(self.mon_jeu.creer_personnage(nom="Jean", classe="Archer", x=0, y=0,pv=100, pa=10))
        self.mon_jeu.ajouter_personnage(self.mon_jeu.creer_personnage(nom="Yemiha", classe="Mage", x=0, y=0,pv=100, ps=10))
        self.mon_jeu.ajouter_personnage(self.mon_jeu.creer_personnage(nom="Rita", classe="GuerrierFou", x=0, y=0,pv=100, pa=10))
        self.mon_jeu.ajouter_personnage(self.mon_jeu.creer_personnage(nom="Sabri", classe="Fée", x=0, y=0,pv=100, pa=10,ps=10))
        #Liste 2 
        self.mon_jeu.ajouter_personnage(self.mon_jeu.creer_personnage(nom="Adam", classe="Guerrier", x=0, y=0, pv=100, pa=100))
        self.mon_jeu.ajouter_personnage(self.mon_jeu.creer_personnage(nom="Suli", classe="Soigneur", x=0, y=0,pv=100,ps=10))
        self.mon_jeu.ajouter_personnage(self.mon_jeu.creer_personnage(nom="Julie", classe="Mage", x=0, y=0,pv=100,ps=10))
        self.mon_jeu.ajouter_personnage(self.mon_jeu.creer_personnage(nom="Souka", classe="Mage", x=0, y=0,pv=100,ps=10))
        self.mon_jeu.ajouter_personnage(self.mon_jeu.creer_personnage(nom="Thomas", classe="Archer", x=0, y=0,pv=100, pa=10))
        self.mon_jeu.ajouter_personnage(self.mon_jeu.creer_personnage(nom="Souleyman", classe="Fée", x=0, y=0,pv=100, pa=10,ps=10))
        self.mon_jeu.ajouter_personnage(self.mon_jeu.creer_personnage(nom="Jean", classe="Archer", x=0, y=0,pv=100, pa=10))
        self.mon_jeu.ajouter_personnage(self.mon_jeu.creer_personnage(nom="Yemiha", classe="Mage", x=0, y=0,pv=100, ps=10))
        self.mon_jeu.ajouter_personnage(self.mon_jeu.creer_personnage(nom="Rita", classe="GuerrierFou", x=0, y=0,pv=100, pa=10))
        self.mon_jeu.ajouter_personnage(self.mon_jeu.creer_personnage(nom="Sabri", classe="Fée", x=0, y=0,pv=100, pa=10,ps=10))

        self.create_widgets()
        self.mainloop()   

    def create_widgets(self):

        self.geometry("800x600")
        self.config(bg="white") # Ajoute une couleur de fond à la fenêtre principale
        self.label = tk.Label(self, text=" Mon Jeu vidéo", bg="white", fg="red", font=("Arial", 27)) # Change la couleur de texte en rouge
        self.label.pack(side="top",anchor = "n", padx=10, pady=10) 
        
        #Liste des personnages
        self.liste = tk.Label(self, text="Liste des Personnages")
        self.liste.place(x=0,y=50)

        #Liste 1
        self.affiche = tk.Listbox(self)     #affiche est la liste des personnages
        self.affiche.bind('<<ListboxSelect>>', lambda event: self.regrouper_méthodes(event))
        self.affiche.insert(1, "Damien","Amalia","Julia","Soukaina","Thomas","Souleyman","Jean","Yemiha","Rita","Sabri")
        self.affiche.place(x=0,y=70)
        #Liste 2 
        self.liste2 = tk.Label(self, text="Liste des Cibles")
        self.affiche2 = tk.Listbox(self)
        self.affiche2.bind('<<ListboxSelect>>',lambda event: self.regrouper_méthodes(event))
        self.affiche2.insert(1, "Damien","Amalia","Julia","Soukaina","Thomas","Souleyman","Jean","Yemiha","Rita","Amalia","Sabri")
        self.liste2.pack(side="right",anchor="ne")
        self.affiche2.place(x=700,y=90)

        #Liste des Options de déplacements
        ListeOptions=["Haut","Bas","Gauche","Droite"]
        self.listeCombo = ttk.Combobox(self, values=ListeOptions)
        self.listeCombo.pack(side ="left",anchor = "w")
        self.listeCombo.current(0)   
        self.listeCombo.bind("<<ComboboxSelected>>", self.select)
        
        #bouton quitter
        self.bouton_quitter = tk.Button(self, text='Quitter', command=self.destroy)
        self.bouton_quitter.pack(side="bottom",expand=True,anchor="center")

        #Action
        self.action = tk.Label(self, text="Sélectionner l'action à effectuer puis cliquer sur le bouton 'Envoyer' " )
        self.action.pack(side="top",anchor="center")
        self.cible = 0
        self.perso = 0
        self.atk = 1

        self.bouton_combat = tk.Button(self, text='Combat',command=self.va_attaquer)
        self.bouton_Soigne = tk.Button(self, text='Soigne', command=self.va_soigner)
        self.bouton_Deplace = tk.Button(self, text='Direction',command = self.deplacement)
        self.direction = "Haut"
        self.bouton_combat.pack(side="top",expand=True,anchor="center")
        self.bouton_Soigne.pack(side="top",expand=True,anchor="center")
        #self.descriptionperso = tk.Label(self, text="Description du personnage")
        #self.descriptionperso.pack(side="left",anchor="sw")
        self.bouton_Deplace.place(x=0,y=250)
        self.bouton_Deplace.bind('<<ListboxSelect>>',lambda event: self.deplacement())
        self.bouton_action = tk.Button(self, text='Envoyer', command=self.attaque_ou_soigne)
        self.bouton_action.pack(side="top",expand=True,anchor="center")

    #Méthodes

    def deplacement(self):

        if self.direction == "Haut":
            self.mon_jeu.deplacer_personnage(self.perso,0,-1)
        if self.direction == "Bas":
            self.mon_jeu.deplacer_personnage(self.perso,0,1)
        if self.direction == "Gauche":
            self.mon_jeu.deplacer_personnage(self.perso,-1,0)
        if self.direction == "Droite":
            self.mon_jeu.deplacer_personnage(self.perso,1,0)
        
    def regrouper_méthodes(self,event):
        if self.affiche.curselection() != () :
            self.afficher_infos_personnage(event)
            try :
                self.perso = self.recuperer_index_personnage()
            except:
                pass
        elif self.affiche2.curselection() != () :
            self.afficher_infos_personnage(event)
            try :
                self.cible = self.recuperer_index_cible() 
            except:
                pass
        else :
            pass

    def attaque_ou_soigne(self):
        if self.atk == 1:
            self.attaquer()
        if self.atk == 0:
            self.soigner()

    def va_attaquer(self):
        self.atk = 1
    def va_soigner(self):
        self.atk = 0
    
    def meurt(self):
        if self.mon_jeu.personnages[self.recuperer_index_personnage()].pv <= 0:
            self.affiche.delete(self.recuperer_index_personnage())
            self.affiche2.delete(self.recuperer_index_personnage())
            self.mon_jeu.personnages.pop(self.recuperer_index_personnage())
            self.label_message.destroy()

    def afficher_infos_personnage(self, event):
        # Récupérer l'indice de l'élément sélectionné
        if self.affiche.curselection() != () :
            index = self.affiche.curselection()[0]
            # Récupérer le personnage correspondant
            personnage = self.mon_jeu.personnages[index]
            # Afficher les informations du personnage
            message = personnage.allInfo()
            if hasattr(self, 'label_message'):
                self.label_message.destroy()  # Supprimer l'ancien message
            self.label_message = tk.Label(self, text=message)
            self.label_message.place(x=0,y=450) 
        else :
            index = self.affiche2.curselection()[0]
            # Récupérer le personnage correspondant
            personnage = self.mon_jeu.personnages[index]
            # Afficher les informations du personnage
            message = personnage.allInfo()
            if hasattr(self, 'label_message'):
                self.label_message.destroy()  # Supprimer l'ancien message
            self.label_message = tk.Label(self, text=message)
            self.label_message.place(x=0,y=450)

    def recuperer_index_personnage(self):
        self.perso = self.affiche.curselection()[0]
        return self.perso
    def recuperer_index_cible(self):
        self.cible = self.affiche2.curselection()[0]
        return self.cible
    
    def attaquer(self):
        if isinstance(self.mon_jeu.personnages[self.perso], (Guerrier,GuerrierFou,Fée,Archer) ) == True:
            try:
                self.mon_jeu.personnages[self.perso].attaquer(self.mon_jeu.personnages[self.cible])
            except IndexError:
                print("Vous n'avez pas sélectionné de personnage")
            except ValueError:
                print("Vous n'avez pas sélectionné de personnage")



    def soigner(self):
        if isinstance(self.mon_jeu.personnages[self.perso], (Soigneur, Mage,Infirmière, Paladin,Fée)) == True:
            try :
                self.mon_jeu.personnages[self.perso].soigner(self.mon_jeu.personnages[self.cible])
            except IndexError:
                print("Vous n'avez pas sélectionné de personnage")
            except ValueError:
                print("Vous n'avez pas sélectionné de personnage")
            except TypeError:
                print("Ce personnage ne peut pas soigner")
             

    def select(self, event):
        self.direction = self.listeCombo.get()
        return self.direction


if __name__ == '__main__':
    app = Application()
