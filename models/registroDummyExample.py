from fastapi import Query
from pydantic import BaseModel


class RegisterDummyExampleRequest(BaseModel):
    tipoMovimiento: str = Query(pattern='^([0-9]{2})$', description='Tipo Movimiento', examples=['01'])
    fechaAlta: str = Query(default=None, pattern='^([1,2]{1}[0-9]{1}[0-9]{2}[0-1]{1}[0-9]{1}[0-9]{2})?$')
    fichaPemex: str = Query(pattern='^([0-9]{1,6})$')
    regimen: str = Query(pattern='^([0-9]{2})$')
    curp: str = Query(pattern='^([A-Z]{4}\\d{6}[A-Z]{6}[A-Z0-9]{2})$')
    curpNueva: str = Query(default=None, pattern='^([A-Z]{4}\\d{6}[A-Z]{6}[A-Z0-9]{2})$')
    primerApellido: str = Query(min_length=1, max_length=40)
    segundoApellido: str = Query(default=None, min_length=1, max_length=40)
    nombre: str = Query(min_length=1, max_length=40)
    fechaNacimiento: str = Query(pattern='^([1,2]{1}[0-9]{1}[0-9]{2}[0-1]{1}[0-9]{1}[0-9]{2})?$')
    genero: str = Query(min_length=1, max_length=1)
    entidadFederativa: str = Query(min_length=2, max_length=2)
    nacionalidad: str = Query(min_length=3, max_length=3)
    rfc: str = Query(pattern='^([A-Z]{4}[0-9]{6})|([A-Z]{4}[0-9]{6}[A-Z0-9]{3})$')
    sueldoRegistradoPeriodo: str = Query(min_length=1, max_length=13, pattern='^([0-9]{1,10}[.]{1}[0-9]{1,2})$')
    diasAcumulados: str = Query(pattern='^([0-9]{1,5})$')
    indicadorRecursosTransferidos: str = Query(pattern='^([0-9]{2})$')
    importeRecursosTransferidos: str = Query(default=None, pattern='^([0-9]{1,8}|([0-9]{1,8}[.]{1}[0-9]{1,2}))$')
    nivel: str = Query(pattern='^([0-9]{2})$')
    jornada: str = Query(pattern='^([0-9]{2})$')
    tipoRegimen: str = Query(min_length=2, max_length=2)
    gradoResponsabilidad: str = Query(default=None, min_length=2, max_length=2)
    factorConversion: str = Query(pattern='^([0-9]{1,2}|([0-9]{1,2}[.]{1}[0-9]{1,2}))$')
