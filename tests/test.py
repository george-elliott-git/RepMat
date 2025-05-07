import sys
sys.path.append(r'D:\RepMatProject')
import RepMat

#1. Tests on groups.py 


    #standard group creation

        #i) CYCLIC

        #cyclic_group = RepMat.Cyclic(test_elements)
        #RepMat.Display(cyclic_group)
        #Group with elements: {0, 1, 2, 3}
        #Group operation: <bound method create_Cyclic.operation of <RepMat.groups.create_Cyclic object at 0x0000028A52636A50>>
        #Traceback (most recent call last):
          #File "<pyshell#7>", line 1, in <module>
            #RepMat.Display(cyclic_group)
          #File "D:\RepMatProject\RepMat\groups.py", line 95, in Display
            #return display_group_info(group)
          #File "D:\RepMatProject\RepMat\groups.py", line 48, in display_group_info
            #print(f"Identity: {self.identity}")
        #AttributeError: 'create_Cyclic' object has no attribute 'identity'

        #ii) PERMUTATION

        


    #custom group creation

test_elements = [0, 1, 2, 3]
op = lambda a, b: (a +b) % 4
    #custom_group = RepMat.create_Group(test_elements, op)
    #-->   <RepMat.groups.create_Group object at 0x00000215BF2C7610>

    #RepMat.Display(custom_group)
        #--> Group with elements: {0, 1, 2, 3}
        #--> Group operation: <function <lambda> at 0x000001599012A8E0>
        #--> Identity: 0
        #--> Inverses: {0: 0, 1: 3, 2: 2, 3: 1}

    #RepMat.Order(new_group)
        #--> 4

    #possibly review .Optn, .Identity, and .Inverse later (if seen as useful)



#2. representations.py == representation creation


