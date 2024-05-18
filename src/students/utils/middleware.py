import datetime
import logging

LOGGER = logging.getLogger("custom_logger")


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        print('Before view')
        LOGGER.debug(f"Before request from {request.user}")
        # request.current_time = datetime.datetime.now()
        setattr(request, 'current_time', datetime.datetime.now())
        response = self.get_response(request)
        print('After view')

        return response
