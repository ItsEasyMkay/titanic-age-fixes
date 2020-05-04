import unittest

class testAge(unittest.TestCase):
    
     def test_minAge(self):
            self.assertEqual(age_minAgefunction(['1','2','3','20']),1)

     def test_minAge2(self):
            
            self.assertEqual(age_minAgefunction(['0','1','2','3','20']),1)
    
     def test_minAge3(self):
            
            self.assertEqual(age_minAgefunction(['-6','1','2','3','20']),1)      
    
     def test_minAge4(self):
            self.assertEqual(age_minAgefunction(['1','2','3','20','yes']),1) 

     def test_minAge5(self):
            self.assertEqual(age_minAgefunction(['1','2','3','20','#~!"£']),1)
    
     def test_minAge6(self):
            self.assertEqual(age_minAgefunction(['1','2','3','20','1000000']),1)
            
     
        
     def test_averageAge(self):             
            self.assertEqual(age_averageAgefunction(['1','2','3','20']),6.5)
    
     def test_averageAge2(self):
            self.assertEqual(age_averageAgefunction(['1','2','3','20','-6']),-1)
            
     def test_averageAge3(self):
            self.assertEqual(age_averageAgefunction(['1','2','3','20','200','10000000']),-1)

     def test_averageAge4(self):
            self.assertEqual(age_averageAgefunction(['1','2','3','20','200','yes']),6.5)
    
     def test_averageAge5(self):
            self.assertEqual(age_averageAgefunction(['1','2','3','20','200','%#~£$']),1)
    
     def test_averageAge6(self):
            self.assertEqual(age_averageAgefunction(['0','1','2','3','20','200']),6.5)
    
    
    
     def test_maxAge(self):
            self.assertEqual(age_maxAgefunction(['1','2','3','20']),20)
    
     def test_maxAge2(self):
            self.assertEqual(age_maxAgefunction(['1','2','3','20','10000000']),-1)
    
     def test_maxAge3(self):
            self.assertEqual(age_maxAgefunction(['1','2','3','20','-70']),20)
            
     def test_maxAge4(self):
            self.assertEqual(age_maxAgefunction(['1','2','3','20','#~!"£']),20)
    
     def test_maxAge5(self):
            self.assertEqual(age_maxAgefunction(['1','2','3','20','200','yes']),20)
     
     def test_maxAge6(self):
            self.assertEqual(age_maxAgefunction(['0','1','2','3','20']),20)
            

def age_minAgefunction(userList):
    

    for i in range(0, len(userList)): 
        userList[i] = float(userList[i])

    minAge = 100
    for num in userList:

        if num < minAge and num != 0 and num > 0:
            minAge = num


    print(minAge)
    return minAge

def age_maxAgefunction(userList):
    
    x = float(0)
    for i in range(0, len(userList)): 
        userList[i] = float(userList[i])

    maxAge = 0
    for num in userList:
        if num > maxAge and num < 120 and num > 0:
            maxAge = num
        if num <= 120:
            x -= 1
            return x
    print(maxAge)
    return maxAge

def age_averageAgefunction(userList):
    
    for i in range(0, len(userList)): 
        userList[i] = float(userList[i])


    sum = 0
    averageAge = 0
    x = float(0)
    for num in userList:
        sum += float(num)
        
        if(num == 0):
            x + 0
        if(num < 0): 
            x -= 1
            return x
        else:
            x += 1

    averageAge = sum/x
    print(averageAge)
    return averageAge




#input_string = input("Enter a list numbers or elements separated by space: ")
#userList = input_string.split()
#print("user list is ", userList)
#result = age_function(userList)

if __name__ == '__main__':
    unittest.main()