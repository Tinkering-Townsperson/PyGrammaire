class Verbe:
	infinitif: str
	racine: str
	terminaison: str
	groupe: str
	aux: str

	def __repr__(self) -> str:
		return (
			f"{self.infinitif}:\n"
			f"\tracine      = {self.racine}\n"
			f"\tterminaison = {self.terminaison}\n"
			f"\tgroupe      = {self.groupe}\n"
			f"\tauxiliaire  = {self.aux}"
		)

	def conj(self) -> str:
		return self.infinitif
