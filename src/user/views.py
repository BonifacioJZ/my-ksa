from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView

# Create your views here.

class UserLoginView(LoginView):
    template_name="user/login.html"
    
class UserLogoutView(LogoutView):
    next_page= reverse_lazy('login')