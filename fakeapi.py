import secrets
from apiflask import APIFlask, Schema
from apiflask.fields import String


app_id = secrets.token_urlsafe(5)

app = APIFlask(
    __name__,
    title=f'Fake API (App ID: {app_id})',
    version='1.0')


class MessageOut(Schema):
    message = String()
    app_id = String()


@app.get('/')
@app.output(MessageOut)
def say_hello():
    return {
        'message': f'Hello! {secrets.token_urlsafe(16)}',
        'app_id': app_id}


if __name__ == '__main__':
  app.run('0.0.0.0', 5000, True)
