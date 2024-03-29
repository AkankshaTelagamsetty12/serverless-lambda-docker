from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import os
import zipfile
import io
import tensorflow as tf
from random import randint
import numpy as np
import matplotlib.pyplot as plt
#from nowcast_reader import read_data
from LocationFetch3 import *

app = FastAPI()
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    location: str
    year: Optional[int] = None
    month: Optional[int] = None
    day: Optional[int] = None

app = FastAPI()


@app.get("/get_pred/{location_name}")
def get_pred(location_name: str , year : int  , month :int, day : int):
    
    #location_name = location_name
    #this_file_path = "./images/"+ str(location_name) + "/images"
    this_file_path = "./images/"+ str(location_name) +"/"
    p, flag,episode_narr,event_narr = prediction(location_name, year, month, day)
    if flag ==1:
        filep = os.path.join(this_file_path,"files/fin.jpg")
        if os.path.exists(filep):
            return FileResponse(filep , media_type="image/jpeg", filename= "myfin.jpg")
    elif flag==0:

        return {"error:file not found"}
    
    #return {"location_name" : location_name, "Year" : year, "Month" : month, "Day":day}
