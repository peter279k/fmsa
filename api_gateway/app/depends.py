import os
import jwt
import datetime
from modules import CacheAccessToken

from starlette import status
from starlette.requests import Request
from starlette.exceptions import HTTPException


def check_api_key(request: Request):
    x_user = request.headers.get('x-user')
    if x_user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='The x-user is missing in headers!'
        )

    key = request.headers.get('x-api-key')
    if key:
        expired_seconds = int(os.getenv('TOKEN_EXPIRED_MINUTES')) * 60
        cache_access_token = CacheAccessToken()
        is_verified = False
        access_token = cache_access_token.redis.get(x_user)
        if access_token == key:
            decoded = jwt.decode(
                key,
                algorithms=['RS256'],
                options={'verify_signature': False}
            )
            expired_timestamp = decoded['exp']
            now_timestamp = int(datetime.datetime.now().timestamp())
            if (expired_timestamp - now_timestamp) <= expired_seconds:
                is_verified = True

        if is_verified is False:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='You pass the invalid api key in the header!',
            )

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='You didn\'t pass the api key in the header! Header: x-api-key',
    )
