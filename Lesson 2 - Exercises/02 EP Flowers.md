### Flowers
A mail-order company selling flower seeds charges 30 kr for postage and packing on all orders up to and including 150 kr value and 40 kr for orders above 150 kr value and up to and including 300 kr value. For orders above 300 kr value there is no charge for postage and packing.

If you were using equivalence partitioning to prepare test cases for the postage and packing charges:
1. What valid input partitions might you use?
2. What test case values could be inferred from said partitions?
3. With the information provided, would there be any invalid partitions?


1. test cases
    - 0.01-150 kr.
    - 150.01-300 kr.
    - 300.01 -> MAX DOUBLE kr.

2. test case values
    - 75 kr.    -> 30 kr.
    - 225 kr.   -> 40 kr.
    - 400 kr.   -> 0 kr.

3. invalid partitions
    - minus values
    - non-intergers
    - more
