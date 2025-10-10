from django.http import JsonResponse
from .models import Job

def jobs_list(request):
    jobs = Job.objects.all().values('title', 'description', 'company', 'location')
    jobs_list = list(jobs)
    return JsonResponse(jobs_list, safe=False)