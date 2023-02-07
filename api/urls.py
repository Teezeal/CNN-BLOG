from django.urls import path 
from .views import api_list_page, Api_list_page, api_detail_page, Api_detail_page, api_create_page, api_update_page, Api_create_page

urlpatterns = [
    path("home/", api_list_page, name="api_home"),
    path("class/home/", Api_list_page.as_view(), name="api_class_home"),
    path("detail/<slug:slug>/", api_detail_page, name="api_detail"),
    path("class/detail/<slug:slug>/", Api_detail_page.as_view(), name="api_class_detail"),
    path("create/", api_create_page, name="api_create"),
    path("class/create/", Api_create_page.as_view(), name="api_create"),
    path("<slug:slug>/update/", api_update_page, name="update"),
]