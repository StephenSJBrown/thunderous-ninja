import peewee as pw
import datetime
from models.base_model import BaseModel

class Centre(BaseModel):
    name = pw.CharField(unique=True)
    place_id = pw.CharField(null=True)
    # location = pw.CharField()
