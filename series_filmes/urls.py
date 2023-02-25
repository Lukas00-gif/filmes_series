"""series_filmes URL Configuration
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from filmes import views
from series import views as series_views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.filmes, name='filmes'),
    path('indicados/', views.indicados, name='indicados'),
    path('melhores2020/', views.melhores2020, name='melhores2020'),
    path('melhores2021/', views.melhores2021, name='melhores2021'),

    path('editar/<int:id>', views.editar_filme, name='editar_filme'),
    path('alterar_filme/<int:id>', views.alterar_filme, name='alterar_filme'),
    
    path('deletar/<int:id>', views.deletar_filme, name='deletar_filme'),

    # urls series
    path('series/', series_views.pag_series , name='series')

    
]
