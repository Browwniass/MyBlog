from rest_framework import viewsets
from .serializers import ArticleSerializer
from .models import Article


class ArticleModelView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
#       if 'filt_tags' in self.request.query_params:


#        print(self)
        return Article.objects.all()
