import re
from pyfr.verbes import Verbe
import pyfr.verbes.auxilliaire as aux

pattern = r"^(\w+?)(aître|enir|cevoir|ger|cer|oire|ire|oir|er|ir|re)$"
# TODO: Ajoute tous les terminaisons des verbes


class Infinitif(Verbe):
	def __init__(self, verbe: str):
		"""Initialise l'instance de la classe Infinitif.

		Parameters:
		verbe (str): L'infinitif du verbe ou le verbe sous forme de string
		"""
		super(Infinitif, self).__init__()
		if verbe is None:
			raise ValueError("Le verbe ne peut pas être \"None\".")
		if issubclass(type(verbe), Verbe):
			verbe = verbe.infinitif
		self.infinitif = verbe.strip().lower()
		if not self.infinitif:
			raise ValueError("Le verbe ne peut pas être vide.")
		if not (m := re.match(pattern, self.infinitif.removeprefix("se ").removeprefix("s'"))):
			raise ValueError(f"Le verbe \"{self.infinitif}\" n'est pas valide.")
		self.racine, self.terminaison = m[1], m[2]
		self.aux = aux.get_aux(self.infinitif)
		self.groupe = 1 if self.terminaison == "er" else 2 if self.terminaison == "ir" else 3
