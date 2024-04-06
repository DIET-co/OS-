# Define initial values for r1 and r2
r1_initial = 0xABEF
r2 = 0x2953

# Perform the operations as per the instructions
# 1) TST r1, r2 (AND operation but result is not written, only flags are affected)
result_tst = r1_initial & r2

# 2) CMP r1, r2 (Subtraction r1 - r2, result is not written, only flags are affected)
result_cmp = r1_initial - r2

# 3) ADD r1, r1, r2 (Addition r1 + r2, result is written back to r1)
r1_after_add = r1_initial + r2

# Define a helper function to calculate and format the CPSR flags (N, Z, C, V) based on the result of an operation
def calculate_cpsr_flags(result, operation, initial_value=0, operand=0):
    # Negative flag (N) - set if result is negative when interpreted as a two's complement signed integer
    N = (result >> 31) & 1
    
    # Zero flag (Z) - set if result is zero
    Z = 1 if result == 0 else 0
    
    # Carry flag (C) - set or cleared depending on the operation and result
    if operation == 'add':
        C = 1 if result > 0xFFFFFFFF else 0
    elif operation == 'sub':
        C = 1 if initial_value >= operand else 0
    else: # for logical operations like AND in TST, carry is not affected
        C = 'Unaffected'
    
    # Overflow flag (V) - set or cleared based on signed overflow for add or sub
    if operation in ['add', 'sub']:
        V = 1 if ((initial_value >> 31) == (operand >> 31)) and ((result >> 31) != (initial_value >> 31)) else 0
    else:
        V = 'Unaffected'
    
    return N, Z, C, V

# Calculate CPSR flags for each operation
flags_tst = calculate_cpsr_flags(result_tst, 'and')
flags_cmp = calculate_cpsr_flags(result_cmp, 'sub', r1_initial, r2)
flags_add = calculate_cpsr_flags(r1_after_add, 'add', r1_initial, r2)

(flags_tst, flags_cmp, flags_add, bin(r1_after_add))
