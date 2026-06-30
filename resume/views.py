from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ResumeSerializer
from .utils.pdf_extractor import extract_text_from_pdf
from .utils.predict_role import predict_role
from .models import *
from .ai.gemini import analyze_resume

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def upload_resume(request):

    serializer = ResumeSerializer(data=request.data)

    if serializer.is_valid():

        resume = serializer.save(user=request.user)

        extracted_text = extract_text_from_pdf(resume.resume.path)

        predicted_role = predict_role(extracted_text)

        resume.extracted_text = extracted_text
        resume.predicted_role = predicted_role
        feedback = analyze_resume(
            resume.extracted_text,
            resume.predicted_role
        )
        
        resume.gemini_feedback = feedback


        resume.save()

        return Response({
            "message": "Resume Uploaded Successfully",
            "predicted_role": predicted_role,
            "data": ResumeSerializer(resume).data
        }, status=201)

    return Response(serializer.errors, status=400)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def resume_history(request):

    resumes = Resume.objects.filter(user=request.user).order_by("-uploaded_at")

    serializer = ResumeSerializer(resumes, many=True)

    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def resume_detail(request, id):

    try:

        resume = Resume.objects.get(
            id=id,
            user=request.user
        )

    except Resume.DoesNotExist:

        return Response(
            {"error": "Resume not found"},
            status=404
        )

    serializer = ResumeSerializer(resume)

    return Response(serializer.data)