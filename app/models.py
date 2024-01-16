from django.db import models
from common.std_log_format import logger


class Requests(models.Model):
    id = models.BigAutoField(primary_key=True)
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    limit = models.IntegerField()
    word1 = models.CharField(max_length=200, blank=False)
    word2 = models.CharField(max_length=200, blank=False)

    class Meta:
        db_table = 'requests'

    # to save the data
    def register(self):
        self.save()

    @staticmethod
    def get_request_by_param(num1, num2, limit, word1, word2):
        try:
            return Requests.objects.get(num1=num1, num2=num2, limit=limit, word1=word1, word2=word2)
        except:
            return False

    @staticmethod
    def get_request_by_id(pk_id):
        try:
            return Requests.objects.get(id=pk_id)
        except:
            return False


class RequestsFrequency(models.Model):
    req_id = models.BigIntegerField()
    freq = models.IntegerField()

    class Meta:
        db_table = 'request_frequency'
        ordering = ['-freq']

    # to save the data
    def register(self):
        self.save()

    @staticmethod
    def get_request_by_id(request_id):
        try:
            return RequestsFrequency.objects.get(req_id=request_id)
        except:
            return False

    @staticmethod
    def get_max_frequency():
        try:
            return RequestsFrequency.objects.all()[0]
        except:
            return False

    @staticmethod
    def inc_request_freq(request_id):
        try:
            q = RequestsFrequency.objects.get(req_id=request_id)
            q.freq += 1
            q.register()
        except:
            logger.info("Something went wrong while increment request frequency..")


