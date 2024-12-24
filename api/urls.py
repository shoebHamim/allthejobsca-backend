# api/urls.py
from django.urls import path, include
from . import views

urlpatterns = [

    path('api-token-auth/', views.CustomAuthToken.as_view(), name='api-token-auth'),


    # User URLs
    path('users/', views.SeeUser.as_view(), name='user-list'),
    path('users/<str:email>/update/', views.UpdateUser.as_view(), name='user-update'),
    path('users/create/', views.CreateUser.as_view(), name='user-create'),
    path('users/<str:email>/', views.GetUser.as_view(), name='user-detail'),
    # Talent URLs
   path('talents/', views.SeeTalent.as_view(), name='talent-list'),
    path('talents/user/<int:user_id>/', views.SeeSingleTalentByUserId.as_view(), name='talent-by-userId'),
    path('talents/<int:pk>/update/', views.UpdateTalent.as_view(), name='talent-update'),
    path('talents/create/', views.CreateTalent.as_view(), name='talent-create'),

    # Employer URLs
    path('employers/', views.SeeEmployer.as_view(), name='employer-list'),
    path('employers/user/<int:user_id>/', views.SeeSingleEmployerByUserId.as_view(), name='employer-by-userId'),
    path('employers/<int:pk>/update/', views.UpdateEmployer.as_view(), name='employer-update'),
    path('employers/create/', views.CreateEmployer.as_view(), name='employer-create'),
    # JobPosting URLs
    path('jobs/', views.SeeJobPosting.as_view(), name='job-list'),
    path('jobs/<int:pk>/update/', views.UpdateJobPosting.as_view(), name='job-update'),
    path('jobs/create/', views.CreateJobPosting.as_view(), name='job-create'),

    # JobApplication URLs
    path('applications/', views.SeeJobApplication.as_view(), name='application-list'),
    path('applications/<int:pk>/update/', views.UpdateJobApplication.as_view(), name='application-update'),
    path('applications/create/', views.CreateJobApplication.as_view(), name='application-create'),

    # Consultant URLs
    path('consultants/', views.SeeConsultant.as_view(), name='consultant-list'),
    path('consultants/user/<int:user_id>/', views.SeeSingleConsultantByUserId.as_view(), name='consultant-by-userId'),
    path('consultants/<int:pk>/update/', views.UpdateConsultant.as_view(), name='consultant-update'),
    path('consultants/create/', views.CreateConsultant.as_view(), name='consultant-create'),

    # Consultation URLs
    path('consultations/', views.SeeConsultation.as_view(), name='consultation-list'),
    path('consultations/<int:pk>/update/', views.UpdateConsultation.as_view(), name='consultation-update'),
    path('consultations/create/', views.CreateConsultation.as_view(), name='consultation-create'),

    # Review URLs
    path('reviews/', views.SeeReview.as_view(), name='review-list'),
    path('reviews/<int:pk>/update/', views.UpdateReview.as_view(), name='review-update'),
    path('reviews/create/', views.CreateReview.as_view(), name='review-create'),

    # Testimonial URLs
    path('testimonials/', views.SeeTestimonial.as_view(), name='testimonial-list'),
    path('testimonials/<int:pk>/update/', views.UpdateTestimonial.as_view(), name='testimonial-update'),
    path('testimonials/create/', views.CreateTestimonial.as_view(), name='testimonial-create'),

    # Package URLs
    path('packages/', views.SeePackage.as_view(), name='package-list'),
    path('packages/<int:pk>/update/', views.UpdatePackage.as_view(), name='package-update'),
    path('packages/create/', views.CreatePackage.as_view(), name='package-create'),

    # PackageInvoice URLs
    path('invoices/', views.SeePackageInvoice.as_view(), name='invoice-list'),
    path('invoices/<int:pk>/update/', views.UpdatePackageInvoice.as_view(), name='invoice-update'),
    path('invoices/create/', views.CreatePackageInvoice.as_view(), name='invoice-create'),
]