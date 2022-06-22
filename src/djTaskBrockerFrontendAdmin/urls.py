from django.urls import path
from .views import index

urlpatterns = [
    path('', index)
    ,path('dashboard', index)
    ,path('login', index)
    ,path('dashboard/app', index)
    ,path('dashboard/user', index)
    ,path('dashboard/products', index)
    ,path('dashboard/blog', index)
    ,path('dashboard/task', index)
    ,path('dashboard/tasklist', index)
    ,path('dashboard/taskelement', index)
    #,path('add', index)
    #,path('task', index)
    #,path('task/<str:taskIdName>', index)
    #path('admin/', admin.site.urls)
    #,path('', include('djTaskBrocker.urls'))
    #,path('', include('djTaskBrockerFrontendAdmin.urls'))
    #,path('test/', include('reglament_test.urls'))
    #,path('bookingtest/', include('djPullgerReflection.com_booking.urls'))
    #,path('test/', views.index())
]