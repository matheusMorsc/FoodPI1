from urllib import response
from typing import List
from fastapi import FastAPI
import databases
import sqlalchemy
from pydantic import BaseModel
from fastapi import FastAPI,status,HTTPException
from typing import Optional,List
from database import SessionLocal
from . import models
 
DATABASE_URL = "postgresql://gqrvrmkxscgslz:f82c919e824d31c3625686bb085e8cb52778ab2bc0161f2866661e071062c891@ec2-3-211-221-185.compute-1.amazonaws.com:5432/d16dj3pn53scrk"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()



menus = sqlalchemy.Table(
    "menus",
    metadata,
    sqlalchemy.Column("nome", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("img", sqlalchemy.String),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL
)

metadata.create_all(engine)

class Menu(BaseModel):
    nome: str
    img: str


app = FastAPI()

db=SessionLocal()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
  

@app.get("/menu/", response_model=List[Menu])   
async def read_restaurantes():
    query = menus.select()
    return await database.fetch_all(query) 

@app.post("/menu/", response_model=Menu)   
async def create_restaurantes(menu: Menu):
    query = menus.insert().values(nome=menu.name, img=menu.img)
    last_record_id = await database.execute(query)
    return {**menu.dict(), "id": last_record_id}

class Item(BaseModel): #serializer
    id:int
    name:str
    description:str
    price:int
    on_offer:bool

    class Config:
        orm_mode=True

@app.get('/items',response_model=List[Item],status_code=200)
def get_all_items():
    items=db.query(models.Item).all()

    return items

@app.get('/item/{item_id}',response_model=Item,status_code=status.HTTP_200_OK)
def get_an_item(item_id:int):
    item=db.query(models.Item).filter(models.Item.id==item_id).first()
    return item

@app.post('/items',response_model=Item,
        status_code=status.HTTP_201_CREATED)
def create_an_item(item:Item):
    db_item=db.query(models.Item).filter(models.Item.name==item.name).first()

    if db_item is not None:
        raise HTTPException(status_code=400,detail="Item already exists")



    new_item=models.Item(
        name=item.name,
        price=item.price,
        description=item.description,
        on_offer=item.on_offer
    )


    

    db.add(new_item)
    db.commit()

    return new_item

@app.put('/item/{item_id}',response_model=Item,status_code=status.HTTP_200_OK)
def update_an_item(item_id:int,item:Item):
    item_to_update=db.query(models.Item).filter(models.Item.id==item_id).first()
    item_to_update.name=item.name
    item_to_update.price=item.price
    item_to_update.description=item.description
    item_to_update.on_offer=item.on_offer

    db.commit()

    return item_to_update

@app.delete('/item/{item_id}')
def delete_item(item_id:int):
    item_to_delete=db.query(models.Item).filter(models.Item.id==item_id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    
    db.delete(item_to_delete)
    db.commit()

    return item_to_delete