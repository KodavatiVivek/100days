import pandas as pd
df=pd.read_csv("./data/french_words.csv")
dictionary=df.to_dict(orient="records")
print(dictionary)