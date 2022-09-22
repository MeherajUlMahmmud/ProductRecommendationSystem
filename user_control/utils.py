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
