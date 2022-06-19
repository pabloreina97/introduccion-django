from django.views.generic import View
from django.shortcuts import render

class HomeView(View):
    def get(self, request, *args, **kwargs):  # La función get es por ejemplo cuando refrescas la página
        context = {

        }
        return render(request, 'index.html', context)