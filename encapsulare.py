class Casa_encapsulare:
		# decorator = elemente care modifica comportamentul unei functii
		_numar_etaje = None
		numar_camere = None
		numar_bai = None
		__material_constructie = None
		suprafata = None
		an_constructie = None
		adresa = None
		clasa_energetica = None
		pret = None

		def __init__(self, numar_etaje, numar_camere, numar_bai, material_constructie, suprafata, adresa):
				self._numar_etaje = numar_etaje
				self.numar_camere = numar_camere
				if numar_bai > 2:
						print("Nu putem construi mai mult de doua bai")
				else:
						self.numar_bai = numar_bai
				self.__material_constructie = material_constructie
				self.suprafata = suprafata
				self.adresa = adresa

		def calculeaza_aprobare_numar_etaje(self):
				if self.numar_etaje > 5:
						print(
								"Cand unul iti spune ca esti beat mergi mai departe. Daca doi iti spun ca esti beat mergi sa te culci")
				else:
						self.aprobare = True

		def __actualizeaza_an_constructie(self, an_constructie):
				self.an_constructie = an_constructie
				return self.an_constructie

		def vinde_casa(self):
				print(f"Apartament de vanazare in zona lalelelor"
							f"Numar camere: {self.numar_camere}"
							f"Numar etaje: {self._numar_etaje}"
							f"Numar bai: {self.numar_bai}"
							f"An constructie: {self.an_constructie},"
							f"Suprafata: {self.suprafata}"
							f"Material constructie: {self.__material_constructie}")

		@property
		def materiale_constructie(self):
				pass

		@materiale_constructie.getter
		def materiale_constructie(self):
				return self.__material_constructie

		@materiale_constructie.setter
		def materiale_constructie(self, material_constructie):
				self.__material_constructie = material_constructie

		@materiale_constructie.deleter
		def materiale_constructie(self):
				self.__material_constructie = None


garsoniera = Casa_encapsulare_decoratori(0, 1, 1, "beton", 40, "Strada Lalelelor 23")
print(
		f"materiale de constructie returnate prin getter inainte de update: {garsoniera.materiale_constructie}")  # apelare getter
garsoniera.materiale_constructie = "caramida"  # setter
print(
		f"materiale de constructie returnate prin getter dupa update: {garsoniera.materiale_constructie}")  # apelare getter
del garsoniera.materiale_constructie
print(
		f"materiale de constructie returnate prin getter dupa delete: {garsoniera.materiale_constructie}")  # apelare getter
