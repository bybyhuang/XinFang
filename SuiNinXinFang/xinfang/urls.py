from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^caseList$', views.caseList, name='case'),
    url(r'^caseDetail$',views.getCaseDetail,name='caseDatail')

]