from django.views.generic import ListView,CreateView
from .form import CategoryForms


class CategoryListView(ListView):
    template_name="category/index.html"
    model = CategoryForms.Meta.model
    context_object_name='category_list'
    queryset = CategoryForms.Meta.model.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Categorias' 
        return context

class CategoryCreateView(CreateView):
    template_name = "category/form.html"
    model= CategoryForms.Meta.model
    form_class = CategoryForms
    queryset = CategoryForms.Meta.model.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Category" 
        return context
    