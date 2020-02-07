import peewee as pw
import datetime
from models.base_model import BaseModel

class Centre(BaseModel):
    name = pw.CharField(unique=True)
    location = pw.CharField()

    def validate():
        duplicate_name = Centre.get_or_none(Centre.name == self.name)

        if self.id == None:
            if duplicate_username:
                self.errors.append(f'{self.username} is unvailable!')

        
