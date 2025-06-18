from datetime import datetime
from typing import Union, Any

from fastapi import FastAPI, HTTPException

import models

app = FastAPI()

pets = [
    {
        "id": 0,
        "name": "Michi",
        "rfid": "123gehri",
        "silo": 1,
        "profile_picture": "null"
    }
]

silos = [
    {
        "id": 1,
        "stockWeight": 12.6
    },
    {
        "id": 2,
        "stockWeight": 5.3
    }
]


@app.get("/pet/pets/list")
def list_pets(limit: int = 10):
    return pets[0:limit]


@app.get("/pet/silos/list")
def list_silos(limit: int = 10):
    return silos[0:limit]


@app.get("/pet/get/{item_id}")
def get_pet(pet_id: int):
    if pet_id < len(pets):
        return pets[pet_id]
    else:
        return HTTPException(status_code=404, detail="Pet not found")


@app.post("/pet/create")
def create_pet(name: str, rfid: str, silo: int):
    pet = models.Pet(rfid=rfid, name=name, silo=silo)
    pets.append(pet)
    return pet
