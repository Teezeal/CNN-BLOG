from django.shortcuts import render
from .models import News
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomePage(ListView):
    model = News
    template_name = 'blog/tech-index.html'
    context_object_name = 'news' 

class DetailPage(DetailView):
    model = News
    template_name = 'blog/tech-single.html'
    context_object_name = 'news'

class CreateNewPage(LoginRequiredMixin,  CreateView):
    model = News
    fields = ['headline', 'content','image', 'reporter']
    template_name = 'blog/make-news.html'
    success_url = '/'

class EditNewsPage(UpdateView):
    model = News
    fields = ['headline', 'content','image', 'reporter']
    template_name = 'blog/update-news.html'
    success_url = '/'

class DeleteNewsPage(LoginRequiredMixin, DeleteView):
    model = News
    template_name = 'blog/delete-news.html'
    success_url = '/'
    


























# function based view
# def get_news(request):
#     news = News.objects.all()

#     context = {
#         'news': news
#     }

#     return render(request, 'blog/tech-index.html', context)

# def details_page(request, id):
#     news = News.objects.get(id=id)

#     context = {
#         'news': news
#     }
        
#     return render(request, 'blog/tech-single.html', context)



# class based view
# class HomePage(ListView):
#     model = News
#     template_name = 'blog/home.html'
#     context_object_name = 'news'


# def contact(request):
#     return render(request, 'blog/tech-contact.html')


