# import uvicorn

# if __name__ == "__main__":
#     uvicorn.run("APITEST:app", host="127.0.0.1", port=8000, reload=True)

from API1 import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
