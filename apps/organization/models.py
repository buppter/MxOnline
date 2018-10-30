from datetime import datetime

from django.db import models


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name="城市名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    dsc = models.CharField(max_length=200, verbose_name="描述")

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name="机构名称")
    desc = models.TextField(verbose_name="机构描述")
    category = models.CharField(default='pxjg', max_length=40, choices=(('pxjg', '培训机构'), ('gx', '高校'), ('gr', '个人')),
                                verbose_name="机构类别")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    students = models.IntegerField(default=0, verbose_name="学习数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="logo", blank=True,)
    address = models.CharField(max_length=150, verbose_name="机构地址")
    course_nums = models.CharField(default=0, max_length=100, verbose_name="课程数量")
    type = models.CharField(max_length=10, verbose_name='机构标签', default='全国知名')
    city = models.ForeignKey(CityDict, on_delete=models.CASCADE, verbose_name="所在城市")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    # 获取机构教师数量
    def get_teacher_nums(self):
        return self.teacher_set.all().count()


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="所属机构")
    name = models.CharField(max_length=50, verbose_name="教师名")
    age = models.IntegerField(default=20, verbose_name='教师年龄')
    work_years = models.IntegerField(default=0, verbose_name="工作年限")
    work_company = models.CharField(max_length=50, verbose_name="就职公司")
    work_position = models.CharField(max_length=50, verbose_name="公司职位")
    points = models.CharField(max_length=50, verbose_name="教学特点")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    image = models.ImageField(upload_to="teacher/%Y/%m", verbose_name="教师封面", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_teacher_course_nums(self):
        return self.course_set.all().count()
