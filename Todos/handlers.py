from aiohttp.web import Response


def get_all_todos(request):
    return Response(text='get_all_todos')


def create_todos(request):
    return Response(text='create_todos')


def update_todos(request):
    return Response(text='update_todos')


def remove_todos(request):
    return Response(text='remove_todos')


def get_todo(request):
    id = request.match_info['id']
    return Response(text='get_todo {}'.format(id))


def update_todo(request):
    id = request.match_info['id']
    return Response(text='update_todo {}'.format(id))


def remove_todo(request):
    id = request.match_info['id']
    return Response(text='remove_todo {}'.format(id))
