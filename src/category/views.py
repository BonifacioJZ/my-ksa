from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView,CreateView
from .form import CategoryForms
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect,render


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
    success_url = reverse_lazy('category_index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Category" 
        return context
    
    def post(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:
        form = CategoryForms(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request=request,message="La categoria fue creada exitosamente")
            return redirect(self.success_url)
        context = {
            'form':form
        }
        return render(request,self.template_name,context=context)
    