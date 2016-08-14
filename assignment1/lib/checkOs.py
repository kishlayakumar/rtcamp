import platform


def checkOs():
 osDetails = platform.platform()
 osDetails = osDetails.split("-")
 os = osDetails[-3]
 return os
