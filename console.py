import cmd
import shlex
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"



    def do_quit(self,arg):
        """To quit from the program"""
        return True

    def do_help_quit(self, arg):
        print("Quit is a command to exit from the program")
        return True

    def do_EFO(self,arg):
        print()

    def do_empty_line(self,arg):
        pass

    def do_create(self,arg):
        """Create a new instance"""
        if not arg:
            print("** class name missing **")
            return
        try:
            n_instance = eval(arg)()
            n_instance.save()
            print(n_instance.id)

        except NameError:
            print("** class doesn't exist **")


    def do_show(self,arg):
        """" """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            class_id = args[1]
            key = "{}.{}".format(class_name, class_id)
            obj = models.storage.all().get(key)
            if obj:
                print(obj)
            else:
                print("** no instance found **")

        except IndexError:
            if not class_name:
                print("** class name missing **")
            else:
                print("** instance id missing **")

        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self,arg):
        """ """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")

        try:
            class_name = args[0]
            class_id = args[1]
            key = "{}.{}".format(class_name, class_id)
            obj = models.storage.all().get(key)

            if obj:
                del models.storage.all()[key]
                models.storage.save()
            else:
                print("** no instance found **")

        except IndexError:
            if not class_name:
                print("** class name missing **")
            else:
                print("** instance id missing **")

        except NameError:
            print("** class doesn't exist **")

    def do_all(self,arg):
        """"""
        args = shlex.split(arg)
        cls_list = []
        if not args:
            for obj in models.storage.all().values():
                cls_list.append(str(obj))
            print(cls_list)

        else:
            try:
                class_name = args[0]
                for key, obj in models.storage.all().items():
                    if class_name == key.split('.')[0]:
                        cls_list.append(str(obj))

                    if cls_list:
                        print(cls_list)
                    else:
                        print("** class doesn't exist **")

            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            obj = models.storage.all().get(key)
            if obj:
                if len(args) >= 3:
                    attribute = args[2]
                    if len(args) >= 4:
                        value_str = args[3]
                        if hasattr(obj, attribute):
                            value = eval(value_str)
                            setattr(obj, attribute, value)
                            models.storage.save()
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** value missing **")
                else:
                    print("** attribute name missing **")
            else:
                print("** no instance found **")
        except IndexError:
            if not class_name:
                print("** class name missing **")
            else:
                print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")





if __name__ == '__main__':
    HBNBCommand().cmdloop()