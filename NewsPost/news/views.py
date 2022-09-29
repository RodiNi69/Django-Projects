from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import Create_news
from django.urls import reverse_lazy


class NewsList(ListView):
    model = Post
    ordering = '-post_date'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class NewsFilter(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'
    ordering = '-post_date'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class Delete_news(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('post_list')


class Create_n(CreateView):
    form_class = Create_news
    model = Post
    template_name = 'create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.method == 'POST':
            post_path = self.request.META['PATH_INFO']
            if post_path == '/news/create/':
                post.post_type = 'Новость'
            elif post_path == '/articles/create/':
                post.post_type = 'Статья'

            return super().form_valid(form)


class Create_edit(UpdateView):
    form_class = Create_news
    model = Post
    template_name = 'edit.html'
