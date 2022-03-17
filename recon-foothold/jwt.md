# jwt decode

check: https://jwt.io

# jku/jwks

## generate public key from jku

https://8gwifi.org/jwkconvertfunctions.jsp

## tamper jku (to your url) and sign it your public/private key (based on https://book.hacktricks.xyz/pentesting-web/hacking-jwt-json-web-tokens)

generate key pair

```bash
openssl genrsa -out rsa-keypair.pem 2048
openssl rsa -in rsa-keypair.pem -pubout -out public-key.pem
openssl pkcs8 -topk8 -inform PEM -outform PEM -nocrypt -in rsa-keypair.pem -out private-key.pem
```

you can now go to jwt.io change the algorithm to rsa256 and paste your payload and keys

valid jwks:

```json
{
  "kty": "RSA",
  "use": "sig",
  "kid": "domain",
  "alg": "RS256",
  "n": "long as base64 string",
  "e": "ABBA"
}
```

to generate "n" and "e" run the follow python script:

```python
from Crypto.PublicKey import RSA
import struct
import base64

fp = open("public-key.pem", "r")
key = RSA.importKey(fp.read())
fp.close()

def long_to_base64(n):
    """
    Borrowed from jwkest.__init__
    """

    def long2intarr(long_int):
        _bytes = []
        while long_int:
            long_int, r = divmod(long_int, 256)
            _bytes.insert(0, r)
        return _bytes

    bys = long2intarr(n)
    data = struct.pack("%sB" % len(bys), *bys)
    if not data:
        data = "\x00"
    s = base64.urlsafe_b64encode(data).rstrip(b"=")
    return s.decode("ascii")

print("n:", long_to_base64(key.n))
print("e:", long_to_base64(key.e))
```

## tampering and other stuff

check out https://github.com/ticarpi/jwt_tool
