from django.db.models.query import QuerySet
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_paginated_collection(request, collection: QuerySet, count_per_page: int = 9): 
    paginator = Paginator(collection, count_per_page)
    page_number = request.GET.get('page', 1)
    try:
        collection = paginator.page(page_number)
    except PageNotAnInteger:
        collection = paginator.page(1)
    except EmptyPage:
        collection = paginator.page(paginator.num_pages) 
    return collection