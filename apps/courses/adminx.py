import xadmin
from .models import Course, Lesson, Video, CourseResource, BannerCourse
from organization.models import CourseOrg

class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                    'add_time', 'get_zj_nums', 'go_to']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                   'add_time']
    ordering = ['-click_nums']
    readonly_fields = ['click_nums', 'fav_nums']
    list_editable = ['desc', 'degree']
    exclude = ['students']
    style_fields = {"detail": "ueditor"}
    inlines = [LessonInline, CourseResourceInline]
    refresh_times = [3, 5]
    # import_excel = True

    def queryset(self):
        # 重载queryset方法，来过滤出我们想要的数据的
        qs = super(CourseAdmin, self).queryset()
        # 只显示is_banner=True的课程
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):
        # 保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()

    # def post(self, request, *args, **kwargs):
    #     if 'excel' in request.FILES:
    #         # upload_redcord = UploadRecord()
    #         # upload_redcord.user = request.user
    #         # upload_redcord.file_name = request.FILES['excel'].name
    #         # upload_redcord.upload_type = "detection"
    #         # upload_redcord.save()
    #         # upload_redcord.upload_file.save(request.FILES['excel'].name, request.FILES['excel'])
    #         # try:
    #         #     pici_num = request.FILES['excel'].name.split(".")[0].split("_")[1]
    #         #     if len(pici_num) != 10 or not pici_num.startswith(u"ZL"):
    #         #         upload_redcord.process = u"文件名出错"
    #         #         upload_redcord.message = u"文件名错误, 正确的文件名格式为：检测数据_ZL20160806"
    #         #         upload_redcord.save()
    #         #     else:
    #         #         upload_redcord.pici_num = pici_num
    #         #         upload_redcord.save()
    #         #
    #         #         arc_download = ArchiveDownload()
    #         #         arc_download.user = request.user
    #         #         arc_download.task_type = 1
    #         #         arc_download.pici_num = pici_num
    #         #         arc_download.save()
    #         #
    #         # except Exception as e:
    #         #     upload_redcord.process = u"文件名出错"
    #         #     upload_redcord.message = u"文件名错误, 正确的文件名格式为：ZL20160806"
    #         #     upload_redcord.save()
    #
    #         pass
    #     return super(CourseAdmin, self).post(request, args, kwargs)


class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                    'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                   'add_time']
    ordering = ['-click_nums']
    readonly_fields = ['click_nums', 'fav_nums' ]
    exclude = ['students']
    inlines = [LessonInline, CourseResourceInline]

    def queryset(self):
        # 重载queryset方法，来过滤出我们想要的数据的
        qs = super(BannerCourseAdmin, self).queryset()
        # 只显示is_banner=True的课程
        qs = qs.filter(is_banner=True)
        return qs


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson__name', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'download', 'name', 'add_time']
    search_fields = ['course', 'download', 'name']
    list_filter = ['course__name', 'download', 'name', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
