from django.conf.urls import re_path
from django.http import HttpResponseRedirect

from . import views

app_name = 'tasks'
urlpatterns = [
    re_path(r'^$', lambda x: HttpResponseRedirect('choose/')),
    re_path(r'^login-form/$', views.login_form, name='login-form'),
    re_path(r'^login/$', views.tps_login, name='login'),
    re_path(r'^choose/$', views.choose, name='choose'),
    re_path(r'^team/$', views.team, name='team-home'),
    re_path(r'^supervisor/$', views.supervisor, name='supervisor-home'),
    re_path(r'^team/all/$', views.task_all, name='task-all'),
    re_path(r'^team/(?P<team_id>[0-9])/all-tasks/$', views.team_all_tasks, name='team-all-tasks'),
    re_path(r'^team/points/$', views.team_points, name='team-points'),
    re_path(r'^create/(?P<team_id>[0-9])/$', views.supervisor_create, name='task-create'),
    re_path(r'^create/developer/$', views.developer_create, name='task-create-developer'),
    re_path(r'^(?P<task_id>[0-9]+)/comment/$', views.send_comment, name='send-comment'),
    re_path(r'^(?P<task_id>[0-9]+)/(?P<status_id>[0-5])/vote/(?P<button_id>[0-5])/$', views.send_vote, name='send-vote'),
    re_path(r'^(?P<task_id>[0-9]+)/view/$', views.view_task, name='view-task'),
    re_path(r'^(?P<task_id>[0-9]+)/update-mod/(?P<mod>[1-5])/$', views.update_task_mod, name='update-task-mod'),
    re_path(r'^(?P<task_id>[0-9]+)/update/(?P<status_id>[0-5])/$', views.update, name='update'),
    re_path(r'^logout/$', views.leave_site, name='leave'),
    re_path(r'^new-pass/$', views.change_pass, name='change-pass'),
    re_path(r'^view-all-teams/$', views.view_all_teams, name='view-all-teams'),
    #re_path(r'^/developer/profile/$', views.view_developer_profile, name='developer-profile'),
    #re_path(r'^/supervisor/profile/$', views.view_supervisor_profile, name='supervisor-profile'),
    #re_path(r'^/developer/profile/notifications/$', views.view_developer_notifications, name='developer-notifications'),
    #re_path(r'^/developer/courses/$', views.view_developer_courses, name='developer-courses'),
    #re_path(r'^/developer/calendar/$', views.view_developer_calendar, name='developer-calendar'),
    #re_path(r'^/developer/profile/comments/$', views.view_developer_comments, name='developer-comments'),
    #re_path(r'^/developer/profile/grades/$', views.view_developer_grades, name='developer-grades'),

]
