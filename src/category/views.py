from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView,CreateView,DetailView,UpdateView
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

class CateagoryDetailView(DetailView):
    model=CategoryForms.Meta.model
    template_name="category/show.html"
    queryset = CategoryForms.Meta.model.objects.all()
    context_object_name = "category"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Category" 
        return context
    
    def get(self, request: HttpRequest, slug=None,*args, **kwargs) -> HttpResponse:
        category = CategoryForms.Meta.model.objects.filter(slug=slug).first()
        if category:
            context = {
                'category':category
            }
            return render(request,self.template_name,context=context)
        messages.error(request,message="No Existe la categoria")
        return redirect(reverse_lazy("category_index"))

class CategoryUpdateView(UpdateView):
    template_name = "category/form.html"
    model=CategoryForms.Meta.model
    form_class=CategoryForms
    queryset=CategoryForms.Meta.model.objects.all()
    