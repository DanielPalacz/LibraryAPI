from __future__ import annotations

from rest_framework.renderers import JSONRenderer  # type: ignore


class AddApiVersionMiddleware:
    def __init__(self, get_response):  # type: ignore
        self.get_response = get_response

    def __call__(self, request):  # type: ignore
        response = self.get_response(request)

        # Add a custom header
        response["X-API-Version"] = "v1.0"

        return response


class CustomJSONRenderer(JSONRenderer):  # type: ignore
    def render(self, data, accepted_media_type=None, renderer_context=None):  # type: ignore
        if data is None:
            return super().render(data, accepted_media_type, renderer_context)

        # Add 'api_version' only for JSON responses
        if isinstance(data, dict):  # Single object response
            data["api_version"] = "v1.0"
        elif isinstance(data, list):  # List response
            data = {"api_version": "v1.0", "results": data}

        return super().render(data, accepted_media_type, renderer_context)
