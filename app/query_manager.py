from .models import Requests, RequestsFrequency
from common.std_log_format import logger


class QueryManager:
    def __init__(self):
        pass

    def save_request(self, kwargs):
        num1 = kwargs.get('num1')
        num2 = kwargs.get('num2')
        limit = kwargs.get('num_range')
        word1 = kwargs.get('word1').lower()
        word2 = kwargs.get('word2').lower()
        req_id = Requests.get_request_by_param(num1=num1, num2=num2, limit=limit, word1=word1, word2=word2)
        if req_id is False:
            q = Requests(num1=num1, num2=num2, limit=limit, word1=word1, word2=word2)
            q.register()

            if q.id:
                req_q = RequestsFrequency(req_id=q.id, freq=1)
                req_q.register()
                logger.info('Request frequency saved in db')

        elif req_id:
            RequestsFrequency.inc_request_freq(req_id.id)
            logger.info("Request frequency increased")

    def get_freq_request(self):
        q = RequestsFrequency.get_max_frequency()
        params = {}
        req_freq = 0
        if q:
            req_freq = q.freq
            req = Requests.get_request_by_id(q.id)
            params = {
                'num1': req.num1,
                'num2': req.num2,
                'limit': req.limit,
                'str1': req.word1,
                'str2': req.word2,
            }
        return {'params': params, 'frequency': req_freq}
