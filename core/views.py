from django.views.generic import TemplateView,ListView, CreateView , UpdateView , DeleteView
from .models import CadastroModels
from .form  import CadastroForm
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = 'index.html'




class IndexList(ListView):
    template_name = 'list.html'
    model = CadastroModels


    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context ['cadastrado'] = CadastroModels.objects.all()
        return context        

class IndexCreat(CreateView):
    template_name = 'create.html'
    model = CadastroModels
    fields = '__all__'
    success_url = reverse_lazy('list')

class IndexUpdate(UpdateView):
    template_name = 'detail.html'
    model = CadastroModels
    fields = '__all__'
    success_url = reverse_lazy('list')

class IndexDelete(DeleteView):
    template_name = 'delete.html'
    model = CadastroModels
    fields = '__all__'
    success_url = reverse_lazy('list')

      