
from __future__ import print_function

import datetime
import re

import aprs
import pycot


# http://xmlwriter.net/xml_guide/xml_declaration.shtml

# 3833.55N/12248.93W
LL_REX = re.compile(
    r"(?P<aprs_lat>\d{4}\.\d{2})[NS]/(?P<aprs_lng>\d{5}\.\d{2})[EW]"
)

def decode_ll(ll):
    ll_match = LL_REX.search(ll)
    if ll_match is not None:
        aprs_lat = ll_match.group('aprs_lat')
        aprs_lat_hours = int(aprs_lat[:2])
        aprs_lat_mins = float(aprs_lat[-5:])
        decimal_lat = aprs.decimaldegrees.dm2decimal(
            aprs_lat_hours, aprs_lat_mins
        )

        aprs_lng = ll_match.group('aprs_lng')
        aprs_lng_hours = int(aprs_lng[:3])
        aprs_lng_mins = float(aprs_lng[-5:])
        decimal_lng = aprs.decimaldegrees.dm2decimal(
            aprs_lng_hours, aprs_lng_mins
        )

        return decimal_lat, decimal_lng


def main():
    #aprs_filter = 'r/35.7157886/-120.7675918/10'  # McMillian
    aprs_filter = 'r/37.76/-122.4975/100'  # Home
    aprs_client = aprs.TCP('W2GMD', 'xxx', aprs_filter=aprs_filter)
    aprs_client.start()
    aprs_client.receive(to_cot)

def to_cot(aprs_frame):
    decoded_ll = decode_ll(aprs_frame.text)
    if decoded_ll is None:
        return

    my_point = pycot.Point()
    my_point.lat = decoded_ll[0]
    my_point.lon = decoded_ll[1]
    my_point.ce = '1'
    my_point.le = '1'
    my_point.hae = '1'

    e = pycot.Event()
    e.version = '0.1'
    e.event_type = 'a-.-G-E-V-C'
    e.uid = 'APRS.%s' % aprs_frame.source
    e.time = datetime.datetime.now()
    e.how = 'h-e'
    e.point = my_point
    print(e.render(standalone=True))


if __name__ == '__main__':
    main()
