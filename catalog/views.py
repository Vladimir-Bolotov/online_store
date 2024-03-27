from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product, Contact, Post
from pytils.translit import slugify


class ProductListView(ListView):
    model = Product
    extra_context = {'title': 'Главная'}


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {'title': 'O нас'}

    def get_context_data(self, **kwargs) -> dict[str]:
        context_data = super().get_context_data(**kwargs)
        context_data['object'] = Contact.objects.order_by('pk').reverse()[0]
        return context_data


class ProductDetailView(DetailView):
    model = Product
    extra_context = {'title': 'Информация о товаре'}


class ProductCreateView(CreateView):
    model = Product
    extra_context = {'title': 'Добавить товар'}
    fields = ['name', 'price', 'description', 'image', 'category']
    success_url = reverse_lazy('catalog:home')


class PostCreateView(CreateView):
    model = Post
    extra_context = {'title': 'Добавить запись'}
    fields = ['title', 'content', 'image', 'is_published']
    success_url = reverse_lazy('catalog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()

        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    extra_context = {'title': 'Редактировать запись'}
    fields = ['title', 'content', 'image', 'is_published']
    success_url = reverse_lazy('catalog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:post', args=[self.kwargs.get('pk')])


class PostListView(ListView):
    model = Post
    extra_context = {'title': 'Блог'}

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class PostDetailView(DetailView):
    model = Post
    extra_context = {'title': 'Запись'}

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('catalog:blog')
