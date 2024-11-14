import fake_math as fk
import true_math as tr



fake_divide = fk.divide
true_divide = tr.divide

result_1 = fake_divide(69, 3)
result_2 = fake_divide(3, 0)
result_3 = true_divide(49, 7)
result_4 = true_divide(15, 0)

print(result_1)
print(result_2)
print(result_3)
print(result_4)