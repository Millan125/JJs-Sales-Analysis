def um():
    import pandas as pd
    from read_excel_write_df import rewd
    import json
    import os

    # Obtain week:
    with open("wsr_week_to_path.json", "r") as d:
        path_json = d.read()
        path_dict = json.loads(path_json)

    with open("wsr_week_to_path.json", "w") as f:
        pass

    # with open("master_sales.xls", "r") as f:
    #     master_xls = f.read()
    if os.path.getsize("master_sales.xls") != 0:
        master_df = pd.read_excel("master_sales.xls")
    else:
        master_df = pd.DataFrame()

    # if master_xls:
    #     master_df = pd.read_csv(master_xls)
    # else:
    #     master_df = pd.DataFrame()

    while path_dict:
        path = path_dict.popitem()
        new_df = rewd(path[0], path[1])
        new_master_df = pd.concat([master_df, new_df]).sort_index(inplace=True)

    with open("wsr_week_to_path.json", "w") as f:
        pass

    new_master_df.to_excel("master_sales.xls", index=False)

    # with open("master_sales.xls", "w") as f:
    #     f.write(pd.to_csv(new_master_df))
    um()


if __name__ == "__main__":
    um()
