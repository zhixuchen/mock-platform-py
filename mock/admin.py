from django.contrib import admin
from mock.models import *


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'name', 'rule']
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('id',)
    # list_editable 设置默认可编辑字段
    list_editable = ['rule']
    # 操作项功能显示位置设置，两个都为True则顶部和底部都显示
    actions_on_top = True
    # actions_on_bottom = True
    # 操作项功能显示选中项的数目
    actions_selection_counter = True
    # 字段为空值显示的内容
    empty_value_display = ' -空白- '
    # 过滤器功能及能过滤的字段
    list_filter = ('name',)
    # 搜索功能及能实现搜索的字段
    search_fields = ('name', 'project',)
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('project',)


@admin.register(Function)
class FunctionAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'function_name', 'value']
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20
    ordering = ('id',)
    # list_editable 设置默认可编辑字段
    list_editable = ['value']
    # 搜索功能及能实现搜索的字段
    search_fields = ('function_name',)
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('function_name',)
    # 过滤器功能及能过滤的字段
    list_filter = ('function_name',)


@admin.register(Method)
class MethodAdmin(admin.ModelAdmin):
    list_display = ['project_id', 'name', 'uri', 'route', 'parameter', 'type', 'result']
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20
    ordering = ('id',)
    # list_editable 设置默认可编辑字段
    list_editable = ['uri', 'result']
    # 搜索功能及能实现搜索的字段
    search_fields = ('name', 'uri')
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('name',)


@admin.register(Callback)
class CallbackAdmin(admin.ModelAdmin):
    list_display = ['project_id', 'name', 'request_uri', 'request_body', 'parameter', 'status']
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20
    ordering = ('id',)
    # list_editable 设置默认可编辑字段
    list_editable = ['request_uri', 'request_body']
    # 搜索功能及能实现搜索的字段
    search_fields = ('name', 'request_uri')
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('name',)


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'method_id', 'name', 'request_url', 'request_body', 'request_method', 'response',
                    'creat_time']
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20
    ordering = ('-id',)
    # 操作项功能显示位置设置，两个都为True则顶部和底部都显示
    actions_on_top = False
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id',)


admin.site.site_header = '自动化管理系统'
admin.site.site_title = '登录系统后台'
admin.site.index_title = '后台管理'
admin.site.site_url = ''
