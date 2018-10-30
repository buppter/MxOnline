import xadmin
from .models import CourseComments, UserMessage, UserAsk, UserCourse, UserFavorite


class CourseCommentsAdmin(object):
    ist_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments', 'add_time']
    model_icon = 'fa fa-commenting'


class UserMessageAdmin(object):
    ist_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']
    model_icon = 'fa fa-newspaper-o'


class UserCourseAdmin(object):
        ist_display = ['user', 'course', 'add_time']
        search_fields = ['user', 'course']
        list_filter = ['user', 'course', 'add_time']


class UserAskAdmin(object):
    ist_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


class UserFavoriteAdmin(object):
    ist_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)