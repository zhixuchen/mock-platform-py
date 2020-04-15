from django.contrib import admin
from mock.models import *
import xadmin
from xadmin.views import BaseAdminView,CommAdminView

from xadmin import views


class ProjectAdmin():
    list_display = ['id', 'project', 'name', 'rule_py']
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('id',)
    # list_editable 设置默认可编辑字段
    list_editable = ['rule_py']
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



class FunctionAdmin():
    list_display = ['id', 'type', 'function_name', 'value_py']
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20
    ordering = ('id',)
    # list_editable 设置默认可编辑字段
    list_editable = ['value_py']
    # 搜索功能及能实现搜索的字段
    search_fields = ('function_name',)
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('function_name',)
    # 过滤器功能及能过滤的字段
    list_filter = ('function_name',)



class MethodAdmin():
    list_display = ['project_id', 'name', 'uri', 'route', 'pragram', 'type', 'result']
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20
    ordering = ('id',)
    # list_editable 设置默认可编辑字段
    list_editable = ['uri', 'result']
    # 搜索功能及能实现搜索的字段
    search_fields = ('name', 'uri')
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('name',)



class CallbackAdmin():
    list_display = ['project_id', 'name', 'request_uri', 'request_body', 'pragram', 'status']
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20
    ordering = ('id',)
    # list_editable 设置默认可编辑字段
    list_editable = ['request_uri', 'request_body']
    # 搜索功能及能实现搜索的字段
    search_fields = ('name', 'request_uri')
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('name',)


class LogAdmin():
    list_display = ['id', 'type', 'method_id', 'name', 'request_url', 'request_body', 'request_method', 'response',
                    'creat_time']
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20
    ordering = ('-id',)
    # 操作项功能显示位置设置，两个都为True则顶部和底部都显示
    actions_on_top = False
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id',)

class GlobalSetting(object):
    site_title="自动化管理后台"
    site_footer="陈治许工作室"

class LoginSetting(object):
    title="自动化管理后台"

xadmin.site.register(views.LoginView,LoginSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)
xadmin.site.register(Project,ProjectAdmin)
xadmin.site.register(Function,FunctionAdmin)
xadmin.site.register(Method,MethodAdmin)
xadmin.site.register(Callback,CallbackAdmin)
xadmin.site.register(Log,LogAdmin)
# xadmin.site.site_header = '自动化管理系统'
# xadmin.site.site_title = '登录系统后台'
# xadmin.site.index_title = '后台管理'
# xadmin.site.site_url = ''
