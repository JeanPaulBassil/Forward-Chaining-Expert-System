from pyknow import KnowledgeEngine, Rule, Fact, AND, OR, MATCH

class Animals(KnowledgeEngine):
    """
    Animals Knowledge Engine.
    This class encapsulates the rules and logic for identifying animals based on certain facts.
    """

    @Rule(OR(
           AND(Fact('sharp teeth'), Fact('claws'), Fact('forward looking eyes')),
           Fact('eats meat')))
    def carnivore(self):
        """
        Rule to identify carnivores.
        """
        self.declare(Fact('carnivor'))
        
    @Rule(OR(Fact('hair'), Fact('gives milk')))
    def mammal(self):
        """
        Rule to identify mammals.
        """
        self.declare(Fact('mammal'))

    @Rule(Fact('mammal'),
          OR(Fact('has hooves'), Fact('chews cud')))
    def hooves(self):
        """
        Rule to identify ungulates (hoofed animals).
        """
        self.declare(Fact('ungulate'))
        
    @Rule(OR(Fact('feathers'), AND(Fact('flies'), Fact('lays eggs'))))
    def bird(self):
        """
        Rule to identify birds.
        """
        self.declare(Fact('bird'))
        
    @Rule(Fact('mammal'), Fact('carnivor'),
          Fact(color='red-brown'),
          Fact(pattern='dark spots'))
    def monkey(self):
        """
        Rule to identify a monkey.
        """
        self.declare(Fact(animal='monkey'))

    @Rule(Fact('mammal'), Fact('carnivor'),
          Fact(color='red-brown'),
          Fact(pattern='dark stripes'))
    def tiger(self):
        """
        Rule to identify a tiger.
        """
        self.declare(Fact(animal='tiger'))

    @Rule(Fact('ungulate'),
          Fact('long neck'),
          Fact('long legs'),
          Fact(pattern='dark spots'))
    def giraffe(self):
        """
        Rule to identify a giraffe.
        """
        self.declare(Fact(animal='giraffe'))

    @Rule(Fact('ungulate'),
          Fact(pattern='dark stripes'))
    def zebra(self):
        """
        Rule to identify a zebra.
        """
        self.declare(Fact(animal='zebra'))

    @Rule(Fact('bird'),
          Fact('long neck'),
          Fact('cannot fly'),
          Fact(color='black and white'))
    def ostrich(self):
        """
        Rule to identify an ostrich.
        """
        self.declare(Fact(animal='ostrich'))

    @Rule(Fact('bird'),
          Fact('swims'),
          Fact('cannot fly'),
          Fact(color='black and white'))
    def penguin(self):
        """
        Rule to identify a penguin.
        """
        self.declare(Fact(animal='penguin'))

    @Rule(Fact('bird'),
          Fact('flies well'))
    def albatross(self):
        """
        Rule to identify an albatross.
        """
        self.declare(Fact(animal='albatross'))
        
    @Rule(Fact(animal=MATCH.a))
    def print_result(self, a):
        """
        Rule to print the identified animal.
        """
        print('Animal is {}'.format(a))

    def factz(self, l):
        """
        Declare multiple facts at once.
        :param l: List of facts to be declared.
        """
        for x in l:
            self.declare(x)
