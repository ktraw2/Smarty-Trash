from django.shortcuts import render
from .models import *
from datetime import datetime, timedelta
from . import timeanddate
from tzlocal import get_localzone
from dateutil.relativedelta import relativedelta


# Create your views here.
def livedata(request):
    return render(request, "data/livedata.json")


def statistics(request, years, months, days, hours, minutes):
    delta = datetime.now() - relativedelta(years=int(years), months=int(months), days=int(days), hours=int(hours), minutes=int(minutes))

    context = {
        'cutoff_year': str(delta.year),
        'cutoff_month': str(delta.month),
        'cutoff_day': str(delta.day),
        'cutoff_hour': str(delta.hour),
        'cutoff_minute': str(delta.minute)
    }
    # Iterate through each entry in the db, if it is less than the tuple, then check the next one
    # Keep some sort of variable to get an average/whatever
    # To verify, we can subtract now from the date in the db entry
    return render(request, "data/statistics.json", context=context)

    # date_string = str(delta.year) + "-" + str(delta.month) + "-" + str(delta.day) + " " + str(delta.hour) + ":" + str(delta.minute)
    # print(date_string)
    # cutoff_date_tuple = timeanddate.calculate_date_difference("now", date_string, str(get_localzone()), return_as_string=False)