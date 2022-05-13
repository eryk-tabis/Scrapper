import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")
item_id = input("Insert item id:\n")

opinions = pd.read_json(f'opinions/{item_id}.json')
print(opinions)
opinions.score = opinions.score.map(lambda x: float(x.split("/")[0].replace(',', '.')))
opinions_count = len(opinions.index)
pros_count = opinions.pros.map(bool).sum()
cons_count = opinions.cons.map(bool).sum()
average_score = opinions.score.mean().round(2)

recomendation = opinions.recomendation.value_counts(dropna=False).sort_index().reindex(["Nie polecam", "Polecam", None])
recomendation.plot.pie(
    label="",
    autopct="%1.1f%%",
    colors=['forestgreen', 'lightskyblue', 'crimson'],
    labels=["Nie polecam", "Polecam", "Nie mam zdania"]
)
plt.title("Rekomendacja")
plt.savefig(f"plots/{item_id}_recomendation.png")
plt.close()

score = opinions.score.value_counts().sort_index().reindex(list(np.arange(0,5.5,0.5)), fill_value=(0))
score.plot.bar()
plt.title("Oceny produktu")
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")
plt.grid(True)
plt.xticks(rotation=0)
plt.savefig(f"plots/{item_id}_stars.png")
plt.close()

