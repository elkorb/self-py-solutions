def copy_file_content(source, destination):
    source_file = open(source)
    destination_file = open(destination,'w')
    destination_file.write(source_file.read())