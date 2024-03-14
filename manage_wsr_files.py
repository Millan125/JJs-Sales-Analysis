def main():
    import os
    import json
    from fnmatch import fnmatch

    #assign downloads directory path
    dir_path = r"C:\Users\milla\Downloads"

    #create list to store files from downloads
    are_files = []
    wsr_files = []
    new_dict = {}

    # check if current path is a file and add to are_files
    for path in os.listdir(dir_path):
    
        if os.path.isfile(os.path.join(dir_path, path)):
            are_files.append(os.path.join(dir_path, path))

    #check if files in are_files contain "Weekly Sales Report" and add those to wsr_files
    for file in are_files:
        if fnmatch(file, "*Weekly Sales Report*"):
            wsr_files.append(file)
    
    
    #create a dictionary 'Week #, -year-': path
    for file in wsr_files:
        key = file[-17:-4]
        new_dict[key] = file

    #open dictionary file, check if keys exist, write to dict if they do not
    with open('wsr_week_to_path.txt', "w+") as f:
        data = dict(f.read())

        for x, y in new_dict.items():
            if x not in data.keys():
                new_dict[x] = y
                data.update(new_dict)
        f.write(str(data))
    
if __name__ == "__main__":
    main()