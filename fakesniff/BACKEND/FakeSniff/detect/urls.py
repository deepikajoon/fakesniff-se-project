from django.urls import path
from . import views

urlpatterns=[
    path("", views.landing_page, name="landing_page"),
    path("login/", views.login_page, name="login_page"),
    path("signup/", views.signup_page, name="signup_page"),
    path("newimage/", views.new_image_save, name="new_image_save"),
    path("report/success/", views.report_sent_success, name="report_sent_success"),
    path("feedback/", views.feedback_page, name="feedback_page"),
    path("dashboard/", views.user_dashboard, name="user_dashboard"),
    path("admin_dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("result/", views.result, name="result"),
    path("chatbot/", views.chatbot_page, name="chatbot_page"),
]
