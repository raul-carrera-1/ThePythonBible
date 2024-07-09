import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'Country': ['USA', 'Candada', 'USA']
}

df = pd.DataFrame(data)
print(df)

print("--------------------")
df = pd.read_csv('Chapter 3/textfile.txt')
print(df.head(2))