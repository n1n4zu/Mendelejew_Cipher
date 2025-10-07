# Mendelejew Cipher

Python implementation of a word and message encryption system based on **Mendelejew's periodic table**.  
Each letter or pair of letters in a word is replaced with an **atomic number** corresponding to an element symbol.

## Features

- **Atomic symbol dictionary** – includes all 118 chemical elements
- **Word encryption** – converts a single word into a list of atomic numbers
- **Message encryption** – converts whole sentences, separating words and atoms with special symbols
- **Recursive algorithm** – finds possible symbol combinations for each word

## Installation

```bash
git clone https://github.com/n1n4zu/Mendelejew_Cipher.git
cd Mendelejew_Cipher
```

## Usage

### Windows
```bash
python main.py
```

### Linux
```bash
python3 main.py
```

### Example Output
```python
print(mendelejew_cipher('SobOta rANo'))
# 16*8*5**86*7*8

print(mendelejew_cipher('nos'))
# 7*8*16

print(mendelejew_cipher('algorytmion'))
# This word cannot be encrypted: algorytmion
```

## Function Documentation

`cipher_word(word: str) -> str | None`

### Description
Encrypts a single word into a sequence of **atomic numbers** based on valid element symbols.

## Parameters 
- `word (str)`: word to encrypt

### Returs
- `list[str]`: list of atomic numbers representing the word
- `None`: if encryption is impossible

### Details
Uses a recursive approach to check both one-letter and two-letter element symbols.
For example, the word `"NoS"` is matched as `["N", "O", "S"] → [7, 8, 16]`.

`mendelejew_cipher(message: str) -> str`

### Description
Encrypts a full message by converting each word into atomic number sequences.
Words are separated by `**`, and atomic numbers within a word by `*`.

### Parameters
- `message (str)`: input text containing words to encrypt

### Returs
- `str`: encrypted message as atomic number sequence
- Error message if any word cannot be encoded

## License
MIT License – See [LICENSE](LICENSE) for details