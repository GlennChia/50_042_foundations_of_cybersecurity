# 50.042 FCS Lab 5 Modular Arithmetics
# Year 2019

import copy
class Polynomial2:
    def __init__(self,coeffs):
        self._coeffs = coeffs

    def add(self,p2):
        add_result = []
        # Extend the shorter array
        len_p1 = len(self._coeffs)
        len_p2 = len(p2._coeffs)
        difference_length = abs(len_p1 - len_p2)
        if len_p1 > len_p2:
            for zero_counter in range(difference_length):
                p2._coeffs.append(0)
        else:
            for zero_counter in range(difference_length):
                self._coeffs.append(0)
        for index, indiv_bit in enumerate(self._coeffs):
            add_result.append(p2._coeffs[index] ^ indiv_bit)
        return(Polynomial2(add_result))


    def sub(self,p2):
        add_result = []
        # Extend the shorter array
        len_p1 = len(self._coeffs)
        len_p2 = len(p2._coeffs)
        difference_length = abs(len_p1 - len_p2)
        if len_p1 > len_p2:
            for zero_counter in range(difference_length):
                p2._coeffs.append(0)
        else:
            for zero_counter in range(difference_length):
                self._coeffs.append(0)
        for index, indiv_bit in enumerate(self._coeffs):
            add_result.append(p2._coeffs[index] ^ indiv_bit)
        return(Polynomial2(add_result))

    def mul(self,p2,modp=None):
        if modp:
            reduction_limit = len(modp._coeffs)
            p2_clone = p2._coeffs
            storage = []
            # For loop through the reference which will be self
            for iterations in range(len(self._coeffs)):
                state = self._coeffs[iterations]
                if iterations == 0:
                    zero_array = p2_clone
                else:
                    try:
                        if p2_clone[-1] == 0:
                            zero_array = [0]
                            zero_array.extend(p2_clone)
                            del zero_array[-1]
                        else:
                            zero_array = [0]
                            zero_array.extend(p2_clone)
                            del zero_array[-1]
                            add_result = []
                            for index, indiv_bit in enumerate(zero_array):
                                add_result.append(modp._coeffs[index] ^ indiv_bit)
                            zero_array = add_result
                    except:
                        # Just shift
                        zero_array = [0]
                        zero_array.extend(p2_clone)
                p2_clone = zero_array
                if state == 1:
                    storage.append(zero_array)
            # Add the partial results
            mult_result = [0 for i in range(reduction_limit - 1)]
            for operables in storage:
                for index_final, value_final in enumerate(mult_result):
                    try:
                        mult_result[index_final] = value_final ^ operables[index_final]
                    except:
                        pass
        else:
            # Standard polynomial
            p2_clone = p2._coeffs
            storage = []
            # For loop through the reference which will be self
            for iterations in range(len(self._coeffs)):
                state = self._coeffs[iterations]
                if iterations == 0:
                    zero_array = p2_clone
                else:
                    zero_array = [0]
                    zero_array.extend(p2_clone)
                p2_clone = zero_array
                if state == 1:
                    storage.append(zero_array)
            # Add the partial results
            mult_result = [0 for i in range(reduction_limit - 1)]
            for operables in storage:
                for index_final, value_final in enumerate(mult_result):
                    try:
                        mult_result[index_final] = value_final ^ operables[index_final]
                    except:
                        pass
        return Polynomial2(mult_result)

    def div(self,p2):
        pass
        return q, r

    def __str__(self):
        formatted_polynomial = ''
        temporary_coeffs = self._coeffs
        temporary_coeffs.reverse()
        for index_coeff, indiv_coeff in enumerate(temporary_coeffs):
            if index_coeff == len(temporary_coeffs) - 1:
                if indiv_coeff == 1:
                    formatted_polynomial += 'x^{}'.format(0)
                else:
                    formatted_polynomial = formatted_polynomial[: -1]
            else:
                if indiv_coeff == 1:
                    formatted_polynomial += 'x^{}+'.format(len(temporary_coeffs) - 1 - index_coeff)
        return formatted_polynomial

    def getInt(p):
        value = 0
        for index_coeff, indiv_coeff in enumerate(p):
            value += indiv_coeff * 2 ** index_coeff
        return value


