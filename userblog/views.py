from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.urls import reverse

from .models import News, CommentNews
from .forms import NewsForm, CommentForm


# Логин
class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'userblog/login.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super(LoginView, self).form_valid(form)


# Регистрация
class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = 'userblog/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)


# Главная страница
class MainPageView(LoginRequiredMixin, ListView):
    context_object_name = 'main'
    template_name = 'userblog/main_page.html'
    model = News

    def get_queryset(self):
        return News.objects.filter(user=self.request.user)


# Добавить новость
class AddNewsView(LoginRequiredMixin, FormView):
    form_class = NewsForm
    template_name = 'userblog/add_news.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        news = form.save(commit=False)
        news.user = self.request.user
        news.save()
        return super(AddNewsView, self).form_valid(form)


# Одна новость
class SingleNewsView(LoginRequiredMixin, FormView):
    template_name = 'userblog/single_news.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(SingleNewsView, self).get_context_data(**kwargs)
        context['news'] = News.objects.get(id=self.kwargs['pk'])
        context['comments'] = CommentNews.objects.filter(news=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.news = News.objects.get(id=self.kwargs['pk'])
        comment.save()
        return super(SingleNewsView, self).form_valid(form)

    def get_success_url(self):
        return reverse('single_news', kwargs={'pk': self.kwargs['pk']})


# Все блоги
class AllUsersView(LoginRequiredMixin, ListView):
    context_object_name = 'users'
    template_name = 'userblog/all_users.html'
    model = User

    def get_queryset(self):
        return User.objects.all().exclude(id=self.request.user.id)


# Блог пользователя
class UserBlogView(LoginRequiredMixin, ListView):
    context_object_name = 'blogs'
    template_name = 'userblog/user_blog.html'
    model = News

    def get_queryset(self):
        return News.objects.filter(user=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(UserBlogView, self).get_context_data(**kwargs)
        context['user'] = User.objects.get(id=self.kwargs['pk'])
        return context


# Все новости
class NewsPageView(LoginRequiredMixin, ListView):
    context_object_name = 'news'
    template_name = 'userblog/news.html'
    model = News
