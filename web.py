from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor, endpoints
from twisted.web.static import File

class FormPage(Resource):

    def render_POST(self, request):
        password = '1234qwer!!'
        password_received = request.args[b"password-field"][0].decode("utf-8")
        if password_received == password:
            return (b"success")
        else:
            return (b"fail")

root = Resource()
root.putChild(''.encode('utf-8'), File("index.html"))
root.putChild(b'activate', FormPage())
factory = Site(root)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8880)
endpoint.listen(factory)
reactor.run()