# Copyright 2022 Shanon sghull@bu.edu
# Copyright 2022 Saraja saraja@bu.edu
# Copyright 2022 Chris Kelly  cekelly@bu.edu

class Polynomial():
    def __init__(self,polynomial=()):
        self.polynomial = polynomial
        
        self.terms=[]
        N = len(polynomial)
        for i, val in enumerate(polynomial):
            #print(i,val)
            if val !=0:
                self.terms.append( (N-i-1, val) )
        poly_dict=(dict(sorted(self.terms)))
        self.terms_dict=poly_dict
        #self.terms_dict=poly_dict
        #return self.terms_dict
    
    def __str__(self):
        return str(self.terms_dict)
    def __repr__(self):
        return str(self.terms_dict)
    
    def __add__(self,second_object):
        p=self.terms_dict
        q=second_object.terms_dict

        return {k: p.get(k, 0) + q.get(k, 0) for k in set(p) | set(q)}
    def __sub__(self,second_object):
        #print(self.terms_dict)
        p=self.terms_dict
        q=second_object.terms_dict

        return {k: p.get(k, 0) - q.get(k, 0) for k in set(p) | set(q)}
        
        #return {key: self.terms_dict(key,0) - second_object.terms_dict.get(key, 0) for key in set(second_object.terms_dict) | set(self.terms_dict)}
    def eval(self,x):
        #print("i am in eval")
        p=self.terms_dict
        x_raised = []
        for key in p:
            pow = x**key
            x_raised.append(pow)
        
        coeff_list = list(p.values())
        #print(coeff_list)
        res = list(zip(coeff_list, x_raised))
        #print(res)
        term_list = []
        for elem in res:
            term_mult = elem[0]*elem[1]
            term_list.append(term_mult)
        #print(term_list)
        return sum(term_list)
    def deriv(self):
        p=self.terms_dict.items()
        result = result = {(key-1): num * key for key, num in p if num * key!=0}
        return result
    def __mul__(self,second_term):
        p1=self.terms_dict
        p2=second_term.terms_dict
        p1_coeffs = list(p1.values())
        #print("This is p1 coeffs", p1_coeffs)
        p1_exp = list(p1.keys())
        #print("This is p1 exp", p1_exp)
        p2_coeffs = list(p2.values())
        #print("This is p2 coeffs",p2_coeffs)
        p2_exp = list(p2.keys())
        #print("This is p2 exp", p2_exp)

        coeffs_prod = []
        exp_sum = []

        for item in p1_exp:
            for item2 in p2_exp:
                a = item + item2
                exp_sum.append(a)
                
        #print(exp_sum)

        for item in p1_coeffs:
            for item2 in p2_coeffs:
                x = item * (item2)
                coeffs_prod.append(x)
        #print(coeffs_prod)

        test = list(zip(exp_sum, coeffs_prod))
        return test
    def __getitem__(self,item):
        #self.org()
        return (self.terms_dict[item])
    def __setitem__(self, key, newvalue):
        self.terms_dict[key] = newvalue
        #self.org()
        return(self.terms_dict)
    def org(self):
        print("d")
        #temp = dict(sorted(self.terms_dict))
        print((sorted(self.terms_dict)))
        return(self.terms_dict)

    def __eq__(self, second_term):
        p1 = self.terms_dict
        p2 = second_term
        #p2 = second_term.terms_dict
        if p1 == p2:
            return True
        if p1 != p2:
            return False

        


def main():
    "write your test code here"
    # print('hi')
    # p1 = [6,5,3,4]
    # p2 = [6,5]
    # polynomial1 = Polynomial(p1) 
    # p1[56]=45
    # print(p1)
    # polynomial2 = Polynomial(p2)  
    # z1 = polynomial1.__add__(polynomial2)
    # z2 = polynomial1.__sub__(polynomial2)

    q = Polynomial({3,4,5})
    q[20000] = 5
    q[10000] = 1
    print(q)

    # print(z1)
    # print(z2)
    pass

if __name__=="__main__":
    main()
    p2 = [6,5]
    p = Polynomial(p2)