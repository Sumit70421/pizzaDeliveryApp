from fastapi import FastAPI
from authRoutes import authRouter
from orderRoutes import orderRouter


app = FastAPI()

app.include_router(orderRouter)
app.include_router(authRouter)

