def rewd(key, path):
    import pandas as pd

    df = pd.read_excel(r"" + path, usecols="D:Q")

    final_df = df.loc[[7, 8, 29]]

    df_filled = final_df.fillna(method="ffill", axis=1)

    unique_dates = pd.to_datetime(df_filled.iloc[0].unique(), format="%m/%d/%Y")

    final_df = pd.DataFrame(
        index=unique_dates, columns=["Week", "AM", "PM", "Total", "Note"]
    )

    am_filtered_df = df_filled.loc[:, df_filled.iloc[1] == "AM"].copy()
    am_filtered_df.replace(",", "", regex=True, inplace=True)
    data1 = am_filtered_df.iloc[2].to_list()
    data2 = [float(i) for i in data1]
    final_df["AM"] = data2

    pm_filtered_df = df_filled.loc[:, df_filled.iloc[1] == "PM"].copy()
    pm_filtered_df.replace(",", "", regex=True, inplace=True)
    data3 = pm_filtered_df.iloc[2].to_list()
    data4 = [float(j) for j in data3]
    final_df["PM"] = data4

    final_df["Total"] = final_df["AM"] + final_df["PM"]

    final_df["Week"] = key

    return final_df


if __name__ == "__main__":
    rewd(
        "C:\\Users\\milla\\Downloads\\Weekly Sales Report - 0215 - Forbes Ave, Pittsburgh, PA   - Week 51, 2023.xls"
    )
