from django.contrib import admin
from django.urls import path, include
from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculaEstudante, ListaMatriculaCurso
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()

router.register('estudantes', EstudanteViewSet, 'Estudantes')
router.register('cursos', CursoViewSet, 'Cursos')
router.register('matriculas', MatriculaViewSet, 'Matriculas')

schema_view = get_schema_view(
   openapi.Info(
      title="Documentaçãod da API",
      default_version='v1',
      description="Documentação da API escola",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas', ListaMatriculaEstudante.as_view()),
    path('cursos/<int:pk>/matriculas', ListaMatriculaCurso.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
