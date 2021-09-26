import camelot as cm
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Open the pdf with Camelot
input_pdf = cm.read_pdf('india_factsheet_economic_n_hdi.pdf', pages='1,2')

for n in input_pdf:
    print(n)

# Get the 3rd table and put it into a dataframe & show it right away
print(input_pdf[2].df)
df = input_pdf[2].df.loc[11:13,1:3] # Get these specific cells
print(df)

df = df.reset_index(drop = True) # Reset the index from 11:13 to 0:2
df.columns = ["KPI", "2001", "2011"] # Rename the columns
print(df)

# Change the integer values to floats
df.loc[:,["2001","2011"]] = df.loc[:,["2001","2011"]].astype(float)
print(df)

df.to_csv("table_from_pdf.csv")
df.to_excel("table_from_pdf.xlsx")

# Visualize the data
df2 = pd.read_csv("table_from_pdf.csv")
print(df2)

df_melted = df.melt('KPI', var_name='year', value_name='percentage')
print(df_melted)
sns.barplot(x='KPI', y = 'percentage', hue = 'year', data = df_melted)
plt.show()
