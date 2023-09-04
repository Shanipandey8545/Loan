from  django.urls import path,include
from .import views


urlpatterns = [
    path("",views.index ,name="index"),
    path("aboutus/",views.aboutus,name="aboutus"),
    path("blog/",views.blog,name="blog"),
    path("contactus/",views.contactus,name="contactus"),
    path("loan/",views.loan,name="loan"),
    path("applynow/",views.applynow,name="applynow"),
    path("homeloan/",views.homeloan,name="homeloan"),
    path("personalloan/",views.personalloan,name="personalloan"),
    path("buisnessloan/",views.buisnessloan,name="buisnessloan"),
    path("user_home/",views.user_home,name="user_home"),
    path("user_login/",views.user_login,name="user_login"),
    path("user_reg/",views.user_reg,name="user_reg"),
    path("logout/",views.logout,name="logout"),





]