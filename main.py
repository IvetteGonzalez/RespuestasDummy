from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import routersExample


app = FastAPI()


# Add router
app.include_router(routersExample.router_dummy)


@app.get("/")
def index():
    return {"message": "servicio disponible"}





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
