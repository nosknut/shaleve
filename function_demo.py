import os

def find_files(folder, search_values):
    filenames = []

    for filename in os.listdir(folder):
        lowercase_filename = filename.lower()

        is_matching = True

        for search_value in search_values:
            if search_value not in lowercase_filename:
                is_matching = False

        if is_matching:
            filenames.append(filename)
    
    return filenames        
    
    
codis_files = find_files("./source", ["codis"])
xml_files = find_files("./source", ["xml"])
codis_xml_files = find_files("./source", ["codis", "xml"])

print("Codis Files:", codis_files)
print("XML Files:", xml_files)
print("codis.xml files:", codis_xml_files)