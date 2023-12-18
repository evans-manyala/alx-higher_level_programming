def safe_print_division(a, b):
  """
  Attempts to divide two integers and print the result, handling various scenarios.

  Args:
      a: First integer operand.
      b: Second integer operand (divisor).

  Returns:
      The result of the division if successful, otherwise None.
  """
  try:
    result = a / b
  except ZeroDivisionError:
    result = None
  finally:
    print("Inside result:", end=" ")
    print("{:.2f}".format(result)) if result is not None else print(None)
  return result
