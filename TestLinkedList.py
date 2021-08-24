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

    def test_contains(self):
        ll = LinkedList()
        for i in range(5):
            ll.ll_add(i)
        result = ll.ll_contains(2)

        self.assertEqual( result, True )

        result = ll.ll_contains(8)
        self.assertEqual( result, False )

    def test_remove_first(self):
        ll = LinkedList()
        for i in range(5):
            ll.ll_add(i)
        ll.ll_remove_first()
        result = '[ '
        ptr = ll.head
        for i in range(ll.length - 1):
            result =  str(result) + str(ptr.value) + ', '
            ptr = ptr.next
        result = str(result) + str(ptr.value) +' ]'

        self.assertEqual( result, '[ 3, 2, 1, 0 ]')

    def test_remove_at(self):
        ll = LinkedList()
        for i in range(5):
            ll.ll_add(i)
        ll.ll_remove_at(2)
        result = '[ '
        ptr = ll.head
        for i in range(ll.length - 1):
            result =  str(result) + str(ptr.value) + ', '
            ptr = ptr.next
        result = str(result) + str(ptr.value) +' ]'

        self.assertEqual( result, '[ 4, 3, 1, 0 ]')


    def test_length(self):
        ll = LinkedList()
        for i in range(5):
            ll.ll_add(i)
        result = ll.length

        self.assertEqual( result, 5)

if __name__ == '__main__':
    unittest.main()
