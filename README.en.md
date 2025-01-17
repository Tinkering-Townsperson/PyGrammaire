# PyGrammaire

![Python logo with a beret and a mustache](https://github.com/Tinkering-Townsperson/PyGrammaire/blob/3073bd5e81550004db2da54af010b30b953e110f/assets/icons/PyGrammaire.png)

 Let's do some Grammar! The rules and exceptions of the french language, in the form of code!

*Lire [l'original (en français)](README.md)*

## L'Usage

```py
import pygrammaire.sujet as sujet
import pygrammaire.verbes.indicatif as indicatif

aller = indicatif.Présent("aller")

print("Je" + aller.conj(sujet.JE))
```
