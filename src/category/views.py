from django.views.generic import ListView
from .models import Category
class CategoryListView(ListView):
    template_name="category/index.html"
    model = Category