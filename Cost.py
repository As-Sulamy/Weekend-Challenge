import math

def paint_cost(colors):
  base_cost = 40.00
  paint_cost = colors * 5.00
  total_before_tax = base_cost + paint_cost
  tax = total_before_tax * 0.1
  total_cost = total_before_tax + tax

  return math.ceil(total_cost)

while True:
  try:
    colors = int(input("Enter the number of colors you want to buy: "))
    if colors < 0:
      print("Invalid input. Please enter a positive integer.")
    else:
      break
  except ValueError:
    print("Invalid input. Please enter a whole number.")

# print(f"The total cost of {colors} colors is ${paint_cost(colors)}.")
# excluding tax
print(f"The total cost of {colors} colors excluding tax is ${paint_cost(colors) - math.ceil((paint_cost(colors) * 0.1))}.")
# including tax
print(f"The total cost of {colors} colors including tax is ${paint_cost(colors)}.")
# tax amount
print(f"The tax amount for {colors} colors is ${math.ceil(paint_cost(colors) * 0.1)}.")