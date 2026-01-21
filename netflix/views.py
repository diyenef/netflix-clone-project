from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .models import Movie

class HomeView(TemplateView):
    template_name = 'netflix/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch some movies for the landing page preview
        context['trending_movies'] = Movie.objects.filter(category='Trending Now')[:5]
        context['new_movies'] = Movie.objects.filter(category='New this week')[:5]
        return context

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'netflix/signup.html'
    success_url = reverse_lazy('browse')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

    def get_initial(self):
        initial = super().get_initial()
        initial['username'] = self.request.GET.get('email', '')
        return initial

class NetflixLoginView(LoginView):
    template_name = 'netflix/login.html'
    
    def get_success_url(self):
        return reverse_lazy('browse')

class NetflixLogoutView(LogoutView):
    next_page = reverse_lazy('home')

class BrowseView(LoginRequiredMixin, TemplateView):
    template_name = 'netflix/browse.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hero_movie'] = Movie.objects.filter(is_hero=True).first()
        
        # Group movies by category
        categories = Movie.objects.values_list('category', flat=True).distinct()
        content_rows = []
        for category in categories:
            content_rows.append({
                'title': category,
                'movies': Movie.objects.filter(category=category)
            })
        context['content_rows'] = content_rows
        return context
