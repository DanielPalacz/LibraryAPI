from __future__ import annotations

from typing import Optional

from rest_framework.response import Response  # type: ignore
from rest_framework.views import exception_handler  # type: ignore


def custom_exception_handler(exc: Exception, context: dict[str, str]) -> Optional[Response]:
    # Calling default exception handler:
    response = exception_handler(exc, context)

    if response is not None:
        # Adding additional info to response. Only added when error flow is handled.
        response.data["api_version"] = "v1.0"

    return response
