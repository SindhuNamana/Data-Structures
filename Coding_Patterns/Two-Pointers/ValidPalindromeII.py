def is_palindrome(string):
  # Replace this placeholder return statement with your code
  def check_palindrome(st, i, j):
    while i<j:
      if st[i] != st[j]:
        return False
      i+=1
      j-=1
    return True
    
  start = 0
  end = len(string)-1
  while start<end:
    if string[start] != string[end]:
      return check_palindrome(string, start+1, end) or check_palindrome(string, start, end-1)
    start+=1
    end-=1
  return True
  
#Time-Complexity = O(n)
#Explanation:
#Space-Complexity = O(1)
