def distinct_words(n, line):
  # transfering line to list

  lineToList = line.split("\n")
  if len(lineToList) != n:
    return "Try Again!"
  # if 1<=n<=10**5 or len(lineToList) >= 10**6:
  #   return "Try Again!"
  
  # creates two lists, listOfWords is two count distinct words and counter to count how many times each word is in line
  listOFwords = []
  counter = []
  # get distinct words from line
  for i in lineToList:
    if i not in listOFwords:
      listOFwords.append(i)
  distinct_word = len(listOFwords)
  
  # count how many times each word appears in line
  for i in lineToList:
    if i in lineToList:
      print(counter)
      counter.append(lineToList.count(i))
      lineToList.remove(i)
  return distinct_word, counter
   
