# Load Pandas
from pandas import read_csv

#Load Dataset
file = 'vgsales.csv'
names = ['Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
dataset = read_csv(file, names=names)

#print(dataset.shape)
#print(dataset.describe)
#print(dataset.head(10)) #Primeiras popsições
#print(dataset.tail())   #Poisções finais

qtde_wii = dataset[(dataset['Platform'] == 'Wii')] 
#print(len(qtde_wii))

qtde_x360 = dataset[(dataset['Platform'] == 'X360')] 
#print(len(qtde_x360))

qtde_ps4 = dataset[(dataset['Platform'] == 'PS4')] 
#print(len(qtde_ps4))

#qtde_ps4.to_csv('ps4.csv') #Exportar um csv
#qtde_x360.to_csv('x360.csv')
#qtde_wii.to_csv('wii.csv')

ps4_ubisoft = dataset.query('Platform == "PS4" & Publisher == "Ubsoft"')
#print(ps4_ubisoft.shape)
#print(ps4_ubisoft.head)

dataset2 = dataset.loc[1:3,['Name', 'Platform']]
print(dataset2.head())