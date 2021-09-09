import fastapi
from pydantic.main import BaseModel
import uvicorn



# create a data model

class NamesData(BaseModel):
    id: int
    first_name: str
    last_name: str

api  = fastapi.FastAPI()

@api.get()
def get_name(id: int):
    try:
        pass
        # look up id in table.
        # if exists then return the entry 
    except:
        print("That id does not exist.")
    return

@api.post()
def post_name(name: NamesData):
    # do something with the data (Ben's class?)
    name.id
    name.first_name
    name.last_name

@api.put()
def update_name():


@api.delete()
def delete_name():