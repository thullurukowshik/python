sec = int(input())

secs = sec%60

minu = sec//60

hours = sec//3600

days = sec//86400

print(f "{days}:days , {hours}:hours , {minu}:minutes , {secs} : seconds")
