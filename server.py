import asyncio
from aiohttp.web import Application
from Todos import handlers


def create_server(loop, handler, host, port):
    srv = loop.create_server(handler, host, port)
    return loop.run_until_complete(srv)


def create_app(loop):
    app = Application(loop=loop)
    handler = app.make_handler()
    return app, handler


def run_server():
    loop = asyncio.get_event_loop()
    app, handler = create_app(loop=loop)
    server = create_server(loop=loop, handler=handler,
                           host='0.0.0.0', port=9000)

    app.router.add_route('GET', '/todos', handlers.get_all_todos)
    app.router.add_route('POST', '/todos', handlers.create_todos)
    app.router.add_route('PATCH', '/todos', handlers.update_todos)
    app.router.add_route('DELETE', '/todos', handlers.remove_todos)
    app.router.add_route('GET', '/todos/{id}', handlers.get_todo)
    app.router.add_route('PATCH', '/todos/{id}', handlers.update_todo)
    app.router.add_route('DELETE', '/todos/{id}', handlers.remove_todo)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.close()
        loop.run_until_complete(server.wait_closed())
        loop.run_until_complete(handler.finish_connections(1.0))
        loop.run_until_complete(app.finish())
    loop.close()


if __name__ == '__main__':
    run_server()
