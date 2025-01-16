# api/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from mainapp.models import User,Talent,Employer,JobPosting,JobApplication,Consultant,Consultation,Review,Testimonial,Package,PackageInvoice
from .serializers import UserSerializer,UserUpdateSerializer,TalentSerializer,EmployerSerializer,JobPostingSerializer,JobApplicationSerializer,ConsultantSerializer,ConsultationSerializer,ReviewSerializer,TestimonialSerializer,PackageSerializer,PackageInvoiceSerializer


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = token.user
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'email': user.email,
            'user_type': getattr(user, 'user_type', 'N/A')
        })


# User Views
class SeeUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'email'
class UpdateUser(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    lookup_field = 'email'
class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class GetUser(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'email'
# Talent Views
class SeeTalent(generics.ListAPIView):
    queryset = Talent.objects.all()
    serializer_class = TalentSerializer
class SeeSingleTalentByUserId(generics.RetrieveAPIView):
    serializer_class = TalentSerializer
    queryset = Talent.objects.all()
    lookup_field = 'user_id'
class UpdateTalent(generics.UpdateAPIView):
    queryset = Talent.objects.all()
    serializer_class = TalentSerializer

class CreateTalent(generics.CreateAPIView):
    queryset = Talent.objects.all()
    serializer_class = TalentSerializer

# Employer Views
class SeeEmployer(generics.ListAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

class SeeSingleEmployerByUserId(generics.RetrieveAPIView):
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()
    lookup_field = 'user_id'

class UpdateEmployer(generics.UpdateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

class CreateEmployer(generics.CreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

# JobPosting Views
class SeeJobPosting(generics.ListAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
class SeeSingleJobPostingById(generics.RetrieveAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
    lookup_field = 'pk'

class UpdateJobPosting(generics.UpdateAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

class CreateJobPosting(generics.CreateAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
class DeleteJobPosting(generics.DestroyAPIView):
    queryset = JobPosting.objects.all()
    lookup_field = 'pk'
    serializer_class = JobPostingSerializer

# JobApplication Views
class SeeJobApplication(generics.ListAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

class SeeSingleJobApplicationById(generics.RetrieveAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    lookup_field = 'pk'

class UpdateJobApplication(generics.UpdateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

class CreateJobApplication(generics.CreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
class DeleteJobApplication(generics.DestroyAPIView):
    queryset = JobApplication.objects.all()
    lookup_field = 'pk'
    serializer_class = JobApplicationSerializer
# Consultant Views
class SeeConsultant(generics.ListAPIView):
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer
class SeeSingleConsultantByUserId(generics.RetrieveAPIView):
    serializer_class = ConsultantSerializer
    queryset = Consultant.objects.all()
    lookup_field = 'user_id'
class UpdateConsultant(generics.UpdateAPIView):
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer

class CreateConsultant(generics.CreateAPIView):
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer

# Consultation Views
class SeeConsultation(generics.ListAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

class UpdateConsultation(generics.UpdateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

class CreateConsultation(generics.CreateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

# Review Views
class SeeReview(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class UpdateReview(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class CreateReview(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Testimonial Views
class SeeTestimonial(generics.ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class UpdateTestimonial(generics.UpdateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class CreateTestimonial(generics.CreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

# Package Views
class SeePackage(generics.ListAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class UpdatePackage(generics.UpdateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class CreatePackage(generics.CreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

# PackageInvoice Views
class SeePackageInvoice(generics.ListAPIView):
    queryset = PackageInvoice.objects.all()
    serializer_class = PackageInvoiceSerializer

class UpdatePackageInvoice(generics.UpdateAPIView):
    queryset = PackageInvoice.objects.all()
    serializer_class = PackageInvoiceSerializer

class CreatePackageInvoice(generics.CreateAPIView):
    queryset = PackageInvoice.objects.all()
    serializer_class = PackageInvoiceSerializer
