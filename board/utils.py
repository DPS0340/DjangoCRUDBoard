from django.http import HttpResponse
import json
import jwt

import sys
sys.path.append("..")
from DjangoCRUDBoard.settings import SECRET_KEY, JWT_ALGORITHM


# 딕셔너리를 JSON으로 전송하는 헬퍼 함수
def send_json(data):
    res = json.dumps(data)
    return HttpResponse(res, content_type='application/json', status=data['status'])


# 가변 인자로 추출된 딕셔너리를 받아오는 헬퍼 함수
def pop_args(dic, *args):
    return {arg: dic[arg] if arg in dic else None for arg in args}

def encode_jwt(dic):
    return jwt.encode(dic, SECRET_KEY, JWT_ALGORITHM)

# 세션에서 디코딩된 JWT 딕셔너리를 가져오는 헬퍼 함수
def decode_jwt(session):
    return jwt.decode(session['JWT_TOKEN'], SECRET_KEY, JWT_ALGORITHM)

def append_jwt_param(session, **kargs):
    decoded = decode_jwt(session)
    for (k, v) in kargs:
        decoded[k] = v
    return encode_jwt(decoded)

# 원본 session을 변경시키는 함수
def delete_jwt_param(session, *args):
    decoded = decode_jwt(session)
    session['JWT_TOKEN'] = encode_jwt(dict(filter(lambda x: x not in args, decoded)))
    return True