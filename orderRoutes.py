from fastapi import APIRouter

orderRouter = APIRouter(
    prefix="/orders",
    tags=['orderere']
)

@orderRouter.get("/")
def greetOrder():
    return{"hello":"order"}