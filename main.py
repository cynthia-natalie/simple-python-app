from fastapi import FastAPI, Query
from pydantic import BaseModel
from datetime import date
import os
from dotenv import load_dotenv

env_path = r"C:\Users\cynth\Downloads\simple-python-application\.env"
load_dotenv(dotenv_path=env_path)
POSTCODE = os.getenv("POSTCODE")

app = FastAPI()

class AddressResponse(BaseModel):
    startDate: date
    endDate: date
    address: str
    postcode: str

@app.get("/address", response_model=AddressResponse)
def get_address(
    startDate: date = Query(),
    endDate: date = Query()
):
    address = "Orchard Road"
    return {"startDate": startDate, "endDate": endDate, "address": address, "postcode": POSTCODE}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
