from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status 
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer


class MovieListView(APIView):
    def get(self,request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)



class MovieDetailView(APIView):
    def get(self,request,pk):
        try:
            movie = Movie.objects.get(pk=pk)
            
        except Movie.DoesNotExist:
            return Response({'Error': 'Movie not found'},status=status.HTTP_404_NOT_FOUND)
            
            
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    
    def put(self,request):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self,request,pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
 

        