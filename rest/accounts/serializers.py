from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        ModelClass = self.Meta.model
        instance = ModelClass.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            active=validated_data['active'] if 'active' in validated_data else True,
            password=validated_data['password']
        )
        return instance

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)