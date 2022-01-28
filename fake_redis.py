class FakeRedis:
    def __init__(self):
        self._dt = {}

    def set(self, k, v):
        self._dt[k] = v

    def get(self, k, default=None):
        return self._dt.get(k, default)

    def delete(self, k):
        if k in self._dt:
            del self._dt[k]

    def incr(self, k, inc) -> int:
        if k not in self._dt:
            self._dt[k] = 0
        else:
            self._dt[k] += inc
        return self._dt[k]
