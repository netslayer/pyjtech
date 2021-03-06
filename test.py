from pyjtech import get_jtech

# Connect via IP
jtech = get_jtech('10.0.0.7')

# Valid zones are 1-8
zone_status = jtech.zone_status(1)

# Print zone status
print('Zone Number = {}'.format(zone_status.zone))
print('Zone Power is {}'.format('On' if zone_status.power else 'Off'))
print('AV Source = {}'.format(zone_status.av))

# Turn off zone #1
jtech.set_zone_power(1, True)

# Set source 5 for zone #1
#jtech.set_zone_source(1, 7)

# Set all zones to source 2
#jtech.set_all_zone_source(2)
