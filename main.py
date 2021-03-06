import time


class Node():
    def __init__(self, coef, power: int):  
        super().__init__()
        self.coef = coef
        self.power = power
        
    def __repr__(self):
        return "{a}x^{b}".format(a=self.coef, b=self.power)

    def __eq__(self, other):
        return self.coef == other.coef and self.power == other.power 
    
        
class Polynomial():
    def __init__(self, list_of_nodes: list):
        super().__init__()
        raw_list_of_nodes = self._sort_by_addition_of_nodes_with_same_power(list_of_nodes)
        self.list_of_nodes = self._sort_by_power(raw_list_of_nodes)
        
    def print_sorted_polynomial(self):
        _str = ''
        for i, v in enumerate(self.list_of_nodes):
            if i == 0:
                _str += str(v)
            else:
                _str += ' + ' + str(v)
        print(_str)
        
    def _sort_by_addition_of_nodes_with_same_power(self, list_of_nodes: list):
        list_to_return = []
        for i, v in enumerate(list_of_nodes):
            node_has_been_added = False
            for _, node in enumerate(list_to_return):
                if v.power == node.power:
                    node.coef += v.coef
                    node_has_been_added = True
            if not node_has_been_added:
                list_to_return.append(v)
                
        return list_to_return
        
    def _sort(self, list_to_sort: list):  # in ascending order
        if len(list_to_sort) <= 1:
            return list_to_sort
        else:
            return self._sort([x for x in list_to_sort[1:] if x < list_to_sort[0]]) + \
                [list_to_sort[0]] + \
                self._sort([x for x in list_to_sort[1:] if x >= list_to_sort[0]])
    
    def _sort_by_power(self, list_of_nodes: list):
        list_of_powers = []
        for i, v in enumerate(list_of_nodes):
            list_of_powers.append(v.power)
        
        new_order_of_powers = self._sort(list_of_powers)
        new_reversed_order_of_powers = list(reversed(new_order_of_powers))
        
        new_order_of_nodes = []
        for _, v in enumerate(new_reversed_order_of_powers):
            for i, node in enumerate(list_of_nodes):
                if v == node.power:
                    new_order_of_nodes.append(node)
                    list_of_nodes.remove(node)
                    
        return new_order_of_nodes  # list of nodes, descending powers order
                                

if __name__ == "__main__":
    start = time.time()
    p = Polynomial([Node(1, 1), Node(3, 3), Node(2, 2), Node(6, 2)])
    p.print_sorted_polynomial()
    # input: 1x^1 + 3x^3 + 2x^2 + 6x^2
    # output: 3x^3 + 8x^2 + 1x^1
    print("Process time: " + str(time.time() - start))  # Process time: 0.0009