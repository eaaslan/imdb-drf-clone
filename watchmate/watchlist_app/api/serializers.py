from rest_framework import serializers
from watchlist_app.models import StreamPlatform,WatchList,Review
 
 # we use self paramter only inside of class

# def name_lenght(value):
#     if len(value) <2:
#         raise serializers.ValidationError( 'Name is too short')
#     else :
#         return value
    
class ReviewSerializer(serializers.ModelSerializer):   
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        exclude = ('watchlist',)


class WatchListSerializer(serializers.ModelSerializer):
   reviews = ReviewSerializer(many=True,read_only=True)
   class Meta:
        model = WatchList
        fields = '__all__'    
        


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True,read_only=True)
    class Meta :
        model = StreamPlatform
        fields = '__all__'    
        
        
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(validators=[name_lenght])
    # description = serializers.CharField()
    # active = serializers.BooleanField()
    
    # def create(self, validated_data):
    #     return Movie.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #    instance.name = validated_data.get('name',instance.name)
    #    instance.description = validated_data.get('description',instance.description)
    #    instance.active = validated_data.get('active',instance.active)
    #    instance.save()
    #    return instance
       
    # def delete(self, instance):
    #     instance.delete()
        
        
    # def validate(self,data):
    #       if data['title']==data['storyline']:
    #           raise serializers.ValidationError('Name and description can not be same')
    #       else :
    #           return data
        
    
    # def validate_title(self,value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name is too short')
    #     else :
    #         return value