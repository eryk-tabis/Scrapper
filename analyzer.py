import os
import pandas as pd
print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")
item_id = input("Insert item id:\n")

opinions = pd.read_json(f'opinions/{item_id}.json')
print(opinions)