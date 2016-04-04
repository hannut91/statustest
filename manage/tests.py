from django.test import TestCase
"""
from .models import Notice, Maintenance, Version, Applist

class ApplistMethodTests(TestCase):

    def applist_fetch_test(self):
        def get(self, request):
        useros = request.GET.get('os',None)
        locale = request.GET.get('locale',None)
        #exception
        if not useros or not locale:
            return JsonResponse({'msg':GET_FAIL_MESSAGE})
        try:
            result = Applist.objects.get(app_nm=useros)
        except Applist.MultipleObjectsReturned, Applist.DoesNotExist:
            return JsonResponse({'msg':FAIL_MESSAGE})

        output = {}
        if result.version:
            temp = {}
            temp['rec_ver'] = result.version.rec_ver
            temp['man_ver'] = result.version.man_ver
            temp['reg_dt'] = result.version.reg_dt
            output['Version'] = temp
        notice_result = result.notice_set.filter(locale=locale)
        if notice_result:
            templist = []
            for notice_list in notice_result:
                temp = {}
                temp['nt_title'] = notice_list.title
                temp['nt_text'] = notice_list.text
                temp['nt_url'] = notice_list.url
                temp['nt_st_dt'] = notice_list.st_dt
                temp['nt_en_dt'] = notice_list.en_dt
                temp['nt_show_dt'] = notice_list.show_nt
                templist.append(temp)
            output['Notice'] = templist
        mtn_result = result.maintenance_set.all()
        if mtn_result:
            templist = []
            for mtn_list in mtn_result:
                temp = {}
                temp['mtn_url'] = mtn_list.url
                temp['mtn_st_dt'] = mtn_list.st_dt
                temp['mtn_en_dt'] = mtn_list.en_dt
                templist.append(temp)
            output['Maintenance'] = templist

        if output:
            return JsonResponse(output)
        else:
            return JsonResponse({'msg':FAIL_MESSAGE})


"""