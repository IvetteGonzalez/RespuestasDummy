from fastapi import APIRouter
from models import registroDummyExample
from generadorDummy import RespuestasExample


router_dummy = APIRouter(
    tags=["Dummy"],
)


@router_dummy.post("")
def registro_dummy_example(request: registroDummyExample.RegisterDummyExampleRequest):
    getresponse = RespuestasExample.genera_dummy_example()
    return getresponse
