from apps.deepseek.views import (
    chat_view,
    index_view
)



def view_routes(app):
    """
    注册所有路由
    """
    app.add_route(route_type="GET", endpoint="/", handler=index_view)
    app.add_route(route_type="POST", endpoint="/chat", handler=chat_view)

