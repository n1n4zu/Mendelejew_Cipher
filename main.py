# Dictionary of atoms and their atomic number
atoms: dict[str, int] = {
    'H': 1,
    'He': 2,
    'Li': 3,
    'Be': 4,
    'B': 5,
    'C': 6,
    'N': 7,
    'O': 8,
    'F': 9,
    'Ne': 10,
    'Na': 11,
    'Mg': 12,
    'Al': 13,
    'Si': 14,
    'P': 15,
    'S': 16,
    'Cl': 17,
    'Ar': 18,
    'K': 19,
    'Ca': 20,
    'Sc': 21,
    'Ti': 22,
    'V': 23,
    'Cr': 24,
    'Mn': 25,
    'Fe': 26,
    'Co': 27,
    'Ni': 28,
    'Cu': 29,
    'Zn': 30,
    'Ga': 31,
    'Ge': 32,
    'As': 33,
    'Se': 34,
    'Br': 35,
    'Kr': 36,
    'Rb': 37,
    'Sr': 38,
    'Y': 39,
    'Zr': 40,
    'Nb': 41,
    'Mo': 42,
    'Tc': 43,
    'Ru': 44,
    'Rh': 45,
    'Pd': 46,
    'Ag': 47,
    'Cd': 48,
    'In': 49,
    'Sn': 50,
    'Sb': 51,
    'Te': 52,
    'I': 53,
    'Xe': 54,
    'Cs': 55,
    'Ba': 56,
    'La': 57,
    'Ce': 58,
    'Pr': 59,
    'Nd': 60,
    'Pm': 61,
    'Sm': 62,
    'Eu': 63,
    'Gd': 64,
    'Tb': 65,
    'Dy': 66,
    'Ho': 67,
    'Er': 68,
    'Tm': 69,
    'Yb': 70,
    'Lu': 71,
    'Hf': 72,
    'Ta': 73,
    'W': 74,
    'Re': 75,
    'Os': 76,
    'Ir': 77,
    'Pt': 78,
    'Au': 79,
    'Hg': 80,
    'Tl': 81,
    'Pb': 82,
    'Bi': 83,
    'Po': 84,
    'At': 85,
    'Rn': 86,
    'Fr': 87,
    'Ra': 88,
    'Ac': 89,
    'Th': 90,
    'Pa': 91,
    'U': 92,
    'Np': 93,
    'Pu': 94,
    'Am': 95,
    'Cm': 96,
    'Bk': 97,
    'Cf': 98,
    'Es': 99,
    'Fm': 100,
    'Md': 101,
    'No': 102,
    'Lr': 103,
    'Rf': 104,
    'Db': 105,
    'Sg': 106,
    'Bh': 107,
    'Hs': 108,
    'Mt': 109,
    'Ds': 110,
    'Rg': 111,
    'Cn': 112,
    'Nh': 113,
    'Fl': 114,
    'Mc': 115,
    'Lv': 116,
    'Ts': 117,
    'Og': 118
}

def cipher_word(word: str) -> str | None:
    """
    Reoccurrence function that encrypts one word into one or two letter atom symbol
    :param word: given word to encrypt
    :return: encrypted word or None if it's impossible to encrypt
    """

    word: str = word.lower()
    n: int = len(word)
    result: list[list[str]] = []

    def recurrency(i: int, code: list[str]) -> None:
        """
        Subfunction that helps to encrypt words
        :param i: position of the letter in the word
        :param code: current list of atomic number
        """
        if i == n:
            result.append(code)
            return

        if i + 1 < n:
            symbol2: str = (word[i] + word[i + 1]).capitalize()
            if symbol2 in atoms:
                recurrency(i + 2, code + [atoms[symbol2]])

        symbol1: str = word[i].capitalize()
        if symbol1 in atoms:
            recurrency(i + 1, code + [atoms[symbol1]])

    recurrency(0, [])
    return  result[0] if result else None

def mendelejew_cipher(message: str) -> str:
    """
    Function that encrypts message by using Mendelejew's cipher
    :param message: given message to encrypt
    :return: encrypted message represented by atomic number
    """
    words: list[str] = message.split()
    encrypted: list[str] = []

    for word in words:
        code: str = cipher_word(word)
        if not code:
            return f'This word cannot be encrypted: {word}'

        encrypted.append('*'.join(map(str, code)))

    return '**'.join(encrypted)


# Tests
print(mendelejew_cipher('SobOta rANo'))
print(mendelejew_cipher('nos'))
print(mendelejew_cipher('algorytmion'))
