from datetime import date
import shutil
import os
join = os.path.join

source_dir = "./source"
archive_dir = "./source/archive"
destination_dir = "./destination"

# https://www.educative.io/answers/what-is-the-datetime-datetoday-function-in-python
today = date.today().strftime("%Y-%m-%d")
print("Today's date:", today)

today_archive_dir = join(archive_dir, today)

if not os.path.exists(today_archive_dir):
    os.makedirs(today_archive_dir)

codis_file_name = "codis.xml"

# copy codis file
# https://stackoverflow.com/questions/123198/how-to-copy-files
shutil.copyfile(join(source_dir, codis_file_name), join(today_archive_dir, codis_file_name))


archive_files = []

for file in os.listdir(today_archive_dir):
    lowercase = file.lower()

    is_codis = "codis" in lowercase
    is_xml = "xml" in lowercase

    if is_codis and is_xml:
        archive_files.append(file)

for file in archive_files:
    new_file = file.replace("xml", "backup")
    # rename
    # https://www.geeksforgeeks.org/rename-multiple-files-using-python/
    print(file, new_file)
    os.rename(join(today_archive_dir, file), join(today_archive_dir, new_file))
    
# find all xml files in source dir
source_xml_files = []
for file in os.listdir(source_dir):
    if file.lower().endswith("xml"):
        source_xml_files.append(file)

for file in source_xml_files:
    
    # remove all @hid.com
    # https://www.geeksforgeeks.org/reading-writing-text-files-python/
    with open(join(source_dir, file), "r") as f:
        file_data = f.read()

    file_data = file_data.replace("@hid.com", "")

    with open(join(source_dir, file), "w") as f:
        f.write(file_data)
    
    # https://stackoverflow.com/questions/8858008/how-to-move-a-file-in-python
    shutil.move(join(source_dir, file), join(destination_dir, file))
