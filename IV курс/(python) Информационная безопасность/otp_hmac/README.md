# Генератор одноразовых паролей с использованием HMAC

![](docs/demo.gif)

## Как использовать

Сгенерировать `secret_key` на сервере:

```
POST /secret-key --data '{"username": "191755@edu.fa.ru"}'

>>> {"secret_key": "CMA2CFRTH5A6SMRGSHKJINXG3525MMVZ"}
```

Сохранить `secret_key` для генерации OTP:

```
POST /secret-key --data '{"name": "FA", "secret_key": "CMA2CFRTH5A6SMRGSHKJINXG3525MMVZ"}'

>>> {"status": "ok"}
```

Сгенерировать One-Time Password:

```
GET /otp?name=FA

>>> {"otp": "119174", "time_remaining": 29}
```

Авторизоваться, используя OTP:

```
POST /auth/login --data '{"username": "191755@edu.fa.ru", "otp": "119174"}'

>>> {"status": "ok"}
```
