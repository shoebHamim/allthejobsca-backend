from django.db import models
from datetime import timedelta
from datetime import datetime
# from django.contrib.auth.models import AbstractUser, Group, Permission



# class CustomUser(AbstractUser):
#     USER_TYPES = (
#         ('generalUser', 'GeneralUser'),
#         ('talent', 'Talent'),
#         ('employer', 'Employer'),
#         ('Consultant', 'consultant'),
#         ('admin', 'Admin'),
#     )
#     user_type = models.CharField(max_length=100, choices=USER_TYPES, default='generalUser')

#     groups = models.ManyToManyField(
#         Group,
#         related_name="customuser_groups",  # Avoid clashes with the default User model
#         blank=True,
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name="customuser_permissions",  # Avoid clashes with the default User model
#         blank=True,
#     )


class User(models.Model):
    USER_ROLES = [
        ('talent', 'Talent'),
        ('employer', 'Employer'),
        ('consultant', 'Consultant'),
        ('admin', 'Admin'),
    ]
    ACCOUNT_STATUS = [
        ('unverified', 'Unverified'),
        ('verified', 'Verified'),
        ('blocked', 'Blocked'),
    ]
    user_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, max_length=30)
    username = models.CharField(unique=True, max_length=30)
    phone = models.CharField(max_length=15, blank=True, null=True)
    password_hash = models.CharField(max_length=70)
    role = models.CharField(max_length=20, choices=USER_ROLES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    systemdate = models.DateTimeField(default=datetime.now,blank=True,null=True)
    account_status = models.CharField(
        max_length=15,
        choices=ACCOUNT_STATUS,
        default='unverified'
    )
    def __str__(self):
        return self.email

# ! Talent Models Start
class Talent(models.Model):
    talent_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    headline = models.CharField(max_length=150, blank=True, null=True)
    about = models.CharField(max_length=500, blank=True, null=True)
    education = models.JSONField(blank=True, null=True, default=list)
    certificates_licenses = models.JSONField(blank=True, null=True, default=list)
    skills = models.JSONField(blank=True, default=list)
    experiences = models.JSONField(blank=True, null=True, default=list)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    cover_letter = models.FileField(upload_to='cover_letters/', blank=True, null=True)
    website = models.CharField(max_length=30, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    area = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    open_to_work = models.BooleanField(default=True,blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    dob = models.CharField(max_length=30, blank=True, null=True)
    saved_jobs = models.JSONField( blank=True, default=list)
    current_salary = models.CharField(max_length=20, blank=True, null=True)
    expected_salary = models.CharField(max_length=20, blank=True, null=True)
    credit = models.CharField(max_length=20, default="0",blank=True, null=True)
    block_credit = models.BooleanField(default=False,blank=True, null=True)
    active_package = models.CharField(max_length=20, blank=True, null=True)
    systemdate = models.DateTimeField(default=datetime.now,blank=True,null=True)

    def __str__(self):
        return self.user_id.email

 # ! Talent Models End

# ! Employer Models Start

class Employer(models.Model):
    employer_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50,blank=True, null=True)
    company_website = models.CharField(max_length=50, blank=True, null=True)
    designation = models.CharField(max_length=30,blank=True, null=True)
    department = models.CharField(max_length=30,blank=True, null=True)
    headline = models.CharField(max_length=150,blank=True, null=True)
    about = models.CharField(max_length=500,blank=True, null=True)
    education = models.JSONField(blank=True, null=True, default=list)
    certificates_licenses = models.JSONField(blank=True, null=True, default=list)
    skills = models.JSONField(blank=True, default=list)
    experiences = models.JSONField(blank=True, null=True, default=list)
    website = models.CharField(max_length=30,blank=True, null=True)
    country = models.CharField(max_length=20,blank=True, null=True)
    city = models.CharField(max_length=20,blank=True, null=True)
    area = models.CharField(max_length=20,blank=True, null=True)
    photo = models.FileField(upload_to='employer_photos/', blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    dob = models.CharField(max_length=30, blank=True, null=True)
    saved_jobs = models.JSONField(null=True,blank=True, default=list)
    credit = models.CharField(max_length=30, blank=True, default="0")
    active_package = models.CharField(max_length=30, blank=True, null=True)
    block_credit = models.BooleanField(default=False,blank=True, null=True)
    is_employer_verified = models.BooleanField(default=False,blank=True, null=True)
    systemdate = models.DateTimeField(default=datetime.now,blank=True,null=True)

    def __str__(self):
        return self.user_id.email

# ! Employer Models End

# ! Job Models Start

class JobPosting(models.Model):
    APPLICATION_TYPE_CHOICES = [
    ("easy_apply", "Easy Apply"),
    ("link_apply", "Link Apply"),
]

    JOB_TYPE_CHOICES = [
    ("Contract", "Contract"),
    ("Freelance", "Freelance"),
    ("Full Time", "Full Time"),
    ("Internship", "Internship"),
    ("Part Time", "Part Time"),
]

    EXPERIENCE_LEVEL_CHOICES = [

    ("Fresh", "Fresh"),
    ("Less Than 1 Year", "Less Than 1 Year"),
    ("1 Year", "1 Year"),
    ("2 Years", "2 Years"),
    ("3 Years", "3 Years"),
    ("4 Years", "4 Years"),
    ("5 Years", "5 Years"),
    ("6 Years", "6 Years"),
    ("7 Years", "7 Years"),
    ("8 Years", "8 Years"),
    ("9 Years", "9 Years"),
    ("10 Years", "10 Years"),]

    LOCATION_TYPE_CHOICES = [
    ("remote", "Remote"),
    ("on-site", "On-Site"),
    ("hybrid", "Hybrid"),]

    STATUS_CHOICES = [
    ("Draft", "Draft"),
    ("Published", "Published"),
    ("Archived", "Archived"),]
    job_id = models.BigAutoField(primary_key=True)
    employer_id = models.ForeignKey("Employer",on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    vacancy_count = models.CharField(max_length=30, blank=True, null=True,default="1")
    benefits = models.JSONField(blank=True, null=True,default=list)
    responsibilities = models.JSONField(blank=True, null=True,default=list)
    education_requirements = models.CharField(max_length=100, blank=True, null=True)
    featured = models.BooleanField(default=False)
    language_requirements = models.JSONField(blank=True, null=True,default=list)
    application_type = models.CharField(
        max_length=30, choices=APPLICATION_TYPE_CHOICES, blank=True, null=True,
    )
    application_link = models.CharField(max_length=50, blank=True, null=True)
    application_instruction = models.CharField(max_length=200, blank=True, null=True)
    industry = models.CharField(max_length=30, blank=True, null=True)
    skills_required = models.JSONField(blank=True, null=True,default=list)
    salary_range = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    job_type = models.CharField(
        max_length=20, choices=JOB_TYPE_CHOICES, blank=True, null=True
    )
    experience_level = models.CharField(
        max_length=20, choices=EXPERIENCE_LEVEL_CHOICES, blank=True, null=True
    )
    location_type = models.CharField(
        max_length=20, choices=LOCATION_TYPE_CHOICES, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_open = models.BooleanField(default=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="Draft"
    )
    views = models.PositiveIntegerField(default=0)
    tags = models.JSONField(blank=True, null=True,default=list)
    systemdate = models.DateTimeField(default=datetime.now,blank=True,null=True)

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    APPLICATION_STATUS_CHOICES = [
    ("applied", "Applied"),
    ("short-listed", "Short-Listed"),
    ("interviewing", "Interviewing"),
    ("hired", "Hired"),
    ("expired", "Expired"),
]
    job_application_id = models.BigAutoField(primary_key=True)
    job_id = models.ForeignKey("JobPosting",on_delete=models.DO_NOTHING)
    talent_id = models.ForeignKey("Talent",on_delete=models.DO_NOTHING)
    status = models.CharField(
        max_length=20, choices=APPLICATION_STATUS_CHOICES, default="applied"
    )
    application_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    feedback = models.CharField(max_length=200, blank=True, null=True)
    application_type = models.CharField(max_length=50, blank=True, null=True)
    systemdate = models.DateTimeField(default=datetime.now,blank=True,null=True)

    def __str__(self):
        return f"Application:{self.job_application_id}-{self.talent_id}"

# ! Job Models End


# ! Consultant Models Start
def get_default_availability():
    return {
        "monday": [],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": []
    }

class Consultant(models.Model):
    # # "day":[
    #     {"start": "09:00", "end": "12:00"},
    #     {"start": "13:00", "end": "17:00"}
    # ],

    UTC_CHOICES = [
    (str(i), f"UTC{'+' if i > 0 else ''}{i}" if i != 0 else "UTC")
    for i in range(-12, 13)
]
    consultant_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey("User",on_delete= models.CASCADE)
    headline = models.CharField(max_length=150)
    about = models.CharField(max_length=500, blank=True, null=True)
    services = models.JSONField(blank=True, null=True,default=list)
    hourly_rate = models.CharField(max_length=30, blank=True, null=True,default="0")
    education = models.JSONField(blank=True, null=True)
    certificates_licenses = models.JSONField(blank=True, null=True)
    skills = models.JSONField(blank=True, null=True)
    experiences = models.JSONField(blank=True, null=True)
    website = models.CharField(max_length=30, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    area = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(upload_to="consultants/photos/", blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    dob = models.CharField(max_length=30, blank=True, null=True)
    saved_jobs = models.JSONField(blank=True, null=True)
    credit = models.CharField(max_length=20, blank=True, null=True,default="0")
    active_package = models.CharField(max_length=20, blank=True, null=True)
    block_credit = models.BooleanField(default=False)
    is_consultant_verified = models.BooleanField(default=False)
    availability_status = models.BooleanField(default=True)
    available_days=models.JSONField(blank=True,null=True,default=get_default_availability)
    timezone=models.CharField(
    choices=UTC_CHOICES,
    default='0',max_length=10)
    systemdate = models.DateTimeField(default=datetime.now,blank=True,null=True)

    def is_time_slot_overlapping(self, day, new_slot):
        new_start = datetime.strptime(new_slot['start'], '%H:%M').time()
        new_end = datetime.strptime(new_slot['end'], '%H:%M').time()
        existing_slots = self.available_days[day]
        for slot in existing_slots:
            slot_start = datetime.strptime(slot['start'], '%H:%M').time()
            slot_end = datetime.strptime(slot['end'], '%H:%M').time()
            if (new_start < slot_end and new_end > slot_start):
                return True
        return False
    def add_availability_slot(self, day, start_time, end_time):
        new_slot = {"start": start_time, "end": end_time}
        if self.is_time_slot_overlapping(day, new_slot):
            raise ValueError(f"Time slot overlaps with existing slots on {day}")
        if day not in self.available_days:
            self.available_days[day] = []
        self.available_days[day].append(new_slot)
        self.save()
    def remove_availability_slot(self, day, start_time, end_time):
        if day not in self.available_days:
            raise ValueError(f"No availability slots found for {day}")
        slot_to_remove = {"start": start_time, "end": end_time}
        day_slots = self.available_days[day]
        if slot_to_remove in day_slots:
            self.available_days[day].remove(slot_to_remove)
            self.save()
        else:
            raise ValueError(f"Time slot {start_time}-{end_time} not found for {day}")

    def __str__(self):
        return f"{self.user_id.email}"


class Consultation(models.Model):
    consultation_id = models.BigAutoField(primary_key=True)
    consultant_id = models.ForeignKey("Consultant",on_delete=models.DO_NOTHING)
    user_id = models.ForeignKey("User",on_delete=models.DO_NOTHING)
    topic = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    consultation_date = models.DateField()
    starting_slot_time = models.CharField(max_length=20,blank=True, null=True)
    ending_slot_time = models.CharField(max_length=20, blank=True, null=True)
    duration_minutes = models.IntegerField(blank=True, null=True)
    status = models.CharField(
        max_length=100,
        choices=[
            ('scheduled', 'Scheduled'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled')
        ],
        default='scheduled'
    )
    rating = models.CharField(max_length=20,blank=True, null=True)
    price = models.CharField(max_length=20,blank=True, null=True)
    systemdate = models.DateTimeField(default=datetime.now,blank=True,null=True)

    def __str__(self):
        return f"{self.consultant_id}"
# # ! Consultant Models End

# # ! Review Model
class Review(models.Model):
    review_id = models.BigAutoField(primary_key=True)
    reviewer_id = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name='reviews_given'  # Reviews written by this user
    )
    reviewed_id = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name='reviews_received'  # Reviews about this user
    )
    rating = models.CharField(max_length=10)
    headline = models.CharField(max_length=50)
    comment = models.CharField(max_length=300)
    review_date = models.DateTimeField(auto_now_add=True)
    systemdate = models.DateTimeField(default=datetime.now,blank=True,null=True)

    def __str__(self):
        return self.reviewed_id
class Testimonial(models.Model):
    testimonial_id = models.BigAutoField(primary_key=True)
    user_id = models.UUIDField()
    rating = models.FloatField()
    headline = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    review_date = models.DateTimeField()
    systemdate = models.DateTimeField(default=datetime.now,blank=True,null=True)



# # ! Package Models Start

class Package(models.Model):
    Package_Target_ROLES = [
    ('talent', 'Talent'),
    ('employer', 'Employer'),
    ('consultant', 'Consultant'),
    ('admin', 'Admin'),
    ]
    package_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    duration_days = models.CharField(max_length=50)
    target_role=models.CharField(choices=Package_Target_ROLES,max_length=30)
    features = models.JSONField(blank=True, null=True, default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    systemdate = models.DateTimeField(default=datetime.now,blank=True,null=True)

    def __str__(self):
        return self.name


class PackageInvoice(models.Model):
    STATUS_CHOICES = [
        ('unpaid', 'Unpaid'),
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled'),
    ]
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
    ]
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    package_id = models.ForeignKey('Package', on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(blank=True,null=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    price = models.CharField(max_length=30)
    discount = models.CharField(max_length=30,blank=True,default="0")
    tax = models.CharField(max_length=30,blank=True,default="0")
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    systemdate = models.DateTimeField(default=datetime.now,blank=True,null=True)
    def __str__(self):
        return f"Invoice {self.id} for User {self.user_id}"
    def save(self, *args, **kwargs):
        if not self.expiry_date:
            duration = timedelta(days=self.package_id.duration_days)
            self.expiry_date = self.purchase_date + duration
        super().save(*args, **kwargs)

# ! Package Models End
