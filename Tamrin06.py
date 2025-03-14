def to_binary(number):
    return bin(number)[2:]  # حذف '0b' از ابتدای خروجی

# دریافت ورودی از کاربر
num = int(input("یک عدد وارد کنید: "))
binary_representation = to_binary(num)
print(f"نمایش باینری: {binary_representation}")