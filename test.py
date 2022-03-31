from exception_googler import google_problem




a = [9]
try:
    b = a[1]
except Exception as e:
    google_problem(e)
    print(e)
