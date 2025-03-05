import httpx
import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Service B HOST
SERVICE_B_HOST = "0.0.0.0"

# Service B PORT
SERVICE_B_PORT = 8012

# Core URL where Service A is available
SERVICE_A_URL = os.environ.get("SERVICE_A_URL", "http://service-a:8011")

app = FastAPI(
    title="Service B FastAPI Client",
    version="0.1.0",
)

@app.get("/ping_service_a")
def ping_service_a() -> JSONResponse:
    with httpx.Client() as client:
        response_from_a = client.get(f"{SERVICE_A_URL}/ping")
        response = f"{response_from_a.json()['message']} (via Service B)"
        return JSONResponse({
            "message": response
        })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=SERVICE_B_HOST, port=SERVICE_B_PORT) 