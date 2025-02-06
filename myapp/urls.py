from django.urls import path
from . import views

urlpatterns = [
    path('admin', views.admin_template, name='admin_template'),
    path('', views.user_setting_template, name='user_setting_template'),
    path('home', views.index_template, name='index_template'),
    path('betting', views.betting_template, name='betting_template'),
    path('confirm_before', views.confirm_before_template, name='confirm_before_template'),
    path('confirm_after', views.confirm_after_template, name='confirm_after_template'),
    path('odds', views.odds_template, name='odds_template'),
]