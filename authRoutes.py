from fastapi import APIRouter
from database import Session,engine

authRouter = APIRouter(
    prefix="/auth"
)



@authRouter.get("/")
def greetAuth():
    return{"hello":"auth"}