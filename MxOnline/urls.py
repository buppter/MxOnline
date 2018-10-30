"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.urls import path
import xadmin
from django.conf.urls import include
from django.conf.urls import url
from django.views.static import serve

from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwView, LogoutView,\
    IndexView
from MxOnline.settings import MEDIA_ROOT
from users import views

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(), name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('captcha/', include('captcha.urls')),
    path('forget/', ForgetPwdView.as_view(), name="forget_pwd"),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    path('modify_pwd/', ModifyPwView.as_view(), name="modify_pwd"),

    # 配置上传文件文件访问函数
    url(r'^media/(?P<path>.*)/$', serve, {"document_root": MEDIA_ROOT}),
    # 配置上传文件文件访问函数
    # url(r'^static/(?P<path>.*)/$', serve, {"document_root": STATIC_ROOT}),

    # 课程机构URL
    path("org/", include('organization.urls', namespace='org')),

    # 课程相关URL
    path("course/", include('courses.urls', namespace='course')),

    # 用户相关URL
    path("users/", include('users.urls', namespace='users')),

    # 富文本相关URL
    url(r'^ueditor/', include('DjangoUeditor.urls')),


]

# 全局404配置
handler404 = views.page_not_found

# 全局500配置
handler500 = views.page_error

