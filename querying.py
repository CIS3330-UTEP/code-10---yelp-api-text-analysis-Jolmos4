import pandas as pd

def get_full_name(row):
    # print(row)
    full_name = row['name'].split()
    
    new_data = {'First_Name':full_name[0], 'Last_Name':" ".join(full_name[1:])}

    return new_data


df = pd.read_csv('billionaires_orginial.csv')

df['First_Name'] = df.apply(get_full_name, axis=1)

fruits = ['apple', 'cherry', 'kiwi', 'pear']

for index, row in df.iterrows():
    full_name = row['name'].split()
    # print(full_name[0])
    # # print(full_name[1:])
    # print(' '.join(full_name[1:]))

    df.at[index, 'First_Name'] = full_name[0]
    df.at[index, 'Last_Name'] = ''.join(full_name[1:])

print(df[['name', 'First_Name', 'Last_Name']])

df.to_csv('new_data.csv', index=False)
