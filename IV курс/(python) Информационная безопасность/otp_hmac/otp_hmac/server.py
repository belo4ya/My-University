import pyotp
import uvicorn
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

KEYSTORE: dict[str, str] = {}

app = FastAPI(title="OTP (HMAC) Server")


class SecretKeyCreate(BaseModel):
    username: str


class SecretKeyRead(BaseModel):
    secret_key: str


@app.post(
    "/secret-keys",
    response_model=SecretKeyRead,
    status_code=status.HTTP_201_CREATED,
    tags=["Secret keys"],
    name="Create secret key",
)
def create_secret_key(data: SecretKeyCreate):
    secret_key = pyotp.random_base32()
    KEYSTORE[data.username] = secret_key
    return SecretKeyRead(secret_key=secret_key)


class LoginCreds(BaseModel):
    username: str
    otp: str


class LoginOkStatus(BaseModel):
    status: str = "ok"


def bad_credentials() -> HTTPException:
    return HTTPException(detail={"message": "bad credentials"}, status_code=status.HTTP_401_UNAUTHORIZED)


@app.post("/auth/login", response_model=LoginOkStatus, tags=["Auth"])
def login(creds: LoginCreds):
    secret_key = KEYSTORE.get(creds.username)
    if not secret_key:
        raise bad_credentials()

    totp = pyotp.TOTP(secret_key)
    if not totp.verify(creds.otp):
        raise bad_credentials()

    return LoginOkStatus()


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
