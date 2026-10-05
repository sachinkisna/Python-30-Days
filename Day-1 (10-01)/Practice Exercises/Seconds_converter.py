second=input("Entyer How Many Seconds: ")

#logi
#100
#100//60=1 Minute
#100//3600= Hour
#100%60=40  Second

hours=int(second)//3600
minutes=int(second)//60
seconds=int(second)%60

print(f"{hours}:{minutes}:{seconds}")
