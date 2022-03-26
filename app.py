# Copyright © 2022 TerminalWarlord
# Encoding = 'utf-8'
# Licensed under MIT License
# https://github.com/TerminalWarlord/
# Data: 26.03.2022 - 16:31(BST)

from fastapi import FastAPI
from main import main
import uvicorn

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/{rating}/{handle}")
async def read_item(rating, handle):
	print(rating, handle)
	return main(rating, handle)

# @app.get("/lmao/{username}")
# async def read_item(username):
#     return user_api(username)

# @app.get("/insta/")
# async def read_item(link):
# 	return insta_dl(link)



if __name__ == "__main__":
  uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)