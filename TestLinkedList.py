import unittest
from LinkedList import LinkedList

class TestLLMethods(unittest.TestCase):

    def test_add(self):
        ll = LinkedList()
        for i in range(5):
            ll.ll_add(i)
        result = '[ '
        ptr = ll.head
        for i in range(ll.length - 1):
            result =  str(result) + str(ptr.value) + ', '
            ptr = ptr.next
        result = str(result) + str(ptr.value) +' ]'

        self.assertEqual( result, '[ 4, 3, 2, 1, 0 ]')

    #def test_contains(self):
    #    self.assertTrue('FOO'.isupper())
    #    self.assertFalse('Foo'.isupper())

    #def test_remove_first(self):
    #    s = 'hello world'
    #    self.assertEqual(s.split(), ['hello', 'world'])
    #    # check that s.split fails when the separator is not a string
    #    with self.assertRaises(TypeError):
    #        s.split(2)
    #def test_remove_at(self):
    #    self.assertTrue('FOO'.isupper())
    #    self.assertFalse('Foo'.isupper())

    #def test_length(self):
    #    s = 'hello world'
    #    self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
    #    with self.assertRaises(TypeError):
    #        s.split(2)

if __name__ == '__main__':
    unittest.main()
