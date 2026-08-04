import time

class ProcessMiddleware():

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):

        print('1. Entrando en middleware\n')

        response = self.get_response(request)

        print('2. Saliendo del middleware\n')

        return response
    

class TimeToRunMiddleware():

    def __init__(self, get_response):
        
        self.get_response = get_response

    def __call__(self, request):
        
        start = time.time()

        response = self.get_response(request)

        end = time.time()


        print(f'Tiempo de ejecucion {end - start}')

        return response
    

from django.http import JsonResponse

class TooManyRequestMiddleware:

    MAX_REQUEST = 5

    def __init__(self, get_response):

        self.get_response = get_response

        self.count = {}

    def __call__(self, request):

        ip = request.META["REMOTE_ADDR"]

        if ip not in self.count:

            self.count[ip] = 0

        self.count[ip] += 1

        print(self.count)

        if self.count[ip] > self.MAX_REQUEST:

            return JsonResponse(

                {"detail": "Too many requests"},

                status=429

            )

        response = self.get_response(request)

        return response


class BlockMaintenanceMiddleware:


    def __init__(self, get_response):
        self.get_response = get_response
        self.maintenance_mode = True

    def __call__(self, request):
        
        if self.maintenance_mode:

            if request.user.is_staff:
                return self.get_response(request)
            
            return JsonResponse(
                {'detail' : 'Server is under maintenance'},
                status =503
            )

        return self.get_response(request)