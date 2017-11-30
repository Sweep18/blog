from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.MainPageView.as_view(), name='main'),
    url(r'^news/$', views.NewsPageView.as_view(), name='news_page'),
    url(r'^news/(?P<pk>[0-9]+)/$', views.SingleNewsView.as_view(), name='single_news'),
    url(r'^add/$', views.AddNewsView.as_view(), name='add_news'),
    url(r'^all/$', views.AllUsersView.as_view(), name='all_users'),
    url(r'^(?P<pk>[0-9]+)/$', views.UserBlogView.as_view(), name='user_blog'),
]