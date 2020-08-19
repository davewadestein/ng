if __name__ != '__main__':
    # We ran this script, rather than importing it
    print('Run some tests before we import the module')
    assert 1 == 1
    print('OK, all is well in the world')

print('now we are in the module')

def func():
    return 45
