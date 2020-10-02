def arithmetic_arranger(problems, flag=False):
  if len(problems) > 5:
    return 'Error: Too many problems.'

  row1 = '' 
  row2 = ''
  row3 = ''
  row4 = ''

  for i, problem in enumerate(problems):
    num1, operator, num2 = problem.split()
    length1, length2 = len(num1), len(num2)

    #checking operators
    if operator not in ['+', '-']:
      return 'Error: Operator must be \'+\' or \'-\'.'
    #checking the num type
    if not (num1.isdigit() and num2.isdigit()):
      return 'Error: Numbers must only contain digits.'
    #checking length of the numbers
    if length1 > 4 or length2 > 4:
      return 'Error: Numbers cannot be more than four digits.'

    spacing = max(length1,length2)
    result = int(num1) + int(num2) if operator == '+' else int(num1) - int(num2)

    row1 = row1 + num1.rjust(spacing+2) 
    row2 = row2 + operator + num2.rjust(spacing+1) 
    row3 = row3 + ''.rjust(spacing+2, '-') 
    row4 = row4 + str(result).rjust(spacing+2) 

    if i < len(problems) - 1:
      row1 += '    '
      row2 += '    '
      row3 += '    '
      row4 += '    '

  
  if flag:
    arranged_problems = row1 + '\n' + row2 + '\n' + row3 + '\n' + row4
  else:
    arranged_problems = row1 + '\n' + row2 + '\n' + row3  
  return arranged_problems

