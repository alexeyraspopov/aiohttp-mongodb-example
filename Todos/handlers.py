from aiohttp.web import Response


def get_all_todos():
    return Response(text='get_all_todos')


def create_todos():
    return Response(text='create_todos')


def update_todos():
    return Response(text='update_todos')


def remove_todos():
    return Response(text='remove_todos')


def get_todo():
    return Response(text='get_todo')


def update_todo():
    return Response(text='update_todo')


def remove_todo():
    return Response(text='remove_todo')
