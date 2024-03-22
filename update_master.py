def um():
    import pandas as pd
    from read_excel_write_df import rewd
    import json
    import os

    # Obtain week:
    with open("wsr_week_to_path.json", "r") as d:
        path_json = d.read()
        path_dict = json.loads(path_json)

    # with open("master_sales.xlsx", "r") as f:
    #     master_xls = f.read()
    # if os.path.getsize("master_sales.xlsx") != 0:
    #     master_df = pd.read_excel("master_sales.xlsx", engine="openpyxl")
    # else:
    master_df = pd.DataFrame()

    while path_dict:
        path = path_dict.popitem()
        new_df = rewd(path[0], path[1])
        master_df = pd.concat([master_df, new_df]).sort_index(inplace=False)
        print(path)
        # print(new_df.head())
        print(master_df.head())
    # with open("wsr_week_to_path.json", "w") as f:
    #     pass

    master_df.to_excel("master_sales.xlsx", index=True)

    # with open("master_sales.xlsx", "w") as f:
    #     f.write(pd.to_csv(master_df))


if __name__ == "__main__":
    um()
