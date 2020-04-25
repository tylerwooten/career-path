import networkx as nx
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import matplotlib.pyplot as plt
#
df = pd.read_csv('titles_formatted.csv', dtype='unicode')

#print(df)
#Graphtype = nx.Graph()
#G = nx.from_pandas_edgelist(df)

#nx.draw(G)
#plt.show() # display

#current = input('Current Job?: ')
future = input('Future Job?: ')
#temp = {'target': current, 'source': future}

list_of_previous = df.loc[df['source'] == future]
list_of_previous['weight'] = list_of_previous['weight'].astype(int)
list_of_previous['percentage'] = round((list_of_previous['weight'] / list_of_previous['weight'].sum()) * 100, 3)
list_of_previous.sort_values('percentage', axis = 0, ascending = True, inplace = True, na_position ='last')

print('TOP PREVIOUS JOBS: ')
print('percentage: ' + 'job:')
for k, row in list_of_previous.iterrows():
    print(str(row['percentage']) + '%  ' + row['target'])

# Need to add recursion here.
# starting at the end "CEO" -> take the previous job's highest percentage previous and check that one.
# repeat until at my current job

# on last step, if the highest probability is my "goal" then return that path.
# if I pass my node or if I don't reach it after 20+ steps, start over

# traverse up the graph based and each step check my highest avg to see if my goal is in there. recurse