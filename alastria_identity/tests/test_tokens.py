from mock import *
import time
from hexbytes import HexBytes

from alastria_identity.services import TokenService
from alastria_identity.types import (
    NetworkDid,
    JwtToken,
    AlastriaSession,
    AlastriaToken,
    AlastriaIdentityCreation)

mock_time = Mock()
mock_time.return_value = time.time()

private_key = '1da6847600b0ee25e9ad9a52abbd786dd2502fa4005dd5af9310b7cc7a3b25db'


def test_jwt():
    jwt = JwtToken(
        header={
            "alg": "ES256K",
            "typ": "JWT"
        },
        payload={
            "iss": "iss",
            "gwu": "gwu",
            "cbu": "cbu",
            "ani": "ani",
            "exp": 1,
            "iat": int(time.time())
        })

    service = TokenService(private_key=private_key)
    signed_jwt = service.sign_jwt(jwt)
    decoded_jwt = service.decode_jwt(signed_jwt)

    assert service.verify_jwt(signed_jwt)
    assert decoded_jwt.get('header') == jwt.header
    assert decoded_jwt.get('payload') == jwt.payload


def test_create_did_with_network_did():
    expected_did = 'did:ala:789:012:345'
    network_did = NetworkDid.from_did('123:456:789:012:345')
    service = TokenService(private_key=private_key)

    did = service.create_did(network_did)

    assert did == expected_did


def test_create_alastria_token_only_required_args():
    expected_jwt = {
        "header": {
            "alg": "ES256K",
            "typ": "JWT"
        },
        "payload": {
            "iss": "iss",
            "gwu": "gwu",
            "cbu": "cbu",
            "ani": "ani",
            "exp": 1,
            "iat": int(time.time())
        }
    }

    jwt = AlastriaToken('iss', 'gwu', 'cbu', 'ani', 1).build_jwt()

    assert jwt == expected_jwt


def test_create_alastria_token_all_args():
    expected_jwt = {
        "header": {
            "alg": "ES256K",
            "typ": "JWT",
            "kid": "kid",
            "jwk": "jwk"
        },
        "payload": {
            "iss": "iss",
            "gwu": "gwu",
            "cbu": "cbu",
            "ani": "ani",
            "exp": 1,
            "iat": int(time.time()),
            "nbf": 1,
            "jti": "jti"
        }
    }

    jwt = AlastriaToken('iss', 'gwu', 'cbu', 'ani', 1,
                        "kid", "jwk", 1, "jti").build_jwt()

    assert jwt == expected_jwt


def test_create_alastria_session_only_required_args():
    expected_jwt = {
        "header": {
            "alg": "ES256K",
            "typ": "JWT"
        },
        "payload": {
            "@context": ['https://alastria.github.io/identity/artifacts/v1', 'CustomContext'],
            "type": ['AlastriaSession', 'CustomType'],
            "iss": "iss",
            "alastriaToken": "0x01234",
            "iat": int(time.time())
        }
    }

    jwt = AlastriaSession(['CustomContext'], ['CustomType'],
                          'iss', '0x01234').build_jwt()

    assert jwt == expected_jwt


def test_create_alastria_session_all_args():
    expected_jwt = {
        "header": {
            "alg": "ES256K",
            "typ": "JWT",
            "kid": "kid",
            "jwk": "jwk"
        },
        "payload": {
            "@context": ['https://alastria.github.io/identity/artifacts/v1', 'CustomContext'],
            "type": ['AlastriaSession', 'CustomType'],
            "iss": "iss",
            "alastriaToken": "0x01234",
            "jti": "jti",
            "exp": 1,
            "nbf": 1,
            "iat": int(time.time())
        }
    }

    jwt = AlastriaSession(['CustomContext'], ['CustomType'],
                          'iss', '0x01234', 'jti', 1, 1, 'kid', 'jwk').build_jwt()

    assert jwt == expected_jwt


