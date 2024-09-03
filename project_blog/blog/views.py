from rest_framework import viewsets
from .serializers import ArticleSerializer
from .models import Article


class ArticleModelView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        print(self.request.query_params)
        if 'filt_date' in self.request.query_params:
            order = self.request.query_params['filt_date']
            if order == "newest":
                return Article.objects.all().order_by('-created_at')
            elif order == "oldest":
                return Article.objects.all().order_by('created_at')
        elif 'filt_start_date' in self.request.query_params and \
             'filt_end_date' in self.request.query_params:
            start_date = self.request.query_params['filt_start_date']
            end_date = self.request.query_params['filt_end_date']
            return Article.objects.filter(created_at__range=[start_date, end_date])
        return Article.objects.all()
