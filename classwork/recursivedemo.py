def recursive_demo (param1, spacing):
    local1 = param1 * 2
    print (spacing, "param1 is", param1, "and local1 is", local1)
    if param1<10:
        recursive_demo(param1+1, spacing+" ")
    print (spacing,"Exiting call with param1 local1", param1, local1)

recursive_demo(1,"")