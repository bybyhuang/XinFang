import null as null
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .models import Case
from django.forms.models import model_to_dict
from django.core.paginator import Paginator

@csrf_exempt
def caseList(request):

    pageNo,pageSize = checkPageParam(request)
    # 只查询某个人,某个状态
    stateId = checkParamInt(request.GET.get('stateId'))
    leaderId = checkParamInt(request.GET.get('leaderId'))

    if stateId != 0 and leaderId != 0:
        # 分页
        caseList = Case.objects.all().filter(state_id=stateId,belongUserId=leaderId)[(pageNo - 1) * pageSize:pageSize]
    elif  stateId == 0 and leaderId != 0:
        caseList = Case.objects.all().filter(belongUserId=leaderId)[(pageNo - 1) * pageSize:pageSize]
    elif leaderId == 0 and stateId != 0:
        caseList = Case.objects.all().filter(state_id=stateId)[(pageNo - 1) * pageSize:pageSize]
    else:
        caseList = Case.objects.all()[(pageNo - 1) * pageSize:pageSize]

    value  = caseList.values("id","reportName","state_id")
    currentList = list(value)
    print(currentList)

    try:
        return JsonResponse({"res": {"list":currentList,"pageNo":pageNo,"pageSize":pageSize}, "state": 200,})
    except:
        return JsonResponse({"res": "fail", "state":400})



def checkPageParam(request):
    pageSize = request.GET.get('pageSize')
    if pageSize == None:
        pageSize = 20

    pageNo = request.GET.get('pageNo')
    if pageNo == None:
        pageNo = 1

    return int(pageNo),int(pageSize)

def getCaseDetail(request):
    # 获取case的详情
    try:
        caseId = checkParamInt(request.GET.get('id'))
        object = Case.objects.get(id=caseId)

        dictValue = model_to_dict(object)
        print(dictValue)
        return JsonResponse({"res": dictValue, "state": 200})
    except:
        return JsonResponse({"res": "请输入正确的caseId", "state": 400})

    return

def checkParamInt(object):
    newObject = object
    if object == None:
        newObject = 0
    return int(newObject)

