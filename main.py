from animals import Animals
from pyknow import Fact

def main():
    """
    Main function to run the Animals Knowledge Engine.
    """
    ex1 = Animals()
    ex1.reset()
    ex1.factz([
        Fact(color='red-brown'),
        Fact(pattern='dark stripes'),
        Fact('sharp teeth'),
        Fact('claws'),
        Fact('forward looking eyes'),
        Fact('gives milk')
    ])
    ex1.run()
    print(ex1.facts)

if __name__ == "__main__":
    main()
