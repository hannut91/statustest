from django.shortcuts import render, render_to_response
from manage.models import Maintenance, Notice, Applist, UpdateList
from django.http import JsonResponse, HttpResponse
from django.db.models import Q

from django.views.generic import View,TemplateView
import MySQLdb

APPNAME_FAIL_MESSAGE = "Can't find appname"
VERSION_FAIL_MESSAGE = "Can't find device's version infomation"
FAIL_MESSAGE = "Can't find device's ID"
GET_FAIL_MESSAGE = "Can't find GET data"
SUCCESS_MESSAGE = "Success"
NATIONAL = ['ko','en','jp','es','zh','fr']

class CheckPing(TemplateView):

    def get(self, request):
        db = MySQLdb.connect("localhost", "root", "dnflwlq2", "status")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM ping_stat")
        pingStatelist = cursor.fetchall()
        return render_to_response("server/pingstate.html",{'pinglist':pingStatelist})


class CheckState(View):
    def get(self, request):
        useros = request.GET.get('os',None)
        locale = request.GET.get('locale',None)

        if not useros or locale not in NATIONAL:
            return JsonResponse({'msg':GET_FAIL_MESSAGE})

        try:
            result = Applist.objects.get(app_name=useros)
        except (Applist.MultipleObjectsReturned, Applist.DoesNotExist):
            return JsonResponse({'msg':APPNAME_FAIL_MESSAGE})

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

        if not result.updatelist_set.filter(Q(locale=locale)|Q(locale='ww')):
            return JsonResponse({'msg':VERSION_FAIL_MESSAGE})

        version_result = result.updatelist_set.filter(Q(locale=locale)|Q(locale='ww')).order_by('-build_ver')[0]

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
    
class CheckState(View):

    def post(self, request):
        return HttpResponse