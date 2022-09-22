import datetime
import os

import jwt
from dotenv import load_dotenv

load_dotenv()


def create_token(user):
    payload = {
        "id": user.id,  # user id to identify the user
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),  # token expiration date
        "iat": datetime.datetime.utcnow(),  # token create time
    }
    token = jwt.encode(payload, os.getenv("JWT_SECRET_KEY"), algorithm=os.getenv("JWT_ALGORITHM"))
    return token


def verify_token(token):
    try:
        payload = jwt.decode(token, os.getenv("JWT_SECRET_KEY"), algorithms=[os.getenv("JWT_ALGORITHM")])
        return payload["id"]
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None