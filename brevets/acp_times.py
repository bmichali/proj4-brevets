"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import math

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    new_date = arrow.get(brevet_start_time)
    if control_dist_km == 0:
        return new_date.isoformat()

    max_speed = {200: 34, 300: 32, 400: 32, 600: 30, 1000: 28}

    if brevet_dist_km <= control_dist_km <= brevet_dist_km*1.10 :
        control_dist_km = brevet_dist_km

    temp_time = 0
    for key, speed in max_speed.items():
        if(control_dist_km <= int(brevet_dist_km)):
            temp_time += control_dist_km/speed
            break
        elif(control_dist_km > key):
            temp_time += 200/speed
        control_dist_km -= 200

    temp_time = math.modf(temp_time)
    opening_time = (float(temp_time[0])*60, int(temp_time[1]))
    return brevet_start_time.shift(hours=+opening_time[1],
                                   minutes=+opening_time[0]).isoformat()

def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
          brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    new_date = arrow.get(brevet_start_time)
    if control_dist_km == 0:
        return new_date.shift(hours=+1).isoformat()

    min_speed = {200: 15, 300: 15, 400: 15, 600: 15, 1000: 11.428}

    if control_dist_km >= brevet_dist_km*1.10:
        control_dist_km = brevet_dist_km

    if control_dist_km == 200:
        return brevet_start_time.shift(hours=+13, minutes=+30).isoformat()

    temp_time = 0
    for dist, speed in min_speed.items():
        if control_dist_km <= int(brevet_dist_km):
            temp_time += control_dist_km / speed
            break
        elif control_dist_km > dist:
            temp_time += 200 / speed
        control_dist_km -= 200

    temp_time = math.modf(temp_time)
    opening_time = (float(temp_time[0]) * 60, int(temp_time[1]))
    return brevet_start_time.shift(hours=+opening_time[1],
                                   minutes=+opening_time[0]).isoformat()
