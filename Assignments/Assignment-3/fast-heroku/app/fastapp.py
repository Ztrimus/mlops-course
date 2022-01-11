# import modules
from fastapi import FastAPI, Request
from app.acreCalculation import calculateAcre

# instantiate fast api object
app = FastAPI()


@app.post("/")
async def get_input(request: Request):
    """
    A fast app to take input and invoke acre calcuation module to process input parameter in square fee and return the area in acre
    """
    packet = await request.json()
    length = packet['length']
    width = packet['width']

    areaInAcre = calculateAcre(length, width)

    return {"area-in-acre": areaInAcre, "input": packet}
