#TaxiRate - How far does 100 pesos take you in different speeds?

timePrice = 1.31/45 #Price per second
distancePrice = 1.31/250 #Price per m
speed = 0
budget = 100
travelTimeUnits = 100/(1.31)

while speed < 20:
    speed = speed + 1
    timeFor250 = 250/speed
    if timeFor250 > 45:
        Limiter = "time"
        DistanceTravelled = 100/(1.31/45) * speed
    else:
        Limiter = "distance"

        DistanceTravelled = 100/distancePrice

    print("If you have the speed of " + str(speed*3.6) + " km/h the fare will be measured by " + str(Limiter) + " and 100 pesos in your pocket, it will take you " + str(DistanceTravelled) +  " meters")
            
    
