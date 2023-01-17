import pathlib
from os import listdir
from os.path import isfile, join
from pathlib import Path

def copy_file_to_snedFolder(filename):
    # filename_without_ext = Path(filename).stem
    src = Path(f"./order/{filename}")
    dest = Path(f"./order_send/{filename}")
    dest.write_text(src.read_text())
    
# orderfilesStr = [f for f in listdir("../order") if isfile(join("../order", f))] 
print(pathlib.Path().resolve())
def get_unsend_filelist():
    orderfilesStr = [f for f in listdir("./order") if isfile(join("./order",f))] 
    ordersendfilesStr = [f for f in listdir("./order_send") if isfile(join("./order_send",f))] 
    unsendfiles = [fn for fn in orderfilesStr if not fn in ordersendfilesStr ]
    print(f'{orderfilesStr=}')
    print(f'{unsendfiles=}')
    return unsendfiles

