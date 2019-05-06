# Analysis

## Task 0
```
O(3) ~= O(1)
```
The output always be 3 lines of code. We can remove the
the statement `len_calls = len(calls)` but in the following line, I will use twice, so it's better to cache this value instead of multiple calls.
The execution time can vary depends on calls.csv file, because we are reading the last register, so we need to calculate the lenght, and to bigger number of registers, most time needs to calculate it.
The out is **Constant**.

## Task 1
```
O(1+9072(4)+ 5213(4) + 1) ~= O(n + m) ~= O(n).
```
The output depends of number of lines to read from the texts and calls csv files. In this case we have 9072 registers of texts and 5213 registers of calls. The number of statatemens will be the sum of the total inputs times 4 (for the statements inside the for loops).
The out is **Linear**.
  
## Task 2
```
O(5213(2) + 1)  ~= O(n)
```

This code is splitted in 2 functions and a loop that iterates over there.
the total number of operations dependes of the input, in this case the number of registers of calls csv file. (5213 in this example).
So the output will be:
```
O(1 + 1 + 1 + 5213(2) + 1 + 5213(2(6))) ~= O(2(5213)) ~= O(2n)
```
The order will be around 2 times the input number, **Linear**

## Task 3
### Part A
    
The code is splitted in some functions, the most execution time will be the `findAllAreaCodes` function, which depends of the input (number of calls). This function is a loop that calls 2 functions in the worst case: `isBangaloreNumber` has 2 statements and `getAreaCode` depends of the area code, in the worst case if 7 items, so the total statements are 
`2 + 7(4) + 1` in this part.

The output will be about 
```
O(5213(2 + 7(12) + 1 + 2) + 5213) ~= O(2n)
```
So is **Linear** and depends twice times the input 
  
### Part B
This part only depends of the number of input, in this example calls entries, which is iterated once with 4 statements inside in the worst case.
```
O(2 + 5213(2(2 + 1) + 1)+ 3) ~= O(n)
```
Order is **Linear**

## Task 4
Taking the worst case escenario, the output depends of the number of inputs (calls and texts) some times.
I have a for loop to iterate the solution in order to print line by line. This loop is iterated `5213+9072` times in the worst case.
To get the result I call to `getListOfNumbers` function definition four times plus a for loop that iterates the number of making calls, which in the worst case will be 5213 times with 4 statements inside.
Finallym the `getListOfNumbers` definition has 7 statements plus a for lopp that iterates a registry list that will be `5213+9072` times (the sum of both inputs).

The order will be about:
```
O((4(4 + 9072(2) + 1)) + 9072(4) + 1 + (5213+9072)) ~= O(4n + 4n + 2n) ~= O(10n)
```
Order will be **linear** 10 times the input number.
