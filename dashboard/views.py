from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt

from models import UserRecipeSuggestions
from food_suggest import config

def dashboard_handler(request):
    return render(request, 'base.html', {})

def recipe_suggestion_handler(request):
    if request.method == "GET":
        limit = 200
        offset = request.GET.get('offset')
        #prob_filter = request.GET.getlist('problem')
        prob_filter = request.GET.get('problem')
        if prob_filter:
            prob_filter = [config.suggested_state[i.lower()] for i in prob_filter.split(",")]
        date_filter = request.GET.get('date')

        stat_filter = request.GET.get('status')
        status_filter=[]
        if stat_filter:
            status_filter=[]
            stat_filter = stat_filter.split(',')
            if 'Open' in stat_filter:
                status_filter.append(False)
            if 'Closed' in stat_filter:
                status_filter.append(True)
            del(stat_filter)

        range_from = request.GET.get('from')
        range_to = request.GET.get('to')

        if range_from and range_to:
            range_from = datetime.datetime.strptime(range_from, "%d-%b-%Y")
            range_to = datetime.datetime.strptime(range_to, "%d-%b-%Y")

        if not offset:
            offset = 0
        offset = int(offset)

        #return all suggestions
        if not prob_filter and not date_filter and not status_filter:
            res = UserRecipeSuggestions.objects.all().order_by("created_on")[offset : offset + limit]
        else:
            if prob_filter and range_from and range_to:
                res = UserRecipeSuggestions.objects.filter(problem__in=prob_filter,
                                                           created_on__range=(range_from, range_to)
                                                           ).order_by("-created_on")
            elif prob_filter and date_filter and status_filter:
                today = datetime.now().date()
                if date_filter == 'Today':
                    day = today
                elif date_filter == 'Yesterday':
                    day = today - timedelta(1)
                res = UserRecipeSuggestions.objects.filter(problem__in=prob_filter, email_status__in=status_filter, created_on=day).order_by("-created_on")
            elif prob_filter and date_filter:
                today = datetime.now().date()
                if date_filter == 'Today':
                    day = today
                elif date_filter == 'Yesterday':
                    day = today - timedelta(1)
                res = UserRecipeSuggestions.objects.filter(problem__in=prob_filter, created_on=day).order_by("-created_on")
            elif prob_filter and status_filter:
                res = UserRecipeSuggestions.objects.filter(problem__in=prob_filter, email_status__in=status_filter).order_by("-created_on")
            elif status_filter and date_filter:
                today = datetime.now().date()
                if date_filter == 'Today':
                    day = today
                elif date_filter == 'Yesterday':
                    day = today - timedelta(1)
                res = UserRecipeSuggestions.objects.filter(email_status__in=status_filter, created_on=day).order_by("-created_on")
            elif prob_filter:
                res = UserRecipeSuggestions.objects.filter(problem__in=prob_filter).order_by("-created_on")
            elif status_filter:
                res = UserRecipeSuggestions.objects.filter(email_status__in=status_filter).order_by("-created_on")
            elif range_from and range_to:
                res = UserRecipeSuggestions.objects.filter(created_on__range=(range_from, range_to)).order_by("-created_on")
            else:
                #datefilter
                today = datetime.now().date()
                if date_filter == 'Today':
                    day = today
                elif date_filter == 'Yesterday':
                    day = today - timedelta(1)
                res = UserRecipeSuggestions.objects.filter(created_on=day).order_by("-created_on")

        resp = []
        for r in res:
            temp = {
                "id" : r.id,
                "created_by": r.created_by,
                "email" : r.email,
                "apk_version" : r.apk_version,
                "subscription_type" : val_to_key(config.subscription_types, r.subscription_type),
                "suggested_food" : r.suggested_food,
                "problem" : val_to_key(config.suggested_state, r.problem),
                "same_as" : r.same_as,
                "action_taken" : r.action_taken,
                "gcm_push" : r.gcm_push,
                "email_status" : r.email_status,
                "created_on" : r.created_on
            }
            resp.append(temp)
        #suggestions = serializers.serialize('json', res)
        data = {'success' : True, 'data' : resp}
        return JsonResponse(data)

@csrf_exempt
def recipe_update_handler(request, suggestion_id):
    if request.method == "PUT":
        # update email_status to True
        type = request.GET.get('type')
        if type == "mail":
            response = mail_handler('','', '')  # to_address, subject , content
            if response:
                res = UserRecipeSuggestions.objects.filter(id=suggestion_id).update(email_status=True)
            else:
                res = False
        elif type == "action":
            res = UserRecipeSuggestions.objects.filter(id=suggestion_id).update(action_taken=True)
        elif type == "gcmpush":
            res = UserRecipeSuggestions.objects.filter(id=suggestion_id).update(gcm_push=True)
        elif type == "sameas":
            res = UserRecipeSuggestions.objects.filter(id=suggestion_id).update(same_as=True)

        if res:
            return JsonResponse({'success':True})
        else:
            return JsonResponse({'success':False})


def mail_handler(to_address, subject, content):
    from django.conf import settings
    from django.core.mail import send_mail

    subject = "Thanks for suggesting a new recipe"
    content = "We have added the new Recipe, please check in the recipe list."
    to_address = "sreebunny5@gmail.com"
    mail_status = send_mail(subject, content, settings.EMAIL_HOST_USER, ['sreebunny5@gmail.com'],
              fail_silently=False)
    return bool(mail_status)


def val_to_key(dict, val):
    for key, value in dict.iteritems():
        if value == val:
            return key