from rest_framework import serializers
from home.models import Person, Team
from django.contrib.auth.models import User



class RegisterSerializer(serializers.Serializer):
    
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    
    # this is for ModelSerializer
    # class Meta:
    #     model = User
    #     fields = ['username', 'email', 'password']
    
    def validate(self, data):
        
        if data.get('username'):
            if User.objects.filter(username=data.get('username')).exists():
                raise serializers.ValidationError('Usrname already exists!')

        if data.get('email'):
            if User.objects.filter(email=data.get('email')).exists():
                raise serializers.ValidationError("Email already exists!")

        return data
    
    def create(self, validated_data):
        
        user_obj = User.objects.create(username=validated_data.get('username'), email=validated_data.get('email'))
        user_obj.set_password(validated_data.get('password'))
        user_obj.save()
        
        return validated_data
    

class LoginSerializer(serializers.Serializer):
    
    username = serializers.CharField()
    password = serializers.CharField()
    
    # For ModelSerializer
    # class Meta:
    #     model = User
    #     fields = ['username', 'password']


class TeamSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Team
        fields = ['team_name']


class PersonSerializer(serializers.ModelSerializer):
    
    team = TeamSerializer(read_only=True)
    # Adding Extra serializer field
    team_info = serializers.SerializerMethodField()
    
    class Meta:
        
        model = Person
        fields = '__all__'
        depth = 1
    
    # method to get the extra field - team_info
    def get_team_info(self, obj):
        return 'Extra serializer field'
        
    # Validating the fields from backend.
    def validate(self, data):
        
        special_chars = '!@#$%^&*()-+?_+,<>/'
        
        if any(c in special_chars for c in data.get('name')):
            
            raise serializers.ValidationError("Name should not have special characters")
        
        if data.get('age') < 18:
            
            raise serializers.ValidationError("Age should not be less than 18")

        return data