from django.shortcuts import render
from . functions import  UPorDOWN, DateRecieve, AbrDay, UsersAuth_DAY, UsersAuth_pDAY, UsersAuth_MON, UsersAuths_pMON, Date_Today
def showhowmany(request):
    date = DateRecieve()
    DAU, sd = UsersAuth_DAY(date=date)
    date_day = AbrDay(sd)
    prevDAU = UsersAuth_pDAY(date=date)
    MAU, sm, em = UsersAuth_MON(date=date)
    date_month = AbrDay(sm) + " - " + AbrDay(em)
    prevMAU = UsersAuths_pMON(date=date)
    tria_DAU, DAUgrowth, colD = UPorDOWN(DAU, prevDAU)#изменения за прошлый день
    tria_MAU, MAUgrowth, colM = UPorDOWN(MAU, prevMAU)#изменения за прошлый месяц
    MAU=str(MAU)[:-3]+' '+ str(MAU)[-3:]
    DAU = str(DAU)[:-3] + ' ' + str(DAU)[-3:]
    date_today=Date_Today()
    date_today_year = date_today.year
    date_today=AbrDay(date_today)+", "+str(date_today_year)
    context = {"DAU": DAU, "MAU": MAU , "date_day": date_day, "date_month": date_month, "MAUgrowth": MAUgrowth, "DAUgrowth":DAUgrowth, "trMAU":tria_MAU, "trDAU":tria_DAU, "CD": colD, "CM":colM,"date_today":date_today}

    return render(request, 'showusers/howmanyusers.html', context)