class GF2N:
    affinemat=[[1,0,0,0,1,1,1,1],
               [1,1,0,0,0,1,1,1],
               [1,1,1,0,0,0,1,1],
               [1,1,1,1,0,0,0,1],
               [1,1,1,1,1,0,0,0],
               [0,1,1,1,1,1,0,0],
               [0,0,1,1,1,1,1,0],
               [0,0,0,1,1,1,1,1]]

    def __init__(self,x,n=8,ip=Polynomial2([1,1,0,1,1,0,0,0,1])):
        pass


    def add(self,g2):
        pass
    def sub(self,g2):
        pass
    
    def mul(self,g2):
        pass

    def div(self,g2):
        pass

    def getPolynomial2(self):
        pass

    def __str__(self):
        pass

    def getInt(self):
        pass

    # def mulInv(self):
    #     pass

    # def affineMap(self):
    #     pass

print('\nTest 1')
print ('======')
print ('p1=x^5+x^2+x')
print ('p2=x^3+x^2+1')
p1=Polynomial2([0,1,1,0,0,1])
p2=Polynomial2([1,0,1,1])
p3=p1.add(p2)
print ('p3= p1+p2 = {}'.format(p3))

print ('\nTest 2')
print ('======')
print ('p4=x^7+x^4+x^3+x^2+x')
print ('modp=x^8+x^7+x^5+x^4+1')
p4=Polynomial2([0,1,1,1,1,0,0,1])
modp=Polynomial2([1,0,0,0,1,1,0,1,1])
p5=p1.mul(p4,modp)
print ('p5=p1*p4 mod (modp)= {}'.format(p5))

print ('\nTest 3')
print ('======')
print ('p6=x^12+x^7+x^2')
print ('p7=x^8+x^4+x^3+x+1')
p6=Polynomial2([0,0,1,0,0,0,0,1,0,0,0,0,1])    
p7=Polynomial2([1,1,0,1,1,0,0,0,1])
p8q,p8r=p6.div(p7)
print ('q for p6/p7= {}'.format(p8q))
print ('r for p6/p7= {}'.format(p8r))

####
print ('\nTest 4')
print ('======')
g1=GF2N(100)
g2=GF2N(5)
print ('g1 = {}'.format(g1.getPolynomial2()))
print ('g2 = {}'.format(g2.getPolynomial2()))
g3=g1.add(g2)
print ('g1+g2 = {}'.format(g3))

print ('\nTest 5')
print ('======')
ip=Polynomial2([1,1,0,0,1])
print ('irreducible polynomial {}'.format(ip))
g4=GF2N(0b1101,4,ip)
g5=GF2N(0b110,4,ip)
print ('g4 = {}'.format(g4.getPolynomial2()))
print ('g5 = {}'.format(g5.getPolynomial2()))
g6=g4.mul(g5)
print ('g4 x g5 = {}'.format(g6.p))

print ('\nTest 6')
print ('======')
g7=GF2N(0b1000010000100,13,None)
g8=GF2N(0b100011011,13,None)
print ('g7 = {}'.format(g7.getPolynomial2()))
print ('g8 = {}'.format(g8.getPolynomial2()))
q,r=g7.div(g8)
print ('g7/g8 =')
print ('q = {}'.format(q.getPolynomial2()))
print ('r = {}'.format(r.getPolynomial2()))

# print '\nTest 7'
# print '======'
# ip=Polynomial2([1,1,0,0,1])
# print 'irreducible polynomial',ip
# g9=GF2N(0b101,4,ip)
# print 'g9 = ',g9.getPolynomial2()
# print 'inverse of g9 =',g9.mulInv().getPolynomial2()

# print '\nTest 8'
# print '======'
# ip=Polynomial2([1,1,0,1,1,0,0,0,1])
# print 'irreducible polynomial',ip
# g10=GF2N(0xc2,8,ip)
# print 'g10 = 0xc2'
# g11=g10.mulInv()
# print 'inverse of g10 = g11 =', hex(g11.getInt())
# g12=g11.affineMap()
# print 'affine map of g11 =',hex(g12.getInt())
