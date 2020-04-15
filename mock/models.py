from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField('项目名称', max_length=64)  # 项目名称
    project = models.CharField('项目标识', max_length=200)  # 项目标识
    rule = models.TextField('项目规则_php')  # 项目规则
    rule_py = models.TextField('项目规则_python')  # 项目规则_python

    class Meta:
        verbose_name = 'MOCK项目管理'
        verbose_name_plural = 'MOCK项目管理'

    def __str__(self):
        return self.rule_py


class Function(models.Model):
    function_name = models.CharField('方法名', max_length=64)  # 方法名
    type = models.CharField('mock类型', max_length=200)  # mock类型
    value = models.TextField('方法内容')  # 方法内容php
    value_py = models.TextField('方法内容')  # 方法内容python
    class Meta:
        verbose_name = 'MOCK方法管理'
        verbose_name_plural = 'MOCK方法管理'

    def __str__(self):
        return self.value_py


class Method(models.Model):

    project_id = models.CharField('项目id', max_length=64)  # 项目id
    name = models.CharField('请求描述', max_length=200)  # 请求描述
    uri = models.CharField('请求接口', max_length=200)  # 请求接口
    route = models.CharField('请求路由', max_length=200)  # 请求路由
    type = models.CharField('请求类型', max_length=200)  # 请求类型
    result = models.TextField('mock结果')  # mock结果
    pragram = models.CharField('请求参数', max_length=200)  # 请求参数

    class Meta:
        verbose_name = 'MOCK请求管理'
        verbose_name_plural = 'MOCK请求管理'

    def __str__(self):
        return self.result


class Callback(models.Model):
    project_id = models.CharField('项目id', max_length=64)  # 项目id
    name = models.CharField('回调描述', max_length=200)  # 回调描述
    request_uri = models.CharField('请求接口', max_length=200)  # 请求接口
    request_body = models.TextField('请求BODY')  # 请求BODY
    pragram = models.CharField('可变参数', max_length=200)  # 可变参数
    status = models.CharField('回调状态', max_length=200)  # 回调状态

    class Meta:
        verbose_name = 'MOCK回调管理'
        verbose_name_plural = 'MOCK回调管理'

    def __str__(self):
        return self.name


class Log(models.Model):
    type = models.CharField('mock类型', max_length=64)  # mock类型
    method_id = models.CharField('mock_id', max_length=200)  # mock_id
    name = models.CharField('mock名称', max_length=200)  # mock名称
    request_url = models.CharField('请求URL', max_length=200)  # 请求URL
    request_body = models.TextField('请求BODY')  # 请求BODY
    request_method = models.CharField('HTTP类型', max_length=200)  # HTTP类型
    response = models.TextField('请求响应')  # 请求响应
    creat_time = models.DateField('请求时间', max_length=200)  # 请求时间

    class Meta:
        verbose_name = 'MOCK请求日志'
        verbose_name_plural = 'MOCK请求日志'

    def __str__(self):
        return self.name
