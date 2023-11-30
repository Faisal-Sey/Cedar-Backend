from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
def login_user(request, *args, **kwargs):
    data = request.data
    username = data.get("username")
    password = data.get("password")

    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse(
            status=400,
            data={
                "status": "failed",
                "message": "Incorrect username or password"
            },
            safe=False
        )

    refresh_token = RefreshToken.for_user(user)

    return JsonResponse(
        status=200,
        data={
            'status': 'success',
            'message': 'Login successful',
            'data': {
                'access_token': str(refresh_token.access_token),
                'refresh_token': str(refresh_token),
                'first_name': user.first_name,
                'last_name': user.last_name
            }
        },
        safe=False
    )
