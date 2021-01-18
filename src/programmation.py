# Parcourez le fichier pour trouver la liste de tous les utilisateurs qui se sont connectés,
# enregistrez cette liste dans un fichier utilisateurs.txt.
def liste_utilisateurs_connectes():
    file= open('input/connection.log','r')
    Lines=file.readlines()
    file.close()
    liste_utilisateurs=[]
    utilisateurs = open("output/utilisateurs.txt", "w")
    for line in Lines:
            utilisateur=line.split(";")[1]
            if utilisateur not in liste_utilisateurs:
                liste_utilisateurs.append(utilisateur)
                utilisateurs.write(utilisateur+'\n')
    print('\n Q1? La liste de tous les utilisateurs qui se sont connectés:')
    print(liste_utilisateurs)
        


# On soupçonne qu’une personne se connecte en dehors des heures d’ouverture des bureaux (8h-19h),
# peut-être depuis un poste distant.
# Utilisez un script pour retrouver l’identifiant de cette personne ainsi que l’ip à la laquelle elle se connectait
def personne_hors_heures():
    file= open('input/connection.log','r')
    Lines=file.readlines()
    file.close()
    d = {}
    soupconne = open("output/soupconne.txt", "w")
    for line in Lines:
            time=line.split(" ")[1]
            soupconneIP=line.split(";")[0]
            soupconneNom=line.split(";")[1]
            soupconneDateHeure=line.split(";")[2]
            if time<"08:00" or time>"19:01":
                if soupconneIP not in d:
                    d[soupconneIP]=soupconneNom
                soupconne.write('L’identifiant de personne soupçonne est {} et l’ip à la laquelle elle se connectait est {} le {}'.format(soupconneNom,soupconneIP,soupconneDateHeure)+'\n')
    print('\n Q2? Personne qui se connecte en dehors des heures d’ouverture des bureaux est:')
    print(d)

# Le service de sécurité informatique a fournit un fichier contenant les ips dangereuses : warning.txt.
#  Lisez ce fichier pour construire une liste contenant toutes les ip dangereuses.
#   A l’aide de cette liste, relevez dans le fichier connexion.log tous les utilisateurs 
#   qui se sont connectés sur une de ces ip, on produira un fichier suspects.txt avec une ligne
#    par utilisateur et le nombre de fois qu’il s’est connecté à une ip interdite :
def utilisateurs_suspects():
    warning= open('input/warning.txt','r')
    warnings=warning.readlines()
    warning.close()
    liste_soupconne=[]
    d = {}
    suspects = open("output/suspects.txt", "w")
    for line in warnings:
        liste_soupconne.append(line)
    dangereuses = [x.replace('\n', '') for x in liste_soupconne]
    print("\n Q3? La liste contenant toutes les ip dangereuses:")
    print(dangereuses)

    file= open('input/connection.log','r')
    lines=file.readlines()
    liste_suspects=[]
    for line in lines:
        part=line.split(";") 
        ip=part[0]
        for ip_s in dangereuses:
            if ip==ip_s:
                liste_suspects.append(part[1])
    for sus in set(liste_suspects):
        times=liste_suspects.count(sus)
        suspects.write("\nUtilisateur {} etait connecté à une ip interdite {} fois".format(sus,times))
        print("Utilisateur {} etait connecté à une ip interdite {} fois".format(sus,times))
    suspects.close()


liste_utilisateurs_connectes()
personne_hors_heures()
utilisateurs_suspects()