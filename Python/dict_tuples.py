my_dict = {
    "Speros": "(555) 555-5555",
    "Michael": "(999) 999-9999",
    "Jay": "(777) 777-7777"
}

def dict_tuple(object):
    keys = object.keys()
    values = object.values()
    my_list = zip(keys, values)
    print my_list

dict_tuple(my_dict)