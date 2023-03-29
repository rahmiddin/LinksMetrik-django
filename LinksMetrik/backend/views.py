from django.http import JsonResponse
from rest_framework.views import APIView
from .utils import domain_finder
from .redis_connect import redis_instance
from .serializers import DomainSerializer

# Create your views here.


class UploadLinks(APIView):
    """class for upload links"""

    def post(self, request):
        try:
            request.data['links'][0]
        except IndexError:
            return JsonResponse({'status': 'Нет адресов!'})
        except KeyError:
            return JsonResponse({'status': 'Нет необходимых данных'})
        else:
            urls = set(list(request.data.values())[0])
            for item in urls:
                if ',' in item:
                    new_item = item.split(',')
                    urls.remove(item)
                    urls += new_item
            domain_list = ','.join(domain_finder(list(urls)))
            time_now = redis_instance.time()[0]
            redis_instance.set(time_now, domain_list)
            return JsonResponse({'status': 'ok'})


class DomainsView(APIView):
    """Views for get a domain"""
    def get(self, request):
        domains = []
        cursor = '0'
        while cursor != 0:
            cursor, keys = redis_instance.scan(cursor=cursor)
            if len(keys) == 0:
                return JsonResponse({'status': 'Нет данных о ваших действиях'})
            values = redis_instance.mget(*keys)
            for item in values:
                domains.append(item.split(','))
            data_for_serializer = {'domains': domains[-1], 'status': 'OK'}
        result = DomainSerializer(data_for_serializer).data
        return JsonResponse(result)

