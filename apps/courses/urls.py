# -*- coding: utf-8 -*-
_Author_ = 'BUPPT'

from django.conf.urls import url

from .views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddCommentsView, VideoPlay


app_name = "courses"
urlpatterns = [
    # 课程列表url
    url(r'^list/$', CourseListView.as_view(), name='courses_list'),

    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="courses_detail"),

    # 课程视频页
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="courses_video"),

    # 课程评论页
    url(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name="courses_comment"),

    # 课程添加评论页
    url(r'^add_comment/$', AddCommentsView.as_view(), name="add_comment"),

    # 课程视频播放
    url(r'^video/(?P<video_id>\d+)/$', VideoPlay.as_view(), name="video_play"),


]