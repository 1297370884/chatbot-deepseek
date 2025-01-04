from robyn import Robyn, Request

from apps.deepseek.routes import view_routes

app = Robyn(__file__)


view_routes(app)


if __name__ == "__main__":
    app.start(port=8081, host="0.0.0.0")