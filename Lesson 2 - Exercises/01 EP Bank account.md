### Bank account
Suppose you have a bank account that offers variable interest rates:

- 0.5 per cent for the first 10000 kr credit
- 1 per cent for the next 10000 kr
- 1.5 per cent for the rest

If you wanted to check that the bank was handling your account correctly: 
1. What input partitions might you use?
2. What test case values could be inferred from said partitions?


1. Input partitions
    - 0.01-10000 kr.
    - 10000.01 - 20000 kr.
    - 20000.01 -> MAX DOUBLE kr.

2. test case values
    - 5000 kr.      -> 0.5%
    - 15000 kr.     -> 1.0%
    - 30000 kr.     -> 1.5%