# Генератор одноразовых паролей с использованием HMAC

![](docs/demo.gif)

## Как использовать

Сгенерировать `secret_key` на сервере:

<img src="docs/step_1.png" width="600"/>

```
POST /secret-key -d '{"username": "191755@edu.fa.ru"}'

>>> {"secret_key": "CMA2CFRTH5A6SMRGSHKJINXG3525MMVZ"}
```

Сохранить `secret_key` для генерации OTP:

<img src="docs/step_2.png" width="600"/>

```
POST /secret-key -d '{"name": "FA", "secret_key": "CMA2CFRTH5A6SMRGSHKJINXG3525MMVZ"}'

>>> {"status": "ok"}
```

Сгенерировать One-Time Password:

<img src="docs/step_3.png" width="600"/>

```
GET /otp?name=FA

>>> {"otp": "119174", "time_remaining": 29}
```

Авторизоваться, используя OTP:

<img src="docs/step_4.png" width="600"/>

```
POST /auth/login -d '{"username": "191755@edu.fa.ru", "otp": "119174"}'

>>> {"status": "ok"}
```
