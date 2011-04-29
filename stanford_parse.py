from stanford_parser.parser import Parser        
cls.parser = Parser()

dependencies = self.parser.parseToStanfordDependencies("Pick up the tire pallet.")

tupleResult = [(rel, gov.text, dep.text) for rel, gov, dep in dependencies.dependencies]
self.assertEqual(tupleResult, [('prt', 'Pick', 'up'),
                               ('det', 'pallet', 'the'),
                               ('nn', 'pallet', 'tire'),
                               ('dobj', 'Pick', 'pallet')])

self.assertEqual(dependencies.tagForTokenStandoff(gov), "VB")
self.assertEqual(dependencies.tagForTokenStandoff(dep), "NN")

print tupleResult