### Bank account
Suppose you have a bank account that offers variable interest rates:

- 0.5 per cent for the first 10000 kr credit
- 1 per cent for the next 10000 kr
- 1.5 per cent for the rest

If you wanted to check that the bank was handling your account correctly: 
1. What input partitions might you use?
2. What test case values could be inferred from said partitions?


1. Input partitions
    - 0 kr. (maybe)
    - 1-10000 kr.
    - 10001 - 20000 kr.
    - 20001 -> inf kr.

2. test case values
    - 0kr. (maybe)  -> 0.0%
    - 5000 kr.      -> 0.5%
    - 15000 kr.     -> 1.0%
    - 30000 kr.     -> 1.5%