# Ce programme à pour objectif de calucler la note qui faut avoir 
# Dans un examen pour valider l'ecue connaissant les notes de devoirs

#////////////////////////////////////////////////////////////////

# la premeier commande est de recupere le nombre de notes que l'étudiant 
# veut faire entrer 

# le message à afficher avant de lancer le code
print("Dans ce exercice il s'agit d'entrer vos differentes de devoirs et connaitre la note min à avoir pour valider l'examen")

# Demander à l'utilisateur de entrer le nombre de notes qu'il veut entrer

note_entrant = input("Veuillez entrer le nombre de notes :")
nte_e = int(note_entrant)

# convertir la valeur de input en float
nbre_note = int(note_entrant)
tour = 0   # initialisation du nombre de tour
note_save = 0 # initialisation de la somme
# Faire une boucle avec les données entrée


while tour < nbre_note :
    note_bcle = input("Veuillez entrer une note : ")
    nbcle_cv = float(note_bcle) # convertion de la valeur entrer dans input en int
    note_save = note_save + nbcle_cv # somme des notes entrer pas l'utilisateur
    tour += 1 # incrementation de la boucle
if tour == nbre_note :
 moyenne_devoirs = round(note_save/nte_e,2)
 print("Votre moyenne de devoir est :",moyenne_devoirs)
 print("La moyenne de devoirs compte pour 40%","et celle de l'examen compte pour 60%")
 part_devoirs = moyenne_devoirs*0.4
 part_exam = 10 - part_devoirs
 
 note_exam = part_exam/0.6

print("la note neccesaire à l'examen est :", round(note_exam,2))

