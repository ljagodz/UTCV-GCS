import cloud_storage
bucket_name = "2018-2019"


def prompt_test_name(existing_tests):
    done = False;
    while not done:
        test_name = input("Enter test name: ")
        if test_name in existing_tests:
            print("Test found\n")
            done = True
        else:
            print("\nTest \"" + test_name + "\" not found")
            if prompt_decision("Create new test \"" + test_name + "\"?"):
                # cloud_storage.create_new_test(test_name, bucket_name)
                print("\nNew test \"" + test_name + "\" has been created")
                done = True
            else:
                print("\n")
    return test_name

def prompt_decision(question):
    decided = False
    while not decided:
        decision =  input(question + " (Y/N): ")
        if decision == "Y":
            return True
        elif decision == "N":
            return False
        else:
            print("\nUnrecognized input \"" + decision + "\"\n")


def prompt_choice(question, list):
    decided = False
    while not decided:
        choices = "("
        for i in range(len(list)):
            choices = choices + "{}".format(list[i])
            if i is not len(list)-1:
                choices = choices + ", "
        choices = choices + ")"

        decision = input(question + " " + choices)

        for i in range(len(list)):
            if decision == list[i]:
                return(i)

        print("\nUnrecognized input \"" + decision + "\"\n")


list = ["A", "faggot", "C", "D"]
prompt_choice("Pick One", list)