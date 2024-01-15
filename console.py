import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.amenity import Amenity

import models


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "Review": Review, "Place": Place, "Amenity": Amenity}

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def do_help(self, arg):
        """
        Command to display the list of accessible commands.
        """
        super().do_help(arg)

    def do_create(self, arg):

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

    def do_show(self, arg):
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

    def do_destroy(self, arg):
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
    # def do_destroy(self, arg):
    #     """Deletes an instance based on the class name and id"""
    #     if not arg:
    #         print("** class name missing **")
    #         return

    #     args = arg.split()

    #     if not args:
    #         print("** instance id missing **")
    #         return

    #     class_name = args[0]

    #     if class_name not in classes:
    #         print("** class doesn't exist **")
    #         return

    #     if len(args) < 2:
    #         print("** instance id missing **")
    #         return

    #     instance_id = args[1]
    #     key = "{}.{}".format(class_name, instance_id)

    #     if key not in models.storage.all():
    #         print("** no instance found **")
    #         return

    #     del models.storage.all()[key]
    #     models.storage.save()

    # def do_all(self, arg):
    #     """"""
    #     args = shlex.split(arg)
    #     cls_list = []
    #     if not args:
    #         for obj in models.storage.all().values():
    #             cls_list.append(str(obj))
    #         print(cls_list)

    #     else:
    #         try:
    #             class_name = args[0]
    #             for key, obj in models.storage.all().items():
    #                 if class_name == key.split('.')[0]:
    #                     cls_list.append(str(obj))

    #                 if cls_list:
    #                     print(cls_list)
    #                 else:
    #                     print("** class doesn't exist **")

    #         except NameError:
    #             print("** class doesn't exist **")

    #     instances = models.storage.all().values()
    #     class_instances = [instance for instance in instances
    #                        if instance.__class__.__name__ == class_name]

    #     # Print string representations of instances
    #     print([str(instance) for instance in class_instances])
    def do_all(self, arg):
        """Prints all string based on the class name"""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in classes:
            print("** class doesn't exist **")
            return

        # Retrieve all instances of the specified class
        instances = models.storage.all().values()
        class_instances = [instance for instance in instances
                           if instance.__class__.__name__ == class_name]

        # Print string representations of instances, including new IDs
        print([str(instance) for instance in class_instances])

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


if __name__ == "__main__":

    HBNBCommand().cmdloop()
