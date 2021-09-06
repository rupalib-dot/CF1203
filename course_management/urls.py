from django.conf.urls import url 
from course_management import views 
 
urlpatterns = [  
    # url(r'^api/users/all_delete$', views.all_user_delete),  
    url(r'^api/dashboard$', views.admin_dashboard), 
    url(r'^api/change/password$', views.change_password), 
    url(r'^api/allot/course$', views.allot_course), 
    url(r'^api/course/allot/completed/(?P<allotid>[0-9]+)$', views.courseAllot_completed),
    url(r'^api/course/allot/list$', views.courseAllot_list),
    url(r'^api/send_email$', views.send_email),
    

    #user apis
    url(r'^api/user/login$', views.user_login), 
    url(r'^api/user/add$', views.add_user),
    url(r'^api/users$', views.user_list),
    url(r'^api/users/detail/(?P<uid>[0-9]+)$', views.user_detail),
    url(r'^api/users/edit/(?P<uid>[0-9]+)$', views.user_edit),
    url(r'^api/user/delete/(?P<uid>[0-9]+)$', views.user_delete),
    url(r'^api/user/change/status/(?P<uid>[0-9]+)$', views.user_changeStatus),


    #caregories apis
    url(r'^api/category/add$', views.add_category),
    url(r'^api/category/list$', views.category_list),
    url(r'^api/category/detail/(?P<catid>[0-9]+)$', views.category_detail), #category id
    url(r'^api/category/edit/(?P<catid>[0-9]+)$', views.category_edit), #category id 
    url(r'^api/category/delete/(?P<catid>[0-9]+)$', views.category_delete), #category id
    url(r'^api/category/change/status/(?P<catid>[0-9]+)$', views.category_changeStatus), #category id


    #course apis
    url(r'^api/course/add$', views.add_course),
    url(r'^api/course/list/(?P<catid>[0-9]+)$', views.course_list), #category id
    url(r'^api/course$', views.all_course),
    url(r'^api/course/detail/(?P<cid>[0-9]+)$', views.course_detail), #course id 
    url(r'^api/course/edit/(?P<cid>[0-9]+)$', views.course_edit), #course id 
    url(r'^api/course/delete/(?P<cid>[0-9]+)$', views.course_delete), #course id
    url(r'^api/course/change/status/(?P<cid>[0-9]+)$', views.course_changeStatus), #course id

    # #course chapter apis
    url(r'^api/chapter/add$', views.add_chapter),
    url(r'^api/chapter/list/(?P<cid>[0-9]+)$', views.chapter_list), #course id
    url(r'^api/chapter$', views.all_chapter),
    url(r'^api/chapter/detail/(?P<chid>[0-9]+)$', views.chapter_detail), #chapter id 
    url(r'^api/chapter/edit/(?P<chid>[0-9]+)$', views.chapter_edit), #chapter id 
    url(r'^api/chapter/delete/(?P<chid>[0-9]+)$', views.chapter_delete), #chapter id
    url(r'^api/chapter/change/status/(?P<chid>[0-9]+)$', views.chapter_changeStatus), #chapter id
 
]