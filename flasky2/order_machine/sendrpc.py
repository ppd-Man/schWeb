from jsonrpcclient import request
from time import sleep
import random
import os
from os import listdir
from os.path import isfile, join
from pathlib import Path
import shutil
import json
import payconfiguration
def copy_file_to_sendFolder(filename):
    # filename_without_ext = Path(filename).stem
    workdir = payconfiguration.WORK_DIR
    src = Path(f"{workdir}/order/{filename}")
    dest = Path(f"{workdir}/order_send/{filename}")
    dest.write_text(src.read_text())
    
def get_unsend_files():
    workdir = payconfiguration.WORK_DIR
    orderfilesStr = [f for f in listdir(f"{workdir}/order") if isfile(join(f"{workdir}/order",f))] 
    ordersendfilesStr = [f for f in listdir(f"{workdir}/order_send") if isfile(join(f"{workdir}/order_send",f))] 
    unsendfiles = [fn for fn in orderfilesStr if not fn in ordersendfilesStr ]
    print(f'{orderfilesStr=}')
    print(f'{unsendfiles=}')
    return unsendfiles

def checkOrderSendFloderExist():
    workdir = payconfiguration.WORK_DIR
    if os.path.isdir(f"{workdir}/order_send"):
        return True
    os.mkdir(f"{workdir}/order_send")

def main():
    checkOrderSendFloderExist()
    a = {"ordernum":"a1234","resp":"010002000300040000500"}
    while True:
        orderfilesStr=get_unsend_files()
        for od in orderfilesStr:
            print(orderfilesStr)  
            txt = Path(f'{workdir}/order/{od}').read_text()
            jsontxt = json.loads(txt)
            print(f'{jsontxt=}')
            try :
                response = request("http://127.0.0.1:9000","jsonrpc_addorder",order=jsontxt)
                print(f'response={response}')
            except:
                print('rpc send not find')
                break
            
            copy_file_to_sendFolder()
        sleep(2)
if __name__ == "__main__":
    main()
# while True:
    
    
#     # num=random.randint(0,1000)
#     # a = {"ordernum":f"a{num:04}","resp":"010002000300040000500"}
    
#     response = request("http://127.0.0.1:5000","jsonrpc_addorder",order=a)
#     sleep(2)