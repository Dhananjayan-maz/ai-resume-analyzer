from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .serializers import RegisterSerializer

from resume.models import Resume
from resume.serializers import ResumeSerializer

@api_view(["POST"])
def register(request):

    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(
            {"message": "User Registered Successfully", "data": serializer.data},
            status=201,
        )

    return Response(serializer.errors, status=400)


@api_view(["POST"])
def login(request):

    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({"access": str(refresh.access_token), "refresh": str(refresh)})

    return Response({"message": "Invalid Credentials"})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def dashboard(request):

    resumes = Resume.objects.filter(
        user=request.user
    ).order_by("-uploaded_at")

    latest_resume = resumes.first()

    return Response({

        "message": f"Welcome back, {request.user.username}",

        "username": request.user.username,

        "total_resumes": resumes.count(),

        "latest_role": (
            latest_resume.predicted_role
            if latest_resume
            else "No Resume Uploaded"
        ),

        "latest_resume": ResumeSerializer(
            latest_resume
        ).data if latest_resume else None

    })


# @api_view(["GET"])
# @permission_classes([IsAuthenticated])
# def dashboard(request):

#     resumes = Resume.objects.filter(user=request.user).order_by("-uploaded_at")

#     latest_role = ""

#     if resumes.exists():
#         latest_role = resumes.first().predicted_role

#     return Response(
#         {
#             "message": f"Welcome {request.user.username}",
#             "username": request.user.username,
#             "total_resumes": resumes.count(),
#             "latest_role": latest_role,
#         }
#     )
