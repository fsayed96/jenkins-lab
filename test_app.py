from app import say_hello

def test_hello():
    assert say_hello() == "Hello Jenkins!"
    print("Test passed!")

#def test_intentinal_failure():
#    assert False, "intentional failure"

#test_hello()
#test_intentinal_failure()
