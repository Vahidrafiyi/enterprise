import datetime
import socket

from django.utils import timezone

from header_footer.models import VisitorInfo


def save_visitor_info(request):
    try:
        # ----- get visitor ip -----#
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
            # ----- check if ip adress is valid -----#
        try:
            socket.inet_aton(ip)
            ip_valid = True
        except socket.error:
            ip_valid = False
        # ----- check if ip adress is valid -----#
        if ip_valid:

            present_date = timezone.now()
            ref_date_1 = present_date - datetime.timedelta(days=1)
            ref_date_2 = present_date - datetime.timedelta(days=2)

            if VisitorInfo.objects.filter(ip_address=ip, page_visited=request.path,
                                          event_date__gte=ref_date_1).count() == 0:
                new_visitor_info = VisitorInfo(
                    ip_address=ip,
                    page_visited=request.path,
                    event_date=present_date)
                new_visitor_info.save()

            if VisitorInfo.objects.filter(ip_address=ip, page_visited=request.path,
                                          event_date__gte=ref_date_1).count() == 1:
                visitor_info_obj = VisitorInfo.objects.get(ip_address=ip, page_visited=request.path,
                                                           event_date__gte=ref_date_1)
                visitor_info_obj.event_date = present_date
                visitor_info_obj.save()
    except:
        pass

    context_nb_vistors = 0
    ref_date = present_date - datetime.timedelta(minutes=5)
    context_nb_vistors = VisitorInfo.objects.filter(event_date__gte=ref_date).values_list('ip_address',
                                                                                          flat=True).distinct().count()

    return {"context_nb_vistors": context_nb_vistors}
