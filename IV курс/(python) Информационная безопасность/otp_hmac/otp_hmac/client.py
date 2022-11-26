from datetime import datetime

import pyotp
import uvicorn
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

KEYSTORE: dict[str, str] = {}

app = FastAPI(title="OTP (HMAC) Client App")


class SecretKeySave(BaseModel):
    name: str
    secret_key: str


class SaveOkStatus(BaseModel):
    status: str = "ok"


@app.post("/secret-keys", response_model=SaveOkStatus, tags=["My keys"], name="Save secret key")
def save_secret_key(data: SecretKeySave):
    KEYSTORE[data.name] = data.secret_key
    return SaveOkStatus()


class OTPRead(BaseModel):
    otp: str
    time_remaining: int


@app.get("/otp", response_model=OTPRead, tags=["My keys"], name="Get one-time password")
def get_otp(name: str):
    secret_key = KEYSTORE.get(name)
    if not secret_key:
        raise HTTPException(detail={"message": "Not found"}, status_code=status.HTTP_404_NOT_FOUND)

    totp = pyotp.TOTP(secret_key)
    time_remaining = int(totp.interval - datetime.now().timestamp() % totp.interval)
    return OTPRead(otp=totp.now(), time_remaining=time_remaining)


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=5000)
