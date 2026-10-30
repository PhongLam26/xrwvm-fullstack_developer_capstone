from django.middleware.csrf import CsrfViewMiddleware


class LogoutCsrfMiddleware(CsrfViewMiddleware):
    """Protect the course's legacy GET logout just like a POST request."""

    def process_view(self, request, callback, callback_args, callback_kwargs):
        method = request.method
        if method == "GET" and request.path.rstrip("/") == "/djangoapp/logout":
            request.method = "POST"
        try:
            return super().process_view(
                request, callback, callback_args, callback_kwargs
            )
        finally:
            request.method = method
