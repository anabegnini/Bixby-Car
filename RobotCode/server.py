from aiohttp import web
from webserver import HandlerWebServer
import RPi.GPIO as GPIO

app = web.Application()
handler = HandlerWebServer()

app.router.add_static('/static', 'static')
app.router.add_post('/command', handler.cmd)

if __name__ == '__main__':
    try:
        web.run_app(app, port=8082)
    finally:
        print('PERDEU CONEXÃO!!')
        GPIO.cleanup()