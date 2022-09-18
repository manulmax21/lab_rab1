# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    def get_func(tag):
        tag1 = "<" + tag + ">"
        tag2 = "</" + tag + ">"
        print("<ol>")
        def func(string):
            nonlocal tag1
            nonlocal tag2
            for i in range(len(string)):
                print(tag1 + " " + string[i] + " " + tag2)
            print("</ol>")
        return func

a = input().split()
new_tag = get_func("li")
new_tag(a)

