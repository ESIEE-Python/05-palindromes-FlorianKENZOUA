#### Fonction secondaire
"""
reconnaitre des palindromes
"""

def ispalindrome(p):
    """
    Prend en argument une chaine de caractère p et renvoie si c'est un palindrome ou non

    Args :
        p : chaine de caractère

    Return :
        Booleen : True or False
    """
    # votre code ici
    s = 0
    taille = len(p)
    table_de_traduction = str.maketrans("PVNSTMCçKLEÉÈÊËéèêëAÁÀÂÄàáâäOÔÖôöÛÜÙûüùIÎÏîï-,:?!'",
    "pvnstmcckleeeeeeeeeaaaaaaaaaooooouuuuuuiiiii      ") # Création d'une table de traduction
    chaine_traduite = p.translate(table_de_traduction)
    while s != taille :
        if chaine_traduite[s] == ' ' :
            chaine_traduite = chaine_traduite[:s] + chaine_traduite[s+1:]
            taille -= 1
        else :
            s += 1
    chaine = chaine_traduite[::-1]
    if chaine_traduite == chaine :
        return True

    return False

#### Fonction principale


def main():
    """
    realise les tests sur la fonction secondaire
    """

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
