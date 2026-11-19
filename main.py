def test_login(user :{_eq_}, password :{_eq_}):
    if user == "admin" and password == "1234":
        print('Login Successful')
    else:
        print('Login Failed')

test_login("admin", "1234")
test_login("user", "0000")