def test_create_alastria_identity_creation_only_required_args():
    expected_jwt = {
        "header": {
            "alg": "ES256K",
            "typ": "JWT",
        },
        "payload": {
            "@context": ['https://alastria.github.io/identity/artifacts/v1', 'CustomContext'],
            "type": ['AlastriaIdentityCreation', 'CustomType'],
            "createAlastriaTX": "0x4321",
            "alastriaToken": "0x01234",
            "publicKey": "0x0011",
            "iat": int(time.time())
        }
    }

    jwt = AlastriaIdentityCreation(
        ['CustomContext'], ['CustomType'], '0x4321', '0x01234', '0x0011').build_jwt()

    assert jwt == expected_jwt


def test_create_alastria_identity_creation_all_args():
    expected_jwt = {
        "header": {
            "alg": "ES256K",
            "typ": "JWT",
            "kid": "kid",
            "jwk": "jwk"
        },
        "payload": {
            "@context": ['https://alastria.github.io/identity/artifacts/v1', 'CustomContext'],
            "type": ['AlastriaIdentityCreation', 'CustomType'],
            "createAlastriaTX": "0x4321",
            "alastriaToken": "0x01234",
            "publicKey": "0x0011",
            "jti": "jti",
            "exp": 1,
            "nbf": 1,
            "iat": int(time.time())
        }
    }

    service = TokenService(private_key=private_key)

    jwt = AlastriaIdentityCreation(['CustomContext'], [
                                   'CustomType'], '0x4321', '0x01234', '0x0011', 'jti', 1, 1, 'kid', 'jwk').build_jwt()

    assert jwt == expected_jwt


def test_psmhash():
    foo_signed_jwt = '''
                    eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksiLCJraWQiOiJkaWQ6YWxhOnF1b3I6cmVkVDo4ZjQ0MDA0O
                    WNiYmU1YzZiYzllZmY0NjM2OWY5MDkxZjFkODEzMzNjI2tleXMtMSJ9.
                    eyJqdGkiOiJmaGJ0aDlocnVkbCIsImlzcyI6ImRpZDphbGE6cXVvcjpyZWRUOjhmNDQwMDQ5Y2JiZTVjNmJjOW
                    VmZjQ2MzY5ZjkwOTFmMWQ4MTMzM2MiLCJzdWIiOiJkaWQ6YWxhOnF1b3I6cmVkVDowYTc3ODAyOTVhYjgwNmY4
                    Y2RiNjIzY2ZhNDhhNzQ5ZTk1OTE4MTU5IiwiaWF0IjoxNTkxMTczNjkzLCJleHAiOjE1OTEyNjAwOTMxNDMsIm
                    5iZiI6MTU5MTE3MzY5MzE0MywidmMiOnsiQGNvbnRleHQiOlsiaHR0cHM6Ly93d3cudzMub3JnLzIwMTgvY3Jl
                    ZGVudGlhbHMvdjEiLCJKV1QiXSwidHlwZSI6WyJWZXJpZmlhYmxlQ3JlZGVudGlhbCIsIkFsYXN0cmlhRXhhbX
                    BsZUNyZWRlbnRpYWwiXSwiY3JlZGVudGlhbFN1YmplY3QiOnsibGV2ZWxPZkFzc3VyYW5jZSI6MywiZnVsbG5h
                    bWUiOiJEYW5pZWwgZGUgbGEgU290YSJ9fX0.
                    DZsssNSg0_NzrjSiCNrkVss9-bnUZxFrbH6oN9NluCJwg0MqwAvyvwtKww_f_lF1sMVXt6UZyl_gJEkCSaspWw',
                    'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksiLCJraWQiOiJkaWQ6YWxhOnF1b3I6cmVkVDo4ZjQ0MDA0OWNiY
                    mU1YzZiYzllZmY0NjM2OWY5MDkxZjFkODEzMzNjI2tleXMtMSJ9.
                    '''
    foo_did = 'did:ala:quor:redT:8f440049cbbe5c6bc9eff46369f9091f1d81333'
    expected_psmash = HexBytes('0xdb61eb3ad9020e8fe0509618a8579fe350cb16be20fbfd43a098e152fa9b3a31')

    psmhash = TokenService.psm_hash(foo_signed_jwt, foo_did)

    assert psmhash == expected_psmash
