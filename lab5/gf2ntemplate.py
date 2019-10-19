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
            to_append = reduction_limit - len(p2_clone) - 1
            for i in range(to_append):
                p2_clone.append(0)
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
            reduction_limit = len(self._coeffs) + len(p2._coeffs)
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


    # Helper methods
    def deg(self):
        for index_coefficient, coefficient in enumerate(self._coeffs):
            if coefficient == 1:
                index_coeff = index_coefficient
        return index_coeff


    def lc(self):
        for index_coefficient, coefficient in enumerate(self._coeffs):
            if coefficient == 1:
                leading_coefficient = coefficient
        return leading_coefficient


    def div(self,p2):
        # Create q based on the highest power of the quotient
        q = Polynomial2([])
        for i in range(len(self._coeffs) - len(p2._coeffs) + 1):
            q._coeffs.append(0)
        r = copy.deepcopy(self)
        b = p2
        d = b.deg()
        c = b.lc()
        while r.deg() >= d:
            power = r.deg() - d
            coeff_power = int(r.lc()/ c)
            s = []
            for i in range(power):
                s.append(0)
            s.append(coeff_power)
            q = Polynomial2(s).add(q)
            sb = Polynomial2(s).mul(b)
            r = r.sub(sb)
        return q, r

    def __str__(self):
        formatted_polynomial = ''
        temporary_coeffs = copy.deepcopy(self._coeffs)
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

    def getInt(self):
        value = 0
        for index_coeff, indiv_coeff in enumerate(self._coeffs):
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
        self.x =x
        self.n = n
        self.ip = ip
        self.p = self.getPolynomial2()


    def add(self,g2):
        add_result = []
        # Extend the shorter array
        self_coeffs = self.getPolynomial2List()
        g2_coeffs = g2.getPolynomial2List()
        len_g1 = len(self_coeffs)
        len_g2 = len(g2_coeffs)
        difference_length = abs(len_g1 - len_g2)
        if len_g1 > len_g2:
            for zero_counter in range(difference_length):
                g2_coeffs.append(0)
        else:
            for zero_counter in range(difference_length):
                self_coeffs.append(0)
        for index, indiv_bit in enumerate(self_coeffs):
            add_result.append(g2_coeffs[index] ^ indiv_bit)
        # Then do a XOR with the ip
        final_result = []
        if self.ip and len(self.ip._coeffs) <= len(add_result):
            for index, indiv_bit in enumerate(self.ip._coeffs):
                final_result.append(indiv_bit ^ add_result[index])
        else:
            final_result = add_result
        # convert to an integer so that we can return a g3 object
        value = self.getInt(final_result)
        #print(value)
        return GF2N(value, self.n, self.ip)


    def sub(self,g2):
        sub_result = []
        # Extend the shorter array
        self_coeffs = self.getPolynomial2List()
        g2_coeffs = g2.getPolynomial2List()
        len_g1 = len(self_coeffs)
        len_g2 = len(g2_coeffs)
        difference_length = abs(len_g1 - len_g2)
        if len_g1 > len_g2:
            for zero_counter in range(difference_length):
                g2_coeffs.append(0)
        else:
            for zero_counter in range(difference_length):
                self_coeffs.append(0)
        for index, indiv_bit in enumerate(self_coeffs):
            sub_result.append(g2_coeffs[index] ^ indiv_bit)
        # Then do a XOR with the ip'
        final_result = []
        if self.ip and len(self.ip._coeffs) <= len(sub_result):
            for index, indiv_bit in enumerate(self.ip._coeffs):
                final_result.append(indiv_bit ^ sub_result[index])
        else:
            final_result = sub_result
        # convert to an integer so that we can return a g3 object
        value = self.getInt(final_result)
        return GF2N(value, self.n, self.ip)
    

    def mul(self,g2):
        self_coeffs = self.getPolynomial2List()
        g2_coeffs = g2.getPolynomial2List()
        if self.ip or g2.ip:
            try:
                modp = self.ip
            except:
                modp = g2.ip
            reduction_limit = len(modp._coeffs)
            to_append = reduction_limit - len(self_coeffs) - 1
            for i in range(to_append):
                self_coeffs.append(0)
            storage = []
            # For loop through the reference which will be self
            for iterations in range(len(g2_coeffs)):
                state = g2_coeffs[iterations]
                if iterations == 0:
                    # g2_coeffs multiplied by x^0
                    zero_array = self_coeffs
                else:
                    try:
                        if self_coeffs[-1] == 0:
                            zero_array = [0]
                            zero_array.extend(self_coeffs)
                            del zero_array[-1]
                        else:
                            zero_array = [0]
                            zero_array.extend(self_coeffs)
                            del zero_array[-1]
                            add_result = []
                            for index, indiv_bit in enumerate(zero_array):
                                add_result.append(modp._coeffs[index] ^ indiv_bit)
                            zero_array = add_result
                    except:
                        # Just shift
                        zero_array = [0]
                        zero_array.extend(self_coeffs)
                self_coeffs = zero_array
                if state == 1:
                    storage.append(zero_array)
            # Add the partial results
            mult_result = [0 for i in range(reduction_limit - 1)]
        else:
            # Standard polynomial
            reduction_limit = len(self_coeffs) + len(g2_coeffs)
            storage = []
            # For loop through the reference which will be self
            for iterations in range(len(g2_coeffs)):
                state = g2_coeffs[iterations]
                if iterations == 0:
                    zero_array = self_coeffs
                else:
                    zero_array = [0]
                    zero_array.extend(self_coeffs)
                self_coeffs = zero_array
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
        value = self.getInt(mult_result)
        return GF2N(value, self.n, self.ip)


    def deg(self):
        # Convert integer to list
        self_coeffs = self.getPolynomial2List()
        for index_coefficient, coefficient in enumerate(self_coeffs):
            if coefficient == 1:
                index_coeff = index_coefficient
        return index_coeff


    def lc(self):
        self_coeffs = self.getPolynomial2List()
        for index_coefficient, coefficient in enumerate(self_coeffs):
            if coefficient == 1:
                leading_coefficient = coefficient
        return leading_coefficient


    def div(self,g2):
        self_coeffs = self.getPolynomial2List()
        g2_coeffs = g2.getPolynomial2List()
        # Create q based on the highest power of the quotient
        q = []
        for i in range(len(self_coeffs) - len(g2_coeffs) + 1):
            q.append(0)
        q_obj = GF2N(self.getInt(q))  # Will be an empty list if the int value is 0
        r = copy.deepcopy(self)
        b = g2
        d = g2.deg()
        c = g2.lc()
        while r.deg() >= d:
            power = r.deg() - d
            coeff_power = int(r.lc()/ c)
            s = []
            for i in range(power):
                s.append(0)
            s.append(coeff_power)
            s = self.getInt(s)
            q = GF2N(s).add(q_obj)
            q_obj = q          
            sb = GF2N(s, self.n, None).mul(b)
            r = r.sub(sb)
        return q, r


    def getPolynomial2(self):
        coeffs = self.getPolynomial2List()
        poly = Polynomial2(coeffs)
        return poly

    
    def getPolynomial2List(self):
        coeffs = list(str(bin(self.x)).lstrip('0b'))
        coeffs = [ int(x) for x in coeffs ]
        #print(coeffs)
        coeffs.reverse()
        return coeffs

        
    def __str__(self):
        return str(self.x)
        # # Print based on an integer representation
        # coeffs = self.getPolynomial2List()
        # formatted_polynomial = ''
        # coeffs.reverse()
        # for index_coeff, indiv_coeff in enumerate(coeffs):
        #     if index_coeff == len(coeffs) - 1:
        #         if indiv_coeff == 1:
        #             formatted_polynomial += 'x^{}'.format(0)
        #         else:
        #             formatted_polynomial = formatted_polynomial[: -1]
        #     else:
        #         if indiv_coeff == 1:
        #             formatted_polynomial += 'x^{}+'.format(len(coeffs) - 1 - index_coeff)
        # return formatted_polynomial

    def getInt(self, coefficients):
        value = 0
        for index_coeff, indiv_coeff in enumerate(coefficients):
            value += indiv_coeff * 2 ** index_coeff
        return value

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


# print ('\nTest Submission test')
# print ('======')
# ip_glenn=Polynomial2([1,0,0,1,1])
# print ('irreducible polynomial {}'.format(ip_glenn))
# g_glenn1=GF2N(0b1101,4,ip_glenn)
# g_glenn2=GF2N(0b110,4,ip_glenn)
# print ('g_glenn1 = {}'.format(g_glenn1.getPolynomial2()))
# print ('g_glenn2 = {}'.format(g_glenn2.getPolynomial2()))
# g_glenn_result=g_glenn1.mul(g_glenn2)
# print ('g_glenn1 x g_glenn2 = {}'.format(g_glenn_result.p))


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
