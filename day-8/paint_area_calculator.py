from math import ceil
# down rounding would be floor instead ceil

def paint_calc(height, cover, width):
    number_of_cans = (height * width) / cover
    number_of_cans_rounded=ceil(number_of_cans)
    print(f"You will need {number_of_cans_rounded} cans of paint")

test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h,width=test_w,cover=coverage)