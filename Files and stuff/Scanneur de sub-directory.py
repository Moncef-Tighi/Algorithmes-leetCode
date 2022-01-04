""" Fonction récursive qui print les noms de tout les fichier dans un dossier
	Tout en visitant les subdirectory et listant leurs fichiers séparemment"""

def scanning(path):
	print("--- Directory : ", path, " ---")
	with os.scandir(path) as link:
		for entrie in link:
			if entrie.is_dir():
				scanning(entrie.path)
			elif entrie.is_file():
				print(entrie.name)

				
scanning('..\..\..\..\..\Desktop\Programmation\Exercices Algorithmes')


"""Idée pour améliorer l'Algorithme :
	Actuellement, L'algorithme n'ordonne pas les fichiers. Quand il rencontre un dossier il l'ouvre puis liste
	les fichiers à l'intérieur avant de revenir puis lister les fichiers et dossiers restants.
	Utiliser un stack pour d'abord lire tout les fichiers avant de lire tout les dossiers?

	Voici la version amélioré :"""



def scanning_Inorder(path):
	stack=[]
	print("--- Directory : ", path, " ---")
	with os.scandir(path) as link:
		for entrie in link:
			if entrie.is_dir():
				stack.append(entrie.path)
			elif entrie.is_file():
				print(entrie.name)
	for dossier in stack:
		scanning_Inorder(dossier)

scanning_Inorder("..\..")

"""Idée pour améliorer ENCORE :
	Créer une distinction pour chaque niveau de sub-directory traversé.
	Exemple :

--> Dossier principal
	--->File
	--->File
	--->File

	----> Subdirectory
		----->File
		----->File

	----> Subdirectory
		----->File
		------>Sub-Subdirectory
			--------->Sub-Sub-Subdirectory
	---->Subdirectory
	


	Je pourrais aussi ajouter un compteur de Fichier + Directory qui s'afficherait à la fin
	Et / Ou un total du nombre du fichier contenu dans le dossier au moment le dossier est nommé.
"""