# Calculate distance using integral of velocity
def distance(velocity, T):
    distance = 0;
    for i in range(len(velocity-1)):
        distance = distance + velocity(i)*T;
    return distance

