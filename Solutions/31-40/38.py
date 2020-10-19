def binaryToDecimal(binary): 
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal
      
  
# Driver code 
if __name__ == '__main__': 
    binary = int(input("Biner : "))
    decimal = binaryToDecimal(binary)
    print("From " + str(binary) + " convert to " + str(decimal))