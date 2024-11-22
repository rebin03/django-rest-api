from rest_framework import serializers
from home.models import Person, Team


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