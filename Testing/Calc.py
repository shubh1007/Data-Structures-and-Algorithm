class Math:
    def add(self, *args):
        """Adds the argument(s) together

        Returns:
            int: The sum of the arguments 
        """
        sum_ = 0
        for i in args: sum_ += i
        return sum_
    
    def subtract(self, a, b):
        """Subtracts the argument(s) together

        Returns:
            int: The difference of the arguments 
        """
        return a - b
    
    def multiply(self, *args):
        """Products the argument(s) together

        Returns:
            int: The product of the arguments 
        """
        res = 1
        for i in args: res *= i
        return res
    
    def divide(self, a, b):
        """Divides the argument(s) together

        Returns:
            float: The division of the arguments 
        """
        try:
            return a / b
        except ZeroDivisionError:
            pass
    

    
    
if __name__ == "__main__":
    m = Math()
    print(m.add(1,2,3,4,5))

    