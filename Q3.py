import hashlib
def crypter_signature(message: list[str]):
    # Référence : Notes de cours et exersice cryptographie
    # https://github.com/vivgxojo/cryptographie/blob/master/app_cryptographie/crypto.py
    """
    cette fonction va prendre la signature de l'utilisateur et va la haché
    :param signature: la signature de l'utilisateur
    :param message: liste qui garde la signature
    :return: la signature haché
    """
    hash_dict = {}
    for mot in message:
        mot_en_bite = mot.encode()
        hash_md5 = hashlib.md5(mot_en_bite).hexdigest()
        hash_sha256 = hashlib.sha256(mot_en_bite).hexdigest()
        hash_sha512 = hashlib.sha512(mot_en_bite).hexdigest()

        hash_dict[mot] = [hash_md5, hash_sha256, hash_sha512]
    return hash_dict
    # Je ne sais pas si la façon dont j'ai fait le code pour la question trois mais comment je l'ai comprisje devais demander la signature,
    # hacher cette signature, puis la comparé avec la signature déjà fournie dans le code.


def comparer(hash_dict, signatures):
    """
    Cette fontion va comparé la signature qui vient d'être haché avec celle qui avait été fournie.
    :param hash_dict: La signature qui a été haché préalablement.
    :param signatures: les signatures haché que on été fournie avec le code.
    :return: si les signatures sont les même.
    """
    if signatures == hash_dict:
        print("Message avec signatures validéées : ")
        print("Code 9 activé demain")
        print("La réponse est 142")
    else:
        print("Message altérés, signatures non valides : ")
        print("Le monstre est au niveau 7 ")
    return

if __name__ == "__main__":

    messages_gr5 = {
        "pseudo" : "IronCode",
        "messages" : ["Le monstre est au niveau 7", "Code 9 activé demain", "La réponse est 142"],
        "signatures" : ["fresea", "odivai", "nses14"]
    }
    signature = input("Entrer les deux avant-dernières de votre mot.(ou pour bonjour)  : ")

    message = []
    signature = message.append(signature)
    comparer(message, signature)
