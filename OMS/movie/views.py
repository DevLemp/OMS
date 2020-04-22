from rest_framework import viewsets, mixins, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.forms.models import model_to_dict 
from django_filters.rest_framework import DjangoFilterBackend
from core.models import Movie, User_Movie
from movie import serializers
import datetime
import json



class MovieViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Get a list of movies in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'id']

    def get_queryset(self):
        """Return objects"""
        return self.queryset.order_by('-id')

        
class RentViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """Rent a movie as user"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = User_Movie.objects.exclude(status='available')
    serializer_class = serializers.User_MovieSerializer

    def get_queryset(self):
        """Return objects"""
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        rental = Movie.objects.get(id=self.request.data['movie'])
        serializer.save(user=self.request.user, movie=rental)


class ReturnViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.UpdateModelMixin):
    """Return a rented movie"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = User_Movie.objects.exclude(status='returned')
    serializer_class = serializers.User_MovieSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class PriceViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.UpdateModelMixin):
    """Show the price that the user has to pay for his rentals"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = User_Movie.objects.exclude(status='returned')
    serializer_class = serializers.User_MovieSerializer

    # def get_queryset(self):
    #     # now = timezone.now()
    #     # if (now-obj.data['insert_date']).days == 0:
    #     #     pass
    #     # elif (now-obj.data['insert_date']).days <= 3:
    #     #     obj.data['price'] = (now-obj.data['insert_date']).days
    #     # else:
    #     #     obj.data['price'] = 3 + 0.5*((now-obj.data['insert_date']).days - 3)
    #     return self.queryset.filter(user=self.request.user)


    def list(self, request, *args, **kwargs):
        now = datetime.datetime.now()
        queryset = self.queryset.filter(user=self.request.user)
        serializer = self.get_serializer(queryset, many=True)
        insert_date = datetime.datetime.strptime(list(serializer.data[0].values())[3], "%Y-%m-%dT%H:%M:%S.%fZ")
        movie = User_Movie.objects.get(id=list(serializer.data[0].values())[0])
        if (now-insert_date).days == 0:
            movie.price = 1
        elif (now-insert_date).days <= 3:
            movie.price = (now-insert_date).days
        else:
            movie.price = 3 + 0.5*((now-insert_date).days - 3)
        print((now-insert_date).days)
        #query.insert_date = query.insert_date.replace("T", " ")
        movie.save()
        dict_obj = model_to_dict(movie)
        ser_mov = serializers.User_MovieSerializer(data=dict_obj)
        ser_mov.is_valid()
        return Response(ser_mov.data)
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)
