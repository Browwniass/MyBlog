from rest_framework import viewsets
from .serializers import ArticleSerializer, MyTagSerializer
from .models import Article
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ArticleModelView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
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
        elif 'filt_tags' in self.request.query_params:
            tags = self.request.query_params['filt_tags'].split(',')
            return Article.objects.filter(tags__name__in=tags).distinct()
        return Article.objects.all()


class TagsModelView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = MyTagSerializer


class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)