import time
import random


score = 0
ent = int(input("How many enemies"))

while ent>0:
    prob = random.uniform(0, 100)
    if prob <10:
        enemy = "shotgun man"
    elif prob>10 and prob<55:
        enemy = "ar man"
    elif prob>55:
        enemy = "pistol man"
    print (enemy)

    #when enemy killed

    enemyk = (enemy + " killed")

    if enemy == "shotgun man":
        sbullet = random.randint(2,5)
        print("Picked shotgun with " + str(sbullet) + " bullets")
        score += 50
        
    elif enemy == "ar man":
        arbullet = random.randint(15, 30)
        print("Picked ar with " + str(arbullet) + " bullets")
        score += 30
        
    elif enemy == "pistol man":
        pbullet = random.randint(5, 15)
        print("Picked pistol with " + str(pbullet) + " bullets")
        score += 20
    ent -=1
    time.sleep(2)
    
print ("Score: " + str(score))
    
