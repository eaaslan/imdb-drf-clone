from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination



class WatchListPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 2
    last_page_strings = 'end'
    
    
class WatchListPOPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'start'
    