from fastapi import FastAPI
import requests
# from fastapi.middleware.cors import CORSMiddleware

# from app.routes.auth import router as auth_router
# from app.routes.user import router as user_router
# from app.routes.posts import router as posts_router

# app = FastAPI()

# app.include_router(auth_router)
# app.include_router(user_router)
# app.include_router(posts_router)

app = FastAPI()

# origins = [
#     "http://localhost:3000",
#     "http://localhost",
#     "http://localhost:8080",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
# @app.get("/")
# def read_root():
#     return("msg: Hello world")

@app.get("/list/{form_input}/")
async def form_input_data(form_input : str):
    reqs= requests.Session()
    reqs.headers.update({'Authorization': 'Token 1a6783768326283428fc7689f3477087ec7ceee9'})
    keyword= 'kidnapping'
    page = 1
    response =  reqs.post('https://api.indiankanoon.org/search/?formInput=%s&pagenum=%s' % (keyword, page))
    # response =  reqs.post('https://api.indiankanoon.org/search/?formInput=kidnapping&pagenum=1')
    data =  response.json()
    # if(response != None):
    #     with open('data.csv', 'a') as f:
    #         f.write(data)
    #         f.close()

    return data
    