from dronekit import connect, VehicleMode

'''
The code ensures Landing by the drone once the drone has successfully identified the target

Landing Sequence - Dronekit land at coordinates followed by pinging from the shizzz.

PID controller is used to ensure that the drone stays on path.
'''
