"""crickinfo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from django.http import HttpResponse
from api.views import UserAuthAPIView, UserProfileAPIView, HomeAPIView,TaskAPIView,FieldTeamView, PromotionTeamView, UserStatisticAPIView, TeamUsersView
from rest_framework_swagger.views import get_swagger_view
from django.urls import re_path as url
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'field-team',FieldTeamView)
router.register(r'promotion-team',PromotionTeamView)
router.register(r'user-team',TeamUsersView)

schema_view = get_swagger_view(title='PromoterPlus API')

urlpatterns = [
    path(r'',include(router.urls)),
    url('^$', HomeAPIView.as_view()),
    path('admin/', admin.site.urls),
    path('user-auth/', UserAuthAPIView.as_view()),
    path("user-profile/", UserProfileAPIView.as_view()),
    re_path('user-profile/(?P<email>.+)/$',UserProfileAPIView.as_view()),
    re_path('user-statistic/(?P<email>.+)/$',UserStatisticAPIView.as_view()),
    path('user-team/<int:user_id>',TeamUsersView.as_view({'get': 'list'})),
    re_path("task/(?P<task_id>.+)/$",TaskAPIView.as_view()),
    path('task/',TaskAPIView.as_view()),
    path('accounts/',include('allauth.urls')),
]
