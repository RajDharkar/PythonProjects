import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Population': ['A', 'B', 'C'],
    'Red': [18, 5, 1],
    'Orange': [20, 4, 0],
    'Yellow': [9, 2, 0],
    'Green': [15, 4, 0],
    'Blue': [17, 0, 2],
    'Purple': [12, 0, 0]
}

df = pd.DataFrame(data)

df.set_index('Population', inplace=True)

plt.figure(figsize=(10, 6))
for column in df.columns:
    plt.plot(df.index, df[column], marker='o', label=column)

plt.title('Change of Rainbow Puff Gene Frequency Over Successive Generations')
plt.xlabel('Population')
plt.ylabel('Frequency of Each Gene')
plt.legend(title='Gene')
plt.grid(True)
plt.show()
