from django.views import generic
from .models import Book
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login 
from django.views.generic import View 
from .forms import UserForm


app_name = 'book'

class IndexView(generic.ListView):
    template_name = 'books/index.html'
 
 
    def get_queryset(self):
        return Book.objects.all()
 
class BookCreate(CreateView):
    model = Book
    fields = ['name', 'author', 'price', 'type']

class BookUpdate(UpdateView):
    model = Book
    fields = ['name', 'author', 'price', 'type']


class BookDelete(DeleteView):
    model = Book

    success_url = reverse_lazy('books:index')


class DetailView(generic.DetailView):
    model = Book

    template_name = 'books/detail.html'

class UserFormView(View):
	form_class = UserForm
	template_name = 'books/registration.html'


	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user = authenticate(username=username, password=password)

			if user is not None:

				if user.is_active:
					login(request, user)
					return redirect('books:index')

		return render(request, self.template_name, {'form': form})































