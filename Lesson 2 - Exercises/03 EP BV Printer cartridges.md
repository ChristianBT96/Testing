### Printer cartridges
A wholesaler sells printer cartridges. The minimum order quantity is 5. There is a 20% discount for orders of 100 or more printer cartridges. You have been asked to prepare test cases using various values for the number of printer cartridges ordered.

Use black-box analysis to identify a comprehensive series of test cases:
1. Identify the corresponding equivalence partitions and propose test cases based on them
2. Use 3-value boundary value analysis to identify further test cases
3. Write down the full resulting list of test cases
4. Implement the discount calculation function in code and write the corresponding unit tests in the language and unit test framework of your choice

1. Partitions and test cases
    - Partitions
        - 5 - 99
        - 100 - MAX INT
    - Test cases
        - 50    -> no discount
        - 150   -> 20% discount
2. 
    - invalid lower
        - 0
        - 1 2 3 4 
    - invalid upper
        - 101
    - valid
        - 5 6 50 98 99 100 101
