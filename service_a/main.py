from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Service A HOST
SERVICE_A_HOST = "0.0.0.0"

# Service A PORT
SERVICE_A_PORT = 8011

app = FastAPI(
    title="Service A FastAPI Client",
    version="0.1.0",
)

@app.get("/ping")
def ping():
    return JSONResponse(
        {
            "message": "Greetings from Service A!"
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=SERVICE_A_HOST, port=SERVICE_A_PORT) 