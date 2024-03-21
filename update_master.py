import pandas as pd
from read_excel_write_df import rewd

# Obtain week:
with open("wsr_week_to_path.txt", "r") as d:
    path_dict = d.read()

with open("master_sales.csv", "r") as f:
    master_csv = f.read()

if master_csv:
    master_df = pd.read_csv(master_csv)
else:
    master_df = pd.DataFrame()

while path_dict:
    path = path_dict.popitem()
    new_df = rewd(path[0], path[1])
    new_master_df = pd.concat([master_df, new_df]).sort_inndex(inplace=True)

new_master_csv = ""
new_master_df.to_csv(new_master_csv, index=False)

with open("wsr_week_to_path.txt", "w") as f:
    pass

with open("master_sales.csv", "w") as f:
    f.write(new_master_csv)
