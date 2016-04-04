from django.shortcuts import render, render_to_response
from manage.models import Maintenance, Notice, Applist, UpdateList
from django.http import JsonResponse
from django.db.models import Q

from django.views.generic import View,TemplateView
import MySQLdb

VERSION_FAIL_MESSAGE = "Can't find device's version infomation"
FAIL_MESSAGE = "Can't find device's ID"
GET_FAIL_MESSAGE = "Can't find GET message"
SUCCESS_MESSAGE = "Success"


class CheckPing(TemplateView):
    def get(self, request):
        db = MySQLdb.connect("192.168.73.178", "root", "dnflwlq2", "status")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM ping_stat")
        pingStatelist = cursor.fetchall()
        return render_to_response("server/pingstate.html",{'pinglist':pingStatelist})




class CheckState(View):
    def get(self, request):
        useros = request.GET.get('os',None)
        locale = request.GET.get('locale',None)

        if not useros or not locale:
            return JsonResponse({'msg':GET_FAIL_MESSAGE})
        try:
            result = Applist.objects.get(app_name=useros)
        except (Applist.MultipleObjectsReturned,Applist.DoesNotExist):
            return JsonResponse({'msg':FAIL_MESSAGE})
        output = {}
        mtn_list = result.maintenance_set.all()
        notice_result = result.notice_set.filter(Q(locale=locale)|Q(locale='ww'))

        if mtn_list:
            templist = []
            for mtn_list in mtn_list:
                temp = {}
                temp['maintenance_url'] = mtn_list.url
                temp['maintenance_start_time'] = mtn_list.start_time
                temp['maintenance_end_time'] = mtn_list.end_time
                templist.append(temp)
            output['Maintenance'] = templist
            return JsonResponse(output)
        elif notice_result:
            templist = []
            for notice_list in notice_result:
                temp = {}
                temp['notice_title'] = notice_list.title
                temp['notice_text'] = notice_list.text
                temp['notice_url'] = notice_list.url
                temp['notice_start_time'] = notice_list.start_time
                temp['notice_end_time'] = notice_list.end_time
                temp['notice_show'] = notice_list.show_notice
                templist.append(temp)
            output['Notice'] = templist
        if not result.updatelist_set.all():
            return JsonResponse({'msg':VERSION_FAIL_MESSAGE})
        version_result = result.updatelist_set.order_by('-build_ver')[0]
        if version_result:
            temp = {}
            temp['rec_ver'] = version_result.rec_ver
            temp['man_ver'] = version_result.man_ver
            temp['register_time'] = version_result.register_time
            output['Version'] = temp

        if output:
            return JsonResponse(output)
        else:
            return JsonResponse({'msg':FAIL_MESSAGE})

def home(request):
    return render(request, 'mobile/index.html')

#class based view
def check_stat(request):
    useros = request.GET['os', None]
    locale = request.GET['locale', None]
    #exception


    app_id = device(useros)
    if app_id == 3:
        return JsonResponse({'msg:':FAIL_MESSAGE})

    try:
        version_info = Version.objects.get(appid=app_id)
    except Version.DoesNotExist:
        version_info = None
    #note for result
    try:
        mtn_info = Maintenance.objects.filter(appid=app_id,on=1)
    except Maintenance.DoesNotExist:
        mtn_info = None
    #exception

    try:
        nt_info = Notice.objects.filter(appid=app_id,locale=locale)
    except Notice.DoesNotExist:
        nt_info = None

    result = {}

    if version_info:
        result['recVer'] = version_info.recVer
        result['manVer'] = version_info.manVer
    if mtn_info:
        temp = []
        for mtn_list in mtn_info:
            list_temp= {}
            list_temp['mtn_url'] = mtn_list.url
            list_temp['mtn_until'] = mtn_list.until
            temp.append(list_temp)
        result['maintenance'] = temp
    if nt_info:
        temp = []
        for nt_list in nt_info:
            list_temp = {}
            list_temp['nt_title'] = nt_list.title
            list_temp['nt_text'] = nt_list.text
            list_temp['nt_url'] = nt_list.url
            list_temp['nt_until'] = nt_list.until
            temp.append(list_temp)
        result['notice'] = temp
    if result:
        return JsonResponse(result)
    else:
        return JsonResponse({'msg':FAIL_MESSAGE})


def check_version(request, useros):
    app_id = device(useros)
    if device(useros) == 2:
        return JsonResponse({'msg':FAIL_MESSAGE})

    temp = Version.objects.get(appid=app_id)

    if temp:
        temp2 = {'recVer':temp.recVer,'manVer':temp.manVer,'msg':SUCCESS_MESSAGE}
        return JsonResponse(temp2)
    else:
        return JsonResponse({'msg':FAIL_MESSAGE})



def check_maintenance(request, useros):
    app_id = device(useros)
    if device(useros) == 2:
        return JsonResponse({'msg':FAIL_MESSAGE})

    temp = Maintenance.objects.get(appid=app_id, on=1)

    if temp:
        temp2 = {'url':temp.url,'until':temp.until}
        return JsonResponse(temp2)
    else:
        return JsonResponse({'msg':FAIL_MESSAGE})

def check_notice(request, useros, locale):
    app_id = device(useros)
    if device(useros) == 2:
        return JsonResponse({'msg':FAIL_MESSAGE})

    temp = Notice.objects.get(Q(appid=app_id), Q(locale=locale)|Q(locale='ww'))

    if temp:
        temp2 = {'title':temp.title,'text':temp.text,'url':temp.url,'until':temp.until}
        return JsonResponse(temp2)
    else:
        return JsonResponse({'msg':FAIL_MESSAGE})


def device(device):
    if device =="ios":
        return 1
    elif device == "android":
        return 2
    else:
        return 3
