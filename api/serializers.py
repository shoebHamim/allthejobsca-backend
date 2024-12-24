# api/serializers.py
from rest_framework import serializers
from mainapp.models import (
    User, Talent, Employer, JobPosting, JobApplication,Consultant,Consultation,Review,Testimonial,Package,PackageInvoice
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class UserRestrictedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','email','username','role','phone','account_status']
class TalentSerializer(serializers.ModelSerializer):
    user = UserRestrictedSerializer(source='user_id', read_only=True)
    class Meta:
        model = Talent
        fields = '__all__'
class EmployerSerializer(serializers.ModelSerializer):
    user = UserRestrictedSerializer(source='user_id', read_only=True)
    class Meta:
        model = Employer
        fields = '__all__'
class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = '__all__'
class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'

class ConsultantSerializer(serializers.ModelSerializer):
    user = UserRestrictedSerializer(source='user_id', read_only=True)
    class Meta:
        model = Consultant
        fields = '__all__'
class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'
class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'

class PackageInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageInvoice
        fields = '__all__'

