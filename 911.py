def are_files_equal(file1, file2):
    a = open(file1,"r")
    b = open(file2,"r")
    return a.read() == b.read()