import pandas as pd  # convention to import and use pandas like this
import matplotlib

df = pd.read_csv("dataset/avocado.csv")# df stands for dataframe. Also a common convention to call this df
df['Date'] = pd.to_datetime(df['Date'])
albany_df = df.copy()[df['region'] == 'Albany']
albany_df.set_index("Date", inplace=True)
albany_df.sort_index(inplace=True)
albany_df['price25ma'] = albany_df["AveragePrice"].rolling(25).mean()
df['region'].unique()

graph_df = pd.DataFrame()

for region in df['region'].unique()[:16]:
    region_df = df.copy()[df['region'] == region]
    region_df.set_index("Date", inplace=True)
    region_df.sort_index(inplace=True)
    region_df[f'{region}_price25ma'] = region_df["AveragePrice"].rolling(25).mean()
    
    if graph_df.empty:
        graph_df = region_df[[f'{region}_price25ma']]
    else:
        graph_df = graph_df.join(region_df[f'{region}_price25ma'])
        
# print(graph_df.head())
print(graph_df.plot(figsize=(8,5), legend=False))
    

