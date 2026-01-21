from django.core.management.base import BaseCommand
from netflix.models import Movie
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Seed movies with local image assets'

    def handle(self, *args, **kwargs):
        # Clear existing movies completely
        self.stdout.write('Hard resetting movie database for local assets...')
        Movie.objects.all().delete()

        # Local static paths
        # Note: In Django, static files are referenced by their relative path in the URL
        # We use /static/images/... in the DB so the browser finds them.
        
        movies = [
            # Hero Movie
            {
                'title': 'Money Heist',
                'description': 'Eight thieves take hostages and lock themselves in the Royal Mint of Spain as a criminal mastermind manipulates the police to carry out his plan.',
                'rating': '8.8/10',
                'view_count': '2B+ Streams',
                'poster': '/static/images/money_heist.jpg',
                'backdrop': '/static/images/money_heist.jpg', # Using same for now
                'logo': 'https://images.weserv.nl/?url=occ-0-2794-2219.1.nflxso.net/dnm/api/v6/LmEnxtiAuzez9jIK9aE68lDh8Bg/AAAABbcO_L4E4_vCq_W_N2YpWn8-Y0S9Yq-o_p_P0P9G9G9G9G9G9G9G9G9G9G9G9G9G9G9G9G9G9G9G9G.png?r=7a6',
                'category': 'Trending Now',
                'is_hero': True
            },
            {
                'title': 'Stranger Things',
                'description': 'When a young boy vanishes, a small town uncovers a mystery.',
                'rating': '8.7/10',
                'view_count': '500M+ Streams',
                'poster': '/static/images/stranger_things.jpg',
                'backdrop': '/static/images/stranger_things.jpg',
                'category': 'Trending Now',
                'is_hero': False
            },
            {
                'title': 'The Irishman',
                'description': 'An old man recalls his time painting houses for his friend Jimmy Hoffa.',
                'rating': '7.8/10',
                'view_count': '60M+ Streams',
                'poster': '/static/images/the_irishman.jpg',
                'backdrop': '/static/images/the_irishman.jpg',
                'category': 'Trending Now',
                'is_hero': False
            },
            {
                'title': 'Extraction 2',
                'description': 'Tyler Rake is back for another high-stakes mission.',
                'rating': '7.0/10',
                'view_count': '120M+ Streams',
                'poster': '/static/images/extraction_2.jpg',
                'backdrop': '/static/images/extraction_2.jpg',
                'category': 'New this week',
                'is_hero': False
            },
            {
                'title': 'The Perfection',
                'description': 'A troubled musical prodigy seeks out her former mentor.',
                'rating': '6.2/10',
                'view_count': '15M+ Streams',
                'poster': '/static/images/the_perfection.jpg',
                'backdrop': '/static/images/the_perfection.jpg',
                'category': 'New this week',
                'is_hero': False
            },
        ]

        for movie_data in movies:
            Movie.objects.create(**movie_data)

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {len(movies)} movies with LOCAL assets'))
