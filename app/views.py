from django.http import JsonResponse
from common.utils import validate_param, validate_range
from app.program import AppFizzBuzz
from app.query_manager import QueryManager
from common.std_log_format import logger


def get_fizz_buzz_resp(request):
    if request.method == 'GET':
        try:
            num1 = validate_param(request.GET.get('num1'), int, 'num1')
            num2 = validate_param(request.GET.get('num2'), int, 'num2')
            num_range = validate_param(request.GET.get('limit'), int, name='limit')
            word1 = validate_param(request.GET.get('str1'), name='str1')
            word2 = validate_param(request.GET.get('str2'), name='str2')

            # make range bound for int, str to avoid memory overflow at run
            num1 = validate_range(num1, int, 'num1')
            num2 = validate_range(num2, int, 'num2')
            num_range = validate_range(num_range, int, 'limit')
            word1 = validate_range(word1, name='str1')
            word2 = validate_range(word2, name='str2')

            param = {'num1': num1, 'num2': num2, 'num_range': num_range, 'word1': word1, 'word2': word2}
            obj = AppFizzBuzz(param)
            output = obj.run()
            sql_obj = QueryManager()
            sql_obj.save_request(param)
            return JsonResponse({'resp': output})
        except Exception as e:
            logger.info('Exception: {}'.format(e))
            return JsonResponse({'resp': f'Error:[{e}]'}, status=405)


def get_stats(request):
    if request.method == 'GET':
        """
        Here will be sending the most frequent request stats param and no of time it called 
        """
        resp = QueryManager().get_freq_request()
        logger.info('Sent request frequency stats.')
        return JsonResponse({'resp': resp})
