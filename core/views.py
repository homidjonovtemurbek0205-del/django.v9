from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Film
from .forms import FilmForm

class BoshSahifaView(View):
    def get(self, request):
        data = {
            'jami_filmlar_soni': Film.objects.count(),
            'faol_filmlar_soni': Film.objects.filter(faol=True).count(),
            'eng_yuqori_reytingli_5_ta_film': Film.objects.filter(faol=True).order_by('-reyting')[:5],
            'loyiha_nomi': "Onlayn Kinoteatr"
        }
        return render(request, 'index.html', data)

class FilmQoshishView(View):
    def get(self, request):
        form = FilmForm()
        return render(request, 'film_qoshish.html', {'form': form})

    def post(self, request):
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('filmlar_royxati')
        return render(request, 'film_qoshish.html', {'form': form})

class FilmlarRoyxatiView(ListView):
    model = Film
    template_name = 'index.html'
    context_object_name = 'filmlar'
    
    def get_queryset(self):
        return Film.objects.filter(faol=True).order_by('-reyting')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['loyiha_nomi'] = "Barcha filmlar"
        context['empty_message'] = "Hozircha filmlar mavjud emas."
        return context

class JanrBoyichaFilmlarView(ListView):
    model = Film
    template_name = 'index.html'
    context_object_name = 'filmlar'

    def get_queryset(self):
        janr_nomi = self.kwargs.get('janr_nomi')
        return Film.objects.filter(janr__iexact=janr_nomi, faol=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        janr_nomi = self.kwargs.get('janr_nomi')
        context['loyiha_nomi'] = f'"{janr_nomi.capitalize()}" janridagi filmlar'
        context['empty_message'] = "Bu janrda filmlar topilmadi."
        return context

class FilmDetailView(DetailView):
    model = Film
    template_name = 'about.html'
    context_object_name = 'film'
    pk_url_kwarg = 'id'