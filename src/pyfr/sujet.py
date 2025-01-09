from pyfr.accord import Genre, Nombre
from typing import Union
from types import NoneType


class Sujet:
	def __init__(
			self,
			nom: str,
			personne: str = 1,
			pluriel_ou_poli: Union[bool, NoneType] = False,
			genre: Union[bool, NoneType] = None
		) -> None:
		"""Initialise l'instance de la classe Sujet.

		Parameters:
		nom (str): Le nom du sujet.
		personne (str, optional): La personne du sujet.
		pluriel_ou_poli (Union[bool, NoneType], optional): Si le sujet est pluriel ou poli. Defaults to False.
		genre (Union[bool, NoneType], optional): Le genre du sujet. Defaults to None.
		"""
		self.nom = nom
		self.personne = personne
		self.pluriel_ou_poli = pluriel_ou_poli
		self.genre = genre

	def __repr__(self) -> str:
		personne = self.personne
		pluriel = "pluriel" if self.pluriel_ou_poli else "singulier"
		genre = "masculin" if self.genre is Genre.Masculin else "feminin" if self.genre is Genre.Feminin else ""
		return f"{self.nom.title()}: {personne}e personne {pluriel}, {genre}"


JE = Sujet("Je", personne=1, pluriel_ou_poli=Nombre.Singulier, genre=Genre.Neutre)
TU = Sujet("Tu", personne=2, pluriel_ou_poli=Nombre.Singulier, genre=Genre.Neutre)
IL = Sujet("Il", personne=3, pluriel_ou_poli=Nombre.Singulier, genre=Genre.Masculin)
ELLE = Sujet("Elle", personne=3, pluriel_ou_poli=Nombre.Singulier, genre=Genre.Feminin)
ON = Sujet("On", personne=3, pluriel_ou_poli=Nombre.Singulier, genre=Genre.Neutre)
NOUS = Sujet("Nous", personne=1, pluriel_ou_poli=Nombre.Pluriel, genre=Genre.Neutre)
VOUS = Sujet("Vous", personne=2, pluriel_ou_poli=Nombre.Pluriel, genre=Genre.Neutre)
ILS = Sujet("Ils", personne=3, pluriel_ou_poli=Nombre.Pluriel, genre=Genre.Masculin)
ELLES = Sujet("Elles", personne=3, pluriel_ou_poli=Nombre.Pluriel, genre=Genre.Feminin)
