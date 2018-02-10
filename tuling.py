import requests


def getResponse(_info):
    # 图灵机器人官网注册账号获取key，免费的
    # http://www.tuling123.com/help/h_cent_webapi.jhtml?nav=doc
    apiUrl = "http://www.tuling123.com/openapi/api"
    data = {
        "key": "这里填写你自己的key",
        "info": _info,
        "userid": "123123123"
    }
    r = requests.post(apiUrl, data=data).json()
    return r
