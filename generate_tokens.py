from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

# Generate tokens for all users
for user in User.objects.all():
    token, created = Token.objects.get_or_create(user=user)
    print(f"Token for {user.username}: {token.key}")