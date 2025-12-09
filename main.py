from fastapi import FastAPI
import uvicorn
from uvicorn import run
from contas_a_pagar_e_receber.routers import contas_a_pagar_e_receber_routers
from shared.database import engine, Base


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


app = FastAPI()

@app.get("/")
def oi_mundo() -> str:
    return ("Oi eu sou o caio")

app.include_router(contas_a_pagar_e_receber_routers.router)

if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0" ,port = 8001)