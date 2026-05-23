from app import say_hello

def test_hello():
    assert say_hello() == "Hello from Jenkins!"
    print("Test passed!")

test_hello()
