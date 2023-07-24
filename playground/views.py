from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.functions import Concat
from django.db.models import Value
from django.db.models import Value, F, Func, Count, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection
from tags.models import TaggedItem
from django.db import transaction
from store.models import Product, OrderItem, Order, Customer

# Create your views here.
def say_hello(request):
    collection = Collection()
    collection.title = 'Video Games'
    collection.featured_product = Product(id =1)
    collection.save()

    return render(request, 'hello.html', {'name':'Rishabh'})