from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.welcome),
    path("resumepage/", views.Resume, name="resumepage"),
    path("index/", views.index, name="index"),
    path("sign_up/", views.Signup, name="sign_up"),
    path("resumepage/upload_resume/", views.upload_resume, name="upload_resume"),
    path("list_resumes", views.list_resumes, name="list_resumes"),
    path("resume_download", views.list_resumes, name="resume_download"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
