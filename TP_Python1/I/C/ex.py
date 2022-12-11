#1

class Etudiant(dict):

    def __setitem__(self, key, value):
        super().__setitem__(key, value)

Charly = Etudiant({"maths":14, "anglais":18, "sport":8})
Maxime = Etudiant({"maths":12, "anglais":14, "sport":14})
Alexandre = Etudiant({"maths":5, "anglais":16, "sport":15})
promotion = [Charly, Maxime, Alexandre]

#2

def moyenneEtudiant(Etudiant):
    moyenne = 0
    for matiere,note in Etudiant.items():
        moyenne += note
    moyenne = moyenne/len(Etudiant)
    print("La moyenne de l'étudiant est :", moyenne)

moyenneEtudiant(Charly)

#3

def moyenneDiscipline(tab, matiere):
    moyenne = 0
    for i in tab:
        moyenne += i[matiere]
    moyenne = moyenne / len(i)
    print("La moyenne de la classe en " + matiere + " est :", moyenne)

moyenneDiscipline(promotion,"maths")

#4

def noteMax(tab, matiere):
    note = 0
    for i in tab:
        if note < i[matiere]:
            note = i[matiere]
    print("La note la plus haute en " + matiere + " est :", note)

def noteMin(tab, matiere):
    note = None
    for i in tab:
        if note is None or note > i[matiere]:
            note = i[matiere]
    print("La note la plus basse en " + matiere + " est :", note)

noteMax(promotion,"maths")
noteMin(promotion,"maths")

#5

def moyennePromotion(promo):
    moyenne = 0
    nb = 0
    for Etudiant in promo:
        for matiere,note in Etudiant.items():
            moyenne += note
            nb += 1
    moyenne = moyenne / nb
    print("La moyenne de classe est :", moyenne)

moyennePromotion(promotion)