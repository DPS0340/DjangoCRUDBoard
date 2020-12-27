from django.http import HttpResponse
import json


# 딕셔너리를 JSON으로 전송하는 헬퍼 함수
def send_json(data):
    res = json.dumps(data)
    return HttpResponse(res, content_type='application/json')


# 가변 인자로 추출된 딕셔너리를 받아오는 헬퍼 함수
def pop_args(dict_, *args):
    return {arg: dict_[arg] if arg in dict_ else None for arg in args}
