#!/usr/bin/env python3
import json
import unittest

data = '''{
    "name": "bob",
    "phone": "647 704 5727"
}'''

def parse_json(message):
    content = json.loads(message)
    return content["name"]
    #return content["phone"]

#tests
class myTests(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(parse_json(data), 'bob')

print(parse_json(data))

if __name__=='__main__':
    unittest.main()
