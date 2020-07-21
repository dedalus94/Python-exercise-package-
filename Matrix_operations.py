class Matrix:
    """This class will create a Matrix.
    To instantiate a matrix, simply provide it formatted as nested lists:
    [[row_1], [row_2],..., [row_n]]."""
            
    def __init__(self, matrix_list=[[]]):
        
        self.matrix_list= matrix_list
        self.rows = len(matrix_list)
        self.columns = len(matrix_list[0])
        self.traspose=[]
        
    def matrix_check(self):
        "This method will check if the matrix has same number of columns and rows and if the elements are numbers"
    
        for row in self.matrix_list:
            for element in row:
                if type(element)==float:
                    pass
                if type(element)==int:
                    pass
                else: 
                    print('ERROR: {} is not a matrix. The elements of the matrix must be floats or ints'.format(self)) 
                    return False
        
        for row in self.matrix_list:             #maybe this for cycle could be changed for a vector comparison using numpy arrays?
            if len(row)==self.columns: 
                pass
            else:
                print('ERROR: {} is not a matrix. The number of columns is not the same in each row'.format(self))
                return False
        print('{} is a matrix'.format(self))
        return True
    
    def matrix_transpose(self):
        
        """This method will compute the matrix transpose. 
        the method matrix_check is called and if an error appears,
        then the input is not a matrix and the function stops"""
        
        
        if self.matrix_check()== False: 
        
            return print("Computation not possible") 
        
        else:
            pass
        
        transposed_matrix=[]
        
        
        for i in range(self.columns):
            new_row=[]                         #new_row is overwrite at each cycle, so that we do not append rows multiple times
            
            for row in self.matrix_list:       #spits out the new row 
                new_row.append(row[i])
                
            transposed_matrix.append(new_row)  #appends the new row when ready, then the other cycle starts, and new_row is overwrite
        
        self.transpose=transposed_matrix       #stores the result as ann attribute 
    
    def matrix_square(self):
        
        self.matrix_check()
        
        for row in self.matrix_list:                          
            if len(row)==len(self.matrix_list): 
                print("This is a square matrix")
                return True 
    
    def __sub__(self,other):
    
        result=Matrix()
        result.matrix_list=[]
        
        if self.columns==other.columns:
            if self.rows==other.rows:
                
                
                
                for m in range(self.rows):
                    new_row=[]
                    for l in range(self.columns):
                        add=self.matrix_list[m][l] - other.matrix_list[m][l]
                        new_row.append(add)
                    result.matrix_list.append(new_row)   
                print(result.matrix_list)            
                return result
        
            else:
                print('ERROR: incorrect dimensions')
        else:
            print('ERROR: incorrect dimensions')
        
    def __add__(self,other):
        
        
        if self.matrix_check()== False: 
        
            return print("Computation not possible")
        else: 
            pass 
        
        if other.matrix_check()== False: 
        
            return print("Computation not possible")
        else: 
            pass 
        
        result=Matrix()
        result.matrix_list=[]
        
        if self.columns==other.columns:
            if self.rows==other.rows:
                
                
                
                for m in range(self.rows):
                    new_row=[]
                    for l in range(self.columns):
                        add=self.matrix_list[m][l] + other.matrix_list[m][l]
                        new_row.append(add)
                    result.matrix_list.append(new_row)   
                print(result.matrix_list)            
                return result
        
            else:
                print('ERROR: incorrect dimensions')
        else:
            print('ERROR: incorrect dimensions')
                
        
    def __mul__(self,other):
        
        
        if self.matrix_check()== False: 
            
            return print("Computation not possible")
        
        else: 
            pass
        
        if other.matrix_check()== False: 
        
            return print("Computation not possible")
        else: 
            pass 
        
        
        result=Matrix()
        result.matrix_list=[]
        
        if self.columns==other.rows:
            for m in range(self.rows):
                
                product_new_row=[]
                for i in range(other.columns):

                    new_element=0
                    count=0
                    
                    for row in other.matrix_list: 

                        new_element+=row[i]*self.matrix_list[m][count]
                        
                        count+=1 
                        
    
                    product_new_row.append(new_element)
                result.matrix_list.append(product_new_row)
                    
            print(result.matrix_list)            
            return result 
        
        else: 
            print('ERROR: incorrect dimensions')
