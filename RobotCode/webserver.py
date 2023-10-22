from aiohttp.web import Response
from queue import Queue
from carbyvoice import Car


class HandlerWebServer(object):
    
    def __init__(self):     
        self.queue = Queue()
        self.car = Car(self.queue)
        self.car.start()
        pass
    
    async def cmd(self, request):
        data = await request.json()
        self.queue.insert(data["command"])        
        print(self.queue.values)

        return Response(text=str(self.queue.values), content_type='text/html')