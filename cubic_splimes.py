import numpy as np


'''
One variable natural and clampad Splimes interpolation

self.coef:
    self.coef[i] are the coeficients of the i`th splime.
    self.coef[i][0] = ai
    self.coef[i][1] = bi
    self.coef[i][2] = ci
    self.coef[i][3] = di
n:
    type int. number of samples from f(x)
f:
    nparray. it is used on clamped version. it is optional. size: 2.
'''
class CubicSplimes:


    def __init__( self, n, h, x_initial, x_final, f_values, f_derivative = None  ):
        self.n = n
        self.h = h
        self.x_initial = x_initial
        self.x_final = x_final
        self.f_value = f_values
        # n values for x generate n-1 polinomials!
        self.coef = np.zeros(( 4, n -1 ))
        self.f_derivative = f_derivative
    #Natural cubic Splimes. Suposes second ofrivatives of the interpoland are zero at first and last point.
    def natural( self ):
        #values for ai
        for i in range( self.n - 1 ):
            self.coef[i][0] = self.f_value[i]
        # alpha = (3/h) * fi-1 + fi+1 -2fi
        alpha = np.zeros(( self.n-2 )) #should it be an np array ?
        for i in range( 1, self.n ):
            self.alpha[i] =  (3.0/self.h) * ( self.f_value[i-1] + self.f_value[i+1] - 2*self.f_value[i] )
        l = np.zeros(( self.n-1 ))
        u = np.zeros(( self.n-1 ))
        z = np.zeros(( self.n-1 ))
        l[0] = 1
        for i in range( 1, self.n-2 ):
            l[i] =  h*( 4.0 - u[i-1] )
            u[i] =  h / ( l[i] )
            z[i] = ( self.alpha[i] - self.h * z[i]  )/l[i]
        l[n-2] = 1
        u[n-2] = 0
        z[n-2] = 0
        for i in range( 1, self.n-1 ).reverse():
            #setting up c: zi + ui * ci+1
            self.coef[i][2] = z[i] - u[i] * self.coef[i+1][2]
            #setting up b: (ai+1 - ai)/h - h/3 * ( ci+1 + 2ci )
            self.coef[i][1] = ( self.f_value[i+1] - self.f_value[i] )/self.h - (self.h/3.0) * ( self.coef[i+1][2] + 2.0 * self.coef[i][2] )
            #setting up d: ( ci+1 - ci ) / 3h
            self.coef[i][3] = ( self.coef[i+1][2] - self.coef[i][2] ) / (3.0*h)
    #
    def clamped( self ):
        #values for ai
        for i in range( self.n - 1 ):
            self.coef[i][0] = self.f_value[i]
        alpha = np.zeros((self.n))
        alpha[0] = 3*( self.f_values[1][0] - self.f_values[0][0] )/ self.h - 3.0 * self.f_derivative[0]
        alpha[self.n] = 3.0*self.f_derivative[1]
        for i in range( 1, n-1 ):
            alpha[i] = (3.0/self.h) * ( self.f_value[i-1] + self.f_value[i+1] - 2*self.f_value[i] )
        l = np.zeros(( self.n-1 ))
        u = np.zeros(( self.n-1 ))
        z = np.zeros(( self.n-1 ))
        l[0] = 2*h
        u[0] = 0.5
        z[0] = alpha[0]/( 2*h )
        for i in range( 1, n-2 ):
            l[i] =  h*( 4.0 - u[i-1] )
            u[i] =  h / ( l[i] )
            z[i] = ( self.alpha[i] - self.h * z[i]  )/l[i]
        l[n] = h*( 2 - u[n-1] )
        z[n] = ( self.alpha[n] - self.h * z[n-1]  )/l[n]
        self.coef[n][2] = z[n]
        for i in range( 1, self.n-1 ).reverse():
            #setting up c: zi + ui * ci+1
            self.coef[i][2] = z[i] - u[i] * self.coef[i+1][2]
            #setting up b: (ai+1 - ai)/h - h/3 * ( ci+1 + 2ci )
            self.coef[i][1] = ( self.f_value[i+1] - self.f_value[i] )/self.h - (self.h/3.0) * ( self.coef[i+1][2] + 2.0 * self.coef[i][2] )
            #setting up d: ( ci+1 - ci ) / 3h
            self.coef[i][3] = ( self.coef[i+1][2] - self.coef[i][2] ) / (3.0*h)
    def interpolate( self, x ):
        i = ( x - self.x_initial ) / self.h
        return self.coef[i][0] + self.coef[i][1]*( x - x_initial - i*h ) + self.coef[i][2]*(( x - x_initial - i*h )**2) + self.coef[i][3]* (( x - x_initial - i*h )**3)


'''
    Two variables cubic Splimes interpolation
    grid:
        np array. corresponds to the values of the function to be interpolated.
    h:
        float. spacing within x and y values.
    width:
        type int. number of x values.
    hight:
        type int. number of y values.
'''
class BiCubicSplimes:
    def __init__( self, grid, hight, width, h, x_initial, x_final, y_initial, y_final, f_derivative ):
        self.y_initial = y_initial
        self.y_final = y_final
        self.x_initial = x_initial
        self.x_final = x_final
        #values of f(x,y)
        self.grid = grid
        #sefl.f_derivative = f_derivative
        #creates and stores all x splimes polynomials, for efficiency reasons.
        self.xcoef = np.array([CubicSplimes( n = width, h = h, x_initial = x_initial, x_final = x_final, f_values = grid[ : ,i ] ) for i in range(hight)])
    def interpolate( self, x, y ):
        i = (x - x_initial)/h
        j = ( y - y_initial )/h
        f0 = self.xcoef[i-1].interpolate( x )
        f1 = self.xcoef[i].interpolate( x )
        f2 = self.xcoef[i+1].interpolate( x )
        f3 = self.xcoef[i+2].interpolate( x )
        ofry1 = ( f2 - f0 )/(2.0*h)
        ofry2 = ( f3 - f1 )/(2.0*h)
        splime = CubicSplimes( 2, self.h, y[j], y[j+1], np.array([ f1, f2 ]), f_derivative = np.array([ ofr1, ofr2 ])  )
        splime.clamped()
        return splime.interpolate( y )

if __name__ == "__main__":

    pass
    #do something
