from django.urls import path
from .views import HomePage, DetailPage, CreateNewPage, EditNewsPage, DeleteNewsPage

urlpatterns = [
    path('<slug:slug>/', DetailPage.as_view(), name='details'),
    path('<slug:slug>/delete/', DeleteNewsPage.as_view(), name='delete'),
    path ('<slug:slug>/edit/', EditNewsPage.as_view(), name='edit'),
    path ('create/', CreateNewPage.as_view(), name='create'),
    path('', HomePage.as_view(), name='home'),
    
    
    
]