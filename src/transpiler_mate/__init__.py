# Transpiler Mate (c) 2025
# 
# Transpiler Mate is licensed under
# Creative Commons Attribution-ShareAlike 4.0 International.
# 
# You should have received a copy of the license along with this work.
# If not, see <https://creativecommons.org/licenses/by-sa/4.0/>.

from __future__ import annotations

from functools import wraps
from http import HTTPStatus
from httpx import (
    Client,
    Headers,
    Request,
    RequestNotRead,
    Response
)
from pydantic import (
    BaseModel,
    ConfigDict
)
from loguru import logger
from typing import (
    Mapping
)

def _decode(value):
    if not value:
        return ''

    if isinstance(value, str):
        return value

    return value.decode("utf-8")

def _log_request(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        request: Request = func(*args, **kwargs)

        logger.warning(f"{request.method} {request.url}")

        headers: Headers = request.headers
        for name, value in headers.raw:
            logger.warning(f"> {_decode(name)}: {_decode(value)}")

        logger.warning('>')
        try:
            if request.content:
                logger.warning(_decode(request.content))
        except RequestNotRead as r:
            logger.warning('[REQUEST BUILT FROM STREAM, OMISSING]')

        return request
    return wrapper

def _log_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        response: Response = func(*args, **kwargs)

        if HTTPStatus.MULTIPLE_CHOICES._value_ <= response.status_code:
            log = logger.error
        else:
            log = logger.success

        status: HTTPStatus = HTTPStatus(response.status_code)
        log(f"< {status._value_} {status.phrase}")

        headers: Mapping[str, str] = response.headers
        for name, value in headers.items():
            log(f"< {_decode(name)}: {_decode(value)}")

        log('')

        if response.content:
            log(_decode(response.content))

        if HTTPStatus.MULTIPLE_CHOICES._value_ <= response.status_code:
            raise RuntimeError(f"A server error occurred when invoking {kwargs['method'].upper()} {kwargs['url']}, read the logs for details")
        return response
    return wrapper

def init_http_logging(http_client: Client):
    http_client.build_request = _log_request(http_client.build_request) # type: ignore
    http_client.request = _log_response(http_client.request) # type: ignore

class TranspilerBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_by_name=True,
        extra='ignore',
        use_enum_values=True,  # Enums dump as .value everywhere
    )

    # Default dumps to JSON-friendly types (URLs -> str, datetimes -> ISO, etc.)
    def model_dump(self, *args, **kwargs):
        kwargs.setdefault('mode', 'json')
        return super().model_dump(*args, **kwargs)

    def model_dump_json(self, *args, **kwargs):
        # stays consistent with model_dump default
        kwargs.setdefault('indent', None)
        return super().model_dump_json(*args, **kwargs)
