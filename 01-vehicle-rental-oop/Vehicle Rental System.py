class VehiculeBase:
	def __str__(self):
		raise NotImplementedError("Cette methode n;est pas implementé")

	def get_frais(self):
		raise NotImplementedError("Cette methode n'est pas implemente")

class Vehicule:
	nb_vehicule = 0
	taxe = 0.15

	def __init__(self , marque , prix_jour , capacite , annee):
		self.marque = marque
		self.annee = annee
		self.prix_jour = prix_jour
		self.capacite = capacite

		Vehicule.nb_vehicule += 1

	@classmethod
	def total_vehicule(cls):
		return cls.nb_vehicule

	@classmethod
	def modifier_taxe(cls , nouvelle_taxe):
		if ( nouvelle_taxe > 0 and nouvelle_taxe < 1):
			cls.taxe = nouvelle_taxe
		else:
			raise ValueError("La taxe doit etre copmprise entre 0 et 1")


	def get_frais(self , annee_actuelle = 2026):
		return ( 2 * ( annee_actuelle - self.annee ) )

	def get_prix_ttc(self):
		return (self.prix_jour + self.get_frais()) * ( 1 + self.taxe)

	def __str__(self):
		return f"{self.marque} ( Capacite = {self.capacite} , prix = {self.prix_jour}$ / jour ,annee = {self.annee})"

	def __add__(self, other):
		marque = self.marque + "+" + other.marque
		prix_jour = ( self.prix_jour + other.prix_jour ) * 0.9
		capacite = self.capacite + other.capacite
		annee = min (self.annee , other.annee)

		return Vehicule(marque , prix_jour , capacite , annee)

	def __eq__(self, other):
		return (self.get_prix_ttc() == other.get_prix_ttc())

	def __lt__(self, other):
		return (self.get_prix_ttc() < other.get_prix_ttc())

class Moto(Vehicule):
	def __init__(self , marque , prix_jour , capacite , annee , casque_inclus):
		super().__init__(marque , prix_jour , capacite , annee)
		self.casque_inclus = casque_inclus

	def __str__(self):
		if self.casque_inclus :
			return f"{self.marque} ( Capacite = {self.capacite} , prix = {self.prix_jour}$ / jour ,annee = {self.annee} , Casque Inclus)"
		else:
			return f"{self.marque} ( Capacite = {self.capacite} , prix = {self.prix_jour}$ / jour ,annee = {self.annee} , Casque Non Inclus)"

	def get_frais(self, annee_actuelle=2026):
		if self.casque_inclus:
			return super().get_frais(annee_actuelle) + 5
		return super().get_frais(annee_actuelle)

class VoitureSport(Vehicule):
	def __init__(self , marque , prix_jour , capacite , annee , vitesse_max):
		super().__init__(marque , prix_jour , capacite , annee)
		self.vitesse_max = vitesse_max

	def __str__(self):
		return super().__str__() + f"{self.vitesse_max} km/h"

	def get_frais(self , annee_actuelle = 2026):
		return super().get_frais(annee_actuelle) + 200

class Van(Vehicule):
	def __str__(self):
		return super().__str__()
	def get_frais(self, annee_actuelle=2026):
		return super().get_frais(annee_actuelle) + 3 * self.capacite

def print_liste(liste):
	for i in range (len(liste)):
		print(f"{i} , {liste[i]}")

def chercher_un_vehicule_par_groupe(liste):
	nombre_personne = int(input("Entrer le nombres de personees : "))
	j = 0
	for i in liste:
		if i.capacite >= nombre_personne:
			j = j + 1
			print(i)
	if j == 0 :
		print("Auncun vehicule n'a une capacite coprrespondate")

def louer_un_pack_de_deux_vehicules(liste):
	indice_1 = int(input("Saisir le premier indice du vehicule que ve voulez: "))
	indice_2 = int(input("Saisir le deuxieme indice du vehicule que ve voulez: "))

	louer = liste[indice_1] + liste[indice_2]
	print(louer)
	print(f"Le prix de premier vehicule = {liste[indice_1].get_prix_ttc()}")
	print(f"Le prix de deuxieme vehicule = {liste[indice_2].get_prix_ttc()}")
	print(f"Le prix de pack est { louer.get_prix_ttc() }")
	print(f"Vous economiser : { ( liste[indice_1].get_prix_ttc() + liste[indice_2].get_prix_ttc() ) - louer.get_prix_ttc() }")

def comparer_deux_vehicules(liste):
	i1 = int(input("Saisir le premier indice du vehicule que ve voulez: "))
	i2 = int(input("Saisir le deuxieme indice du vehicule que ve voulez: "))

	if liste[i1] == liste [i2]:
		print(f"Les deuc vehicules sont egaux")
	else:
		if liste[i1] > liste [i2]:
			print(f"L'Objet {liste[i1]} est plus chere que {liste[i2]}")
		else:
			print(f"L'Objet {liste[i1]} est moin chere que {liste[i2]}")

def modifier_taxe(liste):
	taxe = int(input("Entrer le pourcentagfe de taxe : "))
	Vehicule.modifier_taxe(taxe)

def print_menu():
	print(f"====MENU=====")
	print(f"1.  Afficher les vehicules")
	print(f"2. Chercher un Vehicule par un groupe")
	print(f"3. Louer un pack de deux vehicules")
	print(f"4. Comparer deux vehicules")
	print(f"5. Quittez")

def main():


	agence = [
    Moto("Yamaha MT-07", 50, 2, 2024, True),
    Moto("Kawasaki Z900", 65, 2, 2023, False),
    VoitureSport("Ferrari F8", 350, 2, 2025, 340),
    VoitureSport("Porsche 911", 280, 4, 2024, 310),
    Van("Mercedes Vito", 120, 8, 2022)
	]

	temp = True

	while temp:
		print_menu()

		n = int(input("Entre ce que vous voulez faire : "))

		if n == 1:
			print_liste(agence)

		elif  n == 2:
			chercher_un_vehicule_par_groupe(agence)

		elif n == 3:
			louer_un_pack_de_deux_vehicules(agence)

		elif n == 4:
			comparer_deux_vehicules(agence)

		elif n == 5:
			print("C'est la fin")
			temp = False

		else:
			print(f"Choix non present")
			print_menu()



main()
