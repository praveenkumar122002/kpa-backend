from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WheelSpecification, BogieCheckSheet
from .serializers import WheelSpecificationSerializer, BogieCheckSheetSerializer

# POST /api/forms/wheel-specifications and GET (with filters)
class WheelSpecificationListCreate(APIView):

    def post(self, request):
        serializer = WheelSpecificationSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response({
                "success": True,
                "message": "Wheel specification submitted successfully.",
                "data": {
                    "formNumber": obj.formNumber,
                    "status": "Saved",
                    "submittedBy": obj.submittedBy,
                    "submittedDate": str(obj.submittedDate)
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        filters = {}
        formNumber = request.GET.get("formNumber")
        submittedBy = request.GET.get("submittedBy")
        submittedDate = request.GET.get("submittedDate")
        if formNumber:
            filters["formNumber"] = formNumber
        if submittedBy:
            filters["submittedBy"] = submittedBy
        if submittedDate:
            filters["submittedDate"] = submittedDate

        qs = WheelSpecification.objects.filter(**filters) if filters else WheelSpecification.objects.all()
        result = []
        for obj in qs:
            result.append({
                "formNumber": obj.formNumber,
                "submittedBy": obj.submittedBy,
                "submittedDate": str(obj.submittedDate),
                "fields": obj.fields
            })
        return Response({
            "success": True,
            "message": "Filtered wheel specification forms fetched successfully.",
            "data": result
        })
        
# POST /api/forms/bogie-checksheet
class BogieCheckSheetCreate(APIView):
    def post(self, request):
        serializer = BogieCheckSheetSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response({
                "success": True,
                "message": "Bogie checksheet submitted successfully.",
                "data": {
                    "formNumber": obj.formNumber,
                    "inspectionBy": obj.inspectionBy,
                    "inspectionDate": str(obj.inspectionDate),
                    "status": "Saved"
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
