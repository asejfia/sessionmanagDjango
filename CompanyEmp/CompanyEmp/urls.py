from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'CompanyEmp_app.views.login.user_login'),
    url(r'^accounts/login/$', 'CompanyEmp_app.views.login1.user_login1'),

    url(r'^registration/$', 'CompanyEmp_app.views.registration.user_registration', name='registration'),

    url(r'^user_profile/$', 'CompanyEmp_app.views.user_profile.user_profile', name='profile'),

    url(r'^user_profile/logout/$', 'CompanyEmp_app.views.logout.logout_page', name='logout'),

    url(r'^user_profile/user_information/$', 'CompanyEmp_app.views.update_user_info.manage_account', name='modify_user_info'),
    url(r'^user_profile/stores/$', 'CompanyEmp_app.views.stores.stores', name='modify_user_info'),
    url(r'^user_profile/list/$', 'CompanyEmp_app.views.list.list', name='modify_user_info'),
    url(r'^user_profile/regular_list/$', 'CompanyEmp_app.views.regular_list.regular_list'),
    url(r'^user_profile/manager_list/$', 'CompanyEmp_app.views.manager_list.manager_list'),
 

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
