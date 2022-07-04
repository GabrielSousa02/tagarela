from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken

from .serializer import CustomUserSerializer
from .models import CustomUser


@api_view(["POST"])
def login_user(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data["user"]
    _, token = AuthToken.objects.create(user)

    return Response(
        {
            "user_info": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            },
            "token": token,
        },
        status=200,
    )


@api_view(["POST"])
def signup_user(request):
    serializer = CustomUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    new_user = serializer.save()
    _, token = AuthToken.objects.create(new_user)

    return Response(
        {
            "user_info": {
                "id": new_user.id,
                "username": new_user.username,
                "email": new_user.email,
            },
            "token": token,
        },
        status=201,
    )


@api_view(["GET"])
def detail_user(request):
    current_user = request.user
    currently_following = [user.username for user in current_user.following.all()]
    current_followers = [
        user.username for user in CustomUser.objects.filter(following=current_user.id)
    ]

    if current_user.is_authenticated:
        user_detailed_info = {
            "username": current_user.username,
            "first_name": current_user.first_name,
            "last_name": current_user.last_name,
            "email": current_user.email,
            "following": {
                "total": len(currently_following),
                "users": currently_following,
            },
            "followers": {"total": len(current_followers), "users": current_followers},
        }

        return Response({"user_info": user_detailed_info}, status=200)

    else:
        return Response(
            {"error": "You need to be authenticated to see this information!"},
            status=400,
        )


@api_view(["GET"])
def list_users(request):
    current_user = request.user

    if current_user.is_authenticated:
        raw_users_list = CustomUser.objects.exclude(username=current_user.username)
        currently_following = current_user.following.all()

        final_users_list = []
        for user in list(raw_users_list):
            if current_user.is_following(user, currently_following):
                final_users_list.append(
                    {
                        "username": user.username,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "status": "following",
                    }
                )
            else:
                final_users_list.append(
                    {
                        "username": user.username,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "status": "",
                    }
                )

        return Response({"users": final_users_list}, status=200)

    else:
        return Response(
            {"error": "Sorry, you must be logged in to see this information."},
            status=400,
        )


@api_view(["PATCH"])
def follow_user(request):
    current_user = request.user

    if current_user.is_authenticated:
        success, result = current_user.follow_user(request.data["username"])

        if success:
            return Response({"message": f"You followed {result.username}"})
        else:
            return Response(
                {"error": "Sorry! We could not find that user!"}, status=400
            )


@api_view(["PATCH"])
def unfollow_user(request):
    current_user = request.user

    if current_user.is_authenticated:
        success, result = current_user.unfollow_user(request.data["username"])

        if success:
            return Response({"message": f"You unfollowed {result.username}"})
        else:
            return Response(
                {"error": "Sorry! We could not find that user!"}, status=400
            )
