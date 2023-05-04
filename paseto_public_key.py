import paseto
from paseto.keys.asymmetric_key import AsymmetricSecretKey
from paseto.protocols.v4 import ProtocolVersion4
import time
my_key = AsymmetricSecretKey.generate(protocol=ProtocolVersion4)

payload = {
    'sub': '1234567890',
    'name': 'John Doe',
    'iat': int(time.time()),
    'exp': int(time.time()) + 3600  # Token expira en 1 hora
}
footer={
    "kid": "token-dev-123"
}
# create a paseto token that expires in 5 minutes (300 seconds)
token = paseto.create(
    key=my_key,
    purpose='public',
    claims={'my claims': [1, 2, 3]},
    exp_seconds=300,
    footer=footer
)

print(token)

parsed = paseto.parse(
    key=my_key,
    purpose='public',
    token=token
)
print(parsed)
# {'message': {'exp': '2021-10-25T22:43:20-06:00', 'my claims': [1, 2, 3]}, 'footer': None}