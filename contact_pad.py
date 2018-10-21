#coding=utf-8
def add_contact(phone_list):
    dict_person = {}
    number = len(phone_list)
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    dict_person['name'] = name
    dict_person['phone'] = phone
    dict_person['id'] = number + 1
    phone_list.append(dict_person)
    return phone_list


def find_contact(phone_list1,contact_name):
    new_list = []
    number = len(phone_list1)
    if number == 0:
        return None
    else:
        for i in range(0,number):
            for k,value in phone_list1[i].items():
                if value == contact_name:
                    new_list.append(phone_list1[i])
        return new_list

def del_contact(phone_list,del_name):
    del_list = []
    number = len(phone_list)
    if number == 0:
        return None
    else:
        for i in range(0, number):
            for k, value in phone_list[i].items():
                if value == del_name:
                    del_list.append(phone_list.pop(i))
        return del_list


def mod_contact(phone_list,mod_name,new_name):
    # number = len(phone_list)
    # if number == 0:
    #     return None
    # else:
    #     for i in range(0, number):
    #         for k, value in phone_list[i].items():
    #             if value == mod_name:
    #                 phone_list[i]['name'] = new_name
    #                 return phone_list
    result = find_contact(phone_list,mod_name)
    if result is not None:
        for i in range(0,len(result)):
            result[i]['name'] = new_name
        return result


def main():
    phone_list =[{'id':1 ,'name':'star','phone':'13100000000'}]
    print("通讯录\n1.添加\n2.查找\n3.删除\n4.修改\n5.退出")
    operation = input("请选择操作：")
    while True:
        if operation == '1':
            add_contact(phone_list)
            print("添加成功")
            print("现在的电话本是：{}".format(phone_list))

        if operation == '2':
            contact_name = input("请输入待查找的人员姓名：")
            find_name = find_contact(phone_list,contact_name)
            if find_name == None:
                print("当前电话本为空或者未找到该人员信息，请重新输入！")
            else:
                print(find_name)

        if operation == '3':
            del_name = input("请输入待删除的人员姓名：")
            result_name = del_contact(phone_list,del_name)

            if result_name == None:
                print("当前电话本为空或者未找到该人员信息，请重新输入！")
            else:
                print("电话本删除的信息是：{}".format(result_name))
                print("当前的电话本是：{}".format(phone_list))

        if operation == '4':
            mod_name = input("请输入待修改的人员姓名：")
            new_name = input("请输入修改后的人员姓名：")
            result_name = mod_contact(phone_list,mod_name,new_name)
            if result_name == None:
                print("当前电话本为空或者未找到该人员信息，请重新输入！")
            else:
                print("当前更新后的电话本是：{}".format(phone_list))

        if operation == '5':
            break
        print("******************************************")
        print("通讯录\n1.添加\n2.查找\n3.删除\n4.修改\n5.退出")
        operation = input("请选择操作：")





if __name__ == "__main__":
    main()