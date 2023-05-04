import paseto
from paseto.keys.symmetric_key import SymmetricKey
from paseto.protocols.v4 import ProtocolVersion4
import time

# Crear un payload para el token
payload = {
    'sub': '1234567890',
    'name': 'John Doe',
    'iat': int(time.time()),
    'exp': int(time.time()) + 3600  # Token expira en 1 hora
}

footer={
    "kid": "token-dev-123"
}

# Crear un token PASETO con la clave secreta
# key = paseto.Key.new(version=paseto.Versions.V2, purpose=paseto.Purpose.PUBLIC)
key = SymmetricKey.generate(protocol=ProtocolVersion4)

token = paseto.create(
    key=key,
    purpose='local',
    claims=payload,
    exp_seconds=300,
    footer=footer
)

# Imprimir el token PASETO
print(token)

# Decodificar y verificar el token PASETO
parsed = paseto.parse(
    key=key,
    purpose='local',
    token=token,
)

print(parsed)
