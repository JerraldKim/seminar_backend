from django.urls import path
from .views import new_test, calculator_add, add_post_json, simple_object_json, list_json, get_with_time, order_echo, variable_key_json

urlpatterns = [
    path('test/', new_test),
    path('add/', calculator_add),
    path('add_post_json/', add_post_json),
    path('simple_object_json/', simple_object_json), 
    path('list_json/', list_json),
    path('get_with_time/', get_with_time),
    path('order_echo/', order_echo), 
    path('variable_key_json/', variable_key_json)
]
