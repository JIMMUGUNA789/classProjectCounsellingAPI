from rest_framework import serializers
from .models import Client, Counsellor

#Client Serializer
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'username', 'email', 'phone_number', 'profile_pic')

#client registration serializer
class RegisterClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'username', 'email', 'password', 'phone_number','profile_pic')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        client = Client.objects.create_user(
         validated_data['username'],
         validated_data['email'], 
         validated_data['password'], 
         phone_number=validated_data['phone_number'],
         profile_pic=validated_data['profile_pic'])
        return client
#counsellor seriallizer
class CounsellorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counsellor
        fields = ('id', 'username', 'email', 'phone_number','profile_pic')

class RegisterCounsellorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counsellor
        fields = ('id', 'username', 'email', 'password', 'phone_number', 'profile_pic')
        extra_kwargs = {'password':{'write_only':True}}

    
    def create(self, validated_data):
         counsellor = Counsellor.objects.create_user(
         validated_data['username'],
         validated_data['email'], 
         validated_data['password'], 
         phone_number=validated_data['phone_number'],
         profile_pic=validated_data['profile_pic'])
         return counsellor


class ChangePasswordSerializer(serializers.Serializer):
    model = Client

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ChangeCounsellorPasswordSerializer(serializers.Serializer):
    model = Counsellor
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    