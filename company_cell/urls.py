from django.conf.urls import url
from django.urls import path
from . import views
from company_cell.models import company
from company_cell.views import comp_detail,showCompanies
from django.conf import settings
from django.conf.urls.static import static


app_name='company_cell'
urlpatterns=[

    url(r'^companies$', showCompanies.as_view(), name='showCompanies'),
    # url('applyjob/$',views.applyjob, name='applyjob'),
    url('home/',views.back_home, name='back_home'),
    
    
    path('<slug:pk>/', comp_detail.as_view(), name='comp_detail'),
    path('<slug:comp_id>/<slug:username>/count_stud/',views.count_stud,name='count_stud'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)