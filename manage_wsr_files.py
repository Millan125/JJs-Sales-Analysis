def main():
    import os
    import json
    from fnmatch import fnmatch

    # assign downloads directory path
    dir_path = r"C:\Users\milla\Downloads"

    # create list to store files from downloads
    are_files = []
    wsr_files = []
    new_dict = {}

    # check if current path is a file and add to are_files
    for path in os.listdir(dir_path):

        if os.path.isfile(os.path.join(dir_path, path)):
            are_files.append(os.path.join(dir_path, path))

    # check if files in are_files contain "Weekly Sales Report" and add those to wsr_files
    for file in are_files:
        if fnmatch(file, "*Weekly Sales Report*") and file[-5] != ")":
            wsr_files.append(file)

    # create a dictionary 'Week #, -year-': path
    for file in wsr_files:
        if file[-17] == " ":
            key = file[-16:-4]
        else:
            key = file[-17:-4]
        new_dict[key] = file

    # open dictionary file, check if keys exist, write to dict if they do not
    with open("wsr_week_to_path.json", "w+") as f:
        old_json_data = f.read()
        if old_json_data:
            data = json.loads(old_json_data)
        else:
            data = {}

        for x, y in new_dict.items():
            if x not in data.keys():
                data[x] = y
        new_json_data = json.dumps(data)
        f.write(new_json_data)


if __name__ == "__main__":
    main()
