#Write a function called get_distance that returns the Euclidian distance between two 2D points
#This function will have four parameters (x1, x2, y1, y2)

def get_distance(x1,x2,y1,y2):
    d=(((x2-x1)**2)+((y2-y1)**2))**0.5
    print('The Euclidian distance ' +str(d))
    '''return d'''
