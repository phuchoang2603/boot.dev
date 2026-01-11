def list_files(parent_directory, current_filepath=""):
    lst = []
    for filename in parent_directory:
        new_filepath = current_filepath + "/" + filename
        content = parent_directory[filename]
        if content is None:
            lst.append(new_filepath)
        else:
            lst.extend(list_files(content, new_filepath))
    return lst
