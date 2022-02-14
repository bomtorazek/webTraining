from os import listdir
import os.path as osp
import json

# import motor.motor_asyncio
# client = motor.motor_asyncio.AsyncIOMotorClient() # our async driver for mongoDB.
# # 'motor.motor_asyncio.AsyncIOMotorClient' 
# db = client.gtdb # <class 'motor.motor_asyncio.AsyncIOMotorDatabase'> 
# collection = db.gt # <class 'motor.motor_asyncio.AsyncIOMotorCollection'> database -> collection 

data_path =  'C:/Users/esuh/OneDrive - Cognex Corporation/Desktop/main.py/수아랩/스터디 및 공부/2022_1Q_웹개발/파이썬 프론트엔드/react/blog2/src/catdog'
gt_list = [ [ img, None] for img in listdir(data_path)] # path, label
LEN = len(gt_list)


async def create_gt(idx, label):   
    gt_list[int(idx)][1] = int(label)
    return True


async def fetch_gt(idx):
    idx = int(idx)
    idx %= LEN
    return gt_list[idx]

async def export_gt():
    gt_dict ={ name: lbl for name, lbl in gt_list}
    with open('C:/Users/esuh/Downloads/exported_labels.json', 'w') as fp:
        json.dump(gt_dict, fp)

    return gt_dict
