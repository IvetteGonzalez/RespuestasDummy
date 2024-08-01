from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi, get_definitions
from routers import routersExample


app = FastAPI()


app.include_router(routersExample.router_dummy)


@app.get("/")
def index():
    return {"message": "servicio disponible"}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    error400 = {"codigo": "string",
   "descripcion": {
		"ValidationFailureDetail": {
						 "message": "values does not match pattern in namespace http://www.procesar.com.mx/ArquitecturaSW/DataTypes/tiposComunesProcesar/\n",
	      "xmlLocation": exc.errors()
					}
		 },
  "locacion": "string"
}
    return PlainTextResponse(str(error400), status_code=400)

# Define CORS settings
origins = ["*"]  # Allow requests from any origin

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)



def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="1.0.0",
        openapi_version='3.0.1',
        summary="This is a very custom OpenAPI schema",
        description="Here's a longer description of the custom **OpenAPI** schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi