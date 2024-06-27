# this function adds up from 1 to the number and gives a total. 
def sum(num):
    result = 0
    for i in range(num):
        result = result + num-i
    print(result)
  
sum(5)