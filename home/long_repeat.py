def long_repeat(line): 
  c = [] 
  if len(line) == 1: 
    longest = 1 
  else: 
    for i in range(len(line)-1): 
      if line[i] != line[i+1]: 
        c.append(1) 
      elif i == 0: 
        c.append(1) 
        c[-1] += 1 
      else: 
        c[-1] += 1 
      i += 1 
    if len(c) == 1: 
      longest = c[0] 
    elif len(c) == 0: 
      longest = 0 
    else: 
      longest = max(c) 
  return longest