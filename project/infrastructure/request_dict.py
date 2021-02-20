from flask import Request

class RequestDictionary(dict):
    def __getattr__(self, key):
        return self.get(key)

def create(**route_args) -> RequestDictionary:
    request = Request
    data = {
        **request.args,
        **request.headers,
        **request.form,
        **route_args
    }
    return RequestDictionary(data)