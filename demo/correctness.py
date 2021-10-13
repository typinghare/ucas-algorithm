# iterative
def factorial_iterative(n: int) -> int:
    product = 1
    for i in range(n):
        product *= i + 1
    return product
# <Run a few iterations>
# i = 0: product_0 = 1
# i = 1: product_1 = 1 x 2
# i = 2: product_2 = 1 x 2 x 3
# i = 3: product_3 = 1 x 2 x 3 x 4
# <loop invariant> product_i = (i + 1)!
# <proof>
# initialization: product_0 = 1! = 1 (correct)
# maintenance: if product_k = (k + 1)!, product_(k+1) = (k + 2)!, because

# recursive
def factorial_recursive(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# `totally correct` = (stop) + (return correct output)
# 1. check whether stops
# 2. check the `remaining part`(`partial correctness`)
# partial correctness definition: if the algorithm receiving correct

# definiteness:unambiguous（有二义性的）
# finiteness: no finite loop
# effectiveness

# 1. Induction can be used for proving the correctness of repetitive algorithms:
#   a. iterative algorithms:
#       * Loop invariants: induction hypothesis = loop invariant = relationships between
#         the variables during loop execution.
#   b. recursive algorithms:
#       * Direct induction: hypothesis = a recursive all itself; often a case for applying
#         strong induction.
# 2. Proving that an algorithm is totally correct means:
#   a. Proving that it will terminate.
#   b. Proving that the list of actions applied to the precondition imply the postcondition.
# 3. How to prove repetitive algorithms:
#   a. iterative algorithms: use Loop invariants, Induction
#   b. recursive algorithms: use induction using as hypothesis the recursive call
