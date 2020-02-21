#demo for template strings

from string import Template

def main():
    str1 = "You are watching {0} by {1}".format("Advanced Python", "Joe Marini")
    print(str1)

    # TODO: create template with placeholders - provide security
    templ =  Template("You're watching ${title}  by ${author}")
    # TODO: use the substitute method with kwargs
    str2 = templ.substitute(title="Advanced Python", author="Joe Marini")
    print(str2)

    # TODO: use the substitute method with a dictionary
    data = {
        "author": "Joe Marini",
        "title": "Advanced Python"
    }

    str3 = templ.substitute(data)
    print(str3)

if __name__=='__main__':
    main()