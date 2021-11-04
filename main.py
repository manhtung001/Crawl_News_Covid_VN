import uvicorn
import nest_asyncio
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse

from utils import *

app = FastAPI(title='API News Covid')

# By using @app.get("/") you are allowing the GET method to work for the / endpoint.


@app.get("/")
def home():
    return "Congratulations! Your API is working as expected. Author: Tung Khong Manh. Now head over to " \
           "/docs. "


@app.get("/news")
def getDataVn():
    res = crawlDataCovidVn()
    return res


if __name__ == '__main__':
  # Allows the server to be run in this interactive environment
  nest_asyncio.apply()

  # Host depends on the setup you selected (docker or virtual env)
  host = "0.0.0.0"

  # Spin up the server!
  uvicorn.run(app, host=host, port=8000)

  # Allows the server to be run in this interactive environment
  nest_asyncio.apply()

  # Host depends on the setup you selected (docker or virtual env)
  host = "0.0.0.0"

  # Spin up the server!
  uvicorn.run(app, host=host, port=8000)
