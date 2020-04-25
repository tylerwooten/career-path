import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
#
df = pd.read_csv('titles_small.csv', dtype='unicode')

csv_out = []
v = 1
for row in df.itertuples():
    data = [x for x in row if isinstance(x, str)][1:]
    for n, k in enumerate(data[:-1]):
        temp = {}
        print('processing line: ', v, '\n')
        temp['source'] = data[n]
        temp['target'] = data[n + 1]
        if temp['source'] != temp['target']:
            csv_out.append(temp)
    v += 1

final_pairs = []
len_csv_out = len(csv_out)
for pair in csv_out:
    count = csv_out.count(pair)
    csv_out = [x for x in csv_out if x != pair]  # recreate the list without the pair
    pair['weight'] = count
    if pair['weight'] != 0:
        if pair['source'] != pair['target']:
            final_pairs.append(pair)
            print('current length of final_pairs: ', len(final_pairs), '/', len_csv_out)

formatted = pd.DataFrame(final_pairs)
formatted.to_csv('titles_small_formatted.csv')

# print(df)
# Graphtype = nx.Graph()
# G = nx.from_pandas_edgelist(df)
#
# nx.draw(G)
# plt.show() # display