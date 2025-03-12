student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}
1
import pandas as pd
#TODO 1. Create a dictionary in this format:
df=pd.read_csv("nato_phonetic_alphabet.csv")
Alphabets = {row.letter:row.code for (index,row) in df.iterrows()}



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def phenotic():
    word = input("enter your word\n").upper()
    try:
        lis = [Alphabets[letter] for letter in word]
    except KeyError:
        print("Sorry only alphabets")
        phenotic()
    else:
        print(lis)

phenotic()


