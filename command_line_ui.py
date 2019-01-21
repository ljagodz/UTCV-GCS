from cloud_storage import *
from calculation import *

class UI:
    exit = False
    bucket_name = "2018_2019"
    tests = []

    def __init__(self):
        self.list_tests()
        while not self.exit:
            i = self.prompt_choice("MENU > Enter an option below:",
                          ["\t(VIEW): View data of a test in database",
                           "\t(NEW): Create a new test type in database",
                           "\t(DELETE): Delete a test from the database",
                           "\t(RUN): Run an existing test",
                           "\t(EXIT): Exit program"],
                          ["LIST", "NEW", "DELETE", "EXIT"])

            if i == 0: self.view_test()
            elif i == 1: self.new_test()
            elif i == 2: self.delete_test()
            elif i == 3: self.run_test()
            elif i == 4: self.exit = True



    def prompt_choice(question, list, code):
        decided = False
        while not decided:
            choices = "\n"
            for i in range(len(list)):
                choices = choices + list[i]

            decision = input(question + " " + choices)

            for i in range(len(code)):
                if decision == code[i]:
                    return (i)

            print("\nUnrecognized input \"" + decision + "\". Try again.\n")

    def prompt_decision(question):
        decided = False
        while not decided:
            decision = input(question + " (Y/N): ")
            if decision == "Y":
                return True
            elif decision == "N":
                return False
            else:
                print("\nUnrecognized input \"" + decision + "\"\n")

    def list_tests(self):
        self.tests  = get_blobs_with_prefix(self.bucket_name, "/description", delimiter="/")
        print('Existing Tests:\n')
        i = 0
        for test in self.tests:
            print("\t(" + i + ")" + test.name)
            i += 1

    def new_test(self):
        created = False
        while not created:
            test_name = input("(NEW) > Enter the name of a new test: ")
            if test_name is "RETURN": return
            elif test_name not in [test.name for test in self.tests]:
                # Path to description files
                local = '/localstorage/description/' + test_name + '.txt'
                cloud = '/description/' + test_name

                # Create txt description file
                open(local, 'a').close()


                if self.prompt_decision("Creating new test \"" + test_name + "\". Proceed?"):
                    # Upload generated file into description folder in cloud
                    upload_blob(self.bucket_name, local, cloud)
                    print("New test created.")
                    self.list_tests()
                    return
                else:
                    print("New test not created.\n")
            elif test_name in [test.name for test in self.tests]:
                print("Failed, test already exists. Enter RETURN to go back to MENU\n")

    def delete_test(self):
        # NOT IMPLEMENTED YET LOL #
        print("I have not programmed this path yet")

    def view_test(self):
        i = self.choose_test("Pick a test to visualize")

        # NOT IMPLEMENTED YET LOL #
        print("I have not programmed this path yet")



    def choose_test(self, question):
        #Create questions to pick a test number #
        question = question + " (0, ...," + str(len(self.tests)) + "): "
        options = ["\t(" + str(i) + ") " + self.tests[i].name for i in range(len(self.tests))]
        code = [str(i) for i in range(len(self.tests))]
        return self.prompt_choice(question, options, code)

