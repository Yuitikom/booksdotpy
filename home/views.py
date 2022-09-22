from django.shortcuts import render
from django.urls import reverse_lazy
from .models import PDF
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index(request):
    return render(request, 'home/index.html')


def searchquery(request):
    context = {}
    pdfs = PDF.objects.all()
    if request.method == 'GET':
        query = request.GET.get('query')
        queryset = pdfs.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query)
             ).order_by('-id')
        page = request.GET.get('page')
        paginator = Paginator(queryset, 4)
        try:
            pdfs = paginator.page(page)
        except PageNotAnInteger:
            pdfs = paginator.page(1)
        except EmptyPage:
            pdfs = paginator.page(paginator.num_pages)
        total = queryset.count()
        context.update({
            'total': total,
            'query': query,
            'pdfs': pdfs,
        })

        if query == "":
            return render(request, 'home/searchpage.html')

        return render(request, 'home/searchpage.html', context)


class UploadBook(LoginRequiredMixin, CreateView):
    model = PDF
    template_name = 'home/createbookpage.html'
    fields = ('title', 'image', 'author', 'pdf',)


class EditBook(LoginRequiredMixin, UpdateView):
    model = PDF
    template_name = 'home/editbookpage.html'
    fields = ('title', 'image', 'author', 'pdf',)


class DeleteBook(LoginRequiredMixin, DeleteView):
    model = PDF
    template_name = 'home/deletebookpage.html'
    success_url = reverse_lazy('home')
