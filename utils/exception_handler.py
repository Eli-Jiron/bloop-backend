from rest_framework.views import exception_handler


def simple_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None and isinstance(response.data, dict):
        # Si hay múltiples errores, tomamos el primero
        first_error_key = next(iter(response.data))
        first_error_message = response.data[first_error_key]

        if isinstance(first_error_message, list) and first_error_message:
            response.data = {"detail": first_error_message[0]}

    return response
