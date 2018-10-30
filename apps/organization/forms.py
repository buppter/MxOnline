import re

from django import forms
from operation.models import UserAsk


class UserAskForm(forms.ModelForm):
    # 用户客户课程学习咨询

    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        '''
        验证手机号码是否合法
        :return:
        '''
        mobile = self.cleaned_data['mobile']
        Regex_mobile = "^((13[0-9])|(14[5,7])|(15[0-3,5-9])|(17[0,3,5-8])|(18[0-9])|166|198|199|(147))\\d{8}$"
        p = re.compile(Regex_mobile)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError("手机号码非法", code='mobile_invalid')
