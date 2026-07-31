def func_a(message):
  print("in func_a")
  func_b("a")
  print("finishing func_a: ", message)
   
def func_b(message):
  print("in func_b")
  func_c("is")
  print("finishing func_b: ",message)

def func_c(message):
  print("in func_c")
  func_d("This")
  print("finishing func_c: ",message)


def func_d(message):
  print("in func_d")
  print("finishing func_d: ",message)


func_a("stack")