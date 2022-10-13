#!/usr/bin/python3
""" Console Module """
import cmd
import sys
import models
import json
import shlex
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, 'longitude': float
            }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        _cmd = _cls = _id = _args = ''  # initialize line elements

        # scan for general formating - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:  # parse line left to right
            pline = line[:]  # parsed line

            # isolate <class name>
            _cls = pline[:pline.find('.')]

            # isolate and validate <command>
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            # if parantheses contain arguments, parse them
            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                # partition args: (<id>, [<delim>], [<*args>])
                pline = pline.partition(', ')  # pline convert to tuple

                # isolate _id, stripping quotes
                _id = pline[0].replace('\"', '')
                # possible bug here:
                # empty quotes register as empty _id when replaced

                # if arguments exist beyond _id
                pline = pline[2].strip()  # pline is now str
                if pline:
                    # check for *args or **kwargs
                    if pline[0] == '{' and pline[-1] == '}'\
                            and type(eval(pline)) is dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
                        # _args = _args.replace('\"', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        """ Method to exit the HBNB console"""
        exit()

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        exit()

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    def do_create(self, args):
        """ Create an object of any class"""
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            args = shlex.split(args)
            new_instance = eval(args[0])()
            for i in args[1:]:
                try:
                    key = i.split("=")[0]
                    value = i.split("=")[1]
                    if hasattr(new_instance, key) is True:
                        value = value.replace("_", " ")
                        try:
                            value = eval(value)
                        except:
                            pass
                        setattr(new_instance, key, value)
                except (ValueError, IndexError):
                    pass
            new_instance.save()
            print(new_instance.id)
        except:
            print("** class doesn't exist **")
            return
        # input = args.split()
        # if not args:
        #     print("** class name missing **")
        #     return
        # elif input[0] not in HBNBCommand.classes:
        #     print("** class doesn't exist **")
        #     return
        
        # new_instance = HBNBCommand.classes[input[0]]()
        # for elem in input[1:]:
        #     elem = elem.split("=")
        #     if (len(elem) == 2):
        #         elem[1] = elem[1].replace("_", " ")

        #         if elem[1][0] != '"':
        #             try:
        #                 elem[1] = int(elem[1])
        #             except:
        #                 try:
        #                     elem[1] = float(elem[1])
        #                 except:
        #                     pass
        #         else:
        #             elem[1] = elem[1].replace('"', "")
        #         elem[0] = elem[0].replace('"', "")
        #         try:
        #             setattr(new_instance, elem[0], elem[1])
        #         except:
        #             pass
        # new_instance.save()
        # print(new_instance.id)

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """ Method to show an individual object """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_dict = storage.all(args[0])
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        try:
            value = obj_dict[key]
            print(value)
        except KeyError:
            print("** no instance found **")

        # new = args.partition(" ")
        # c_name = new[0]
        # c_id = new[2]

        # # guard against trailing args
        # if c_id and ' ' in c_id:
        #     c_id = c_id.partition(' ')[0]

        # if not c_name:
        #     print("** class name missing **")
        #     return

        # if c_name not in HBNBCommand.classes:
        #     print("** class doesn't exist **")
        #     return

        # if not c_id:
        #     print("** instance id missing **")
        #     return

        # key = c_name + "." + c_id
        # try:
        #     print(storage._FileStorage__objects[key])
        # except KeyError:
        #     print("** no instance found **")

    def help_show(self):
        """ Help information for the show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """ Destroys a specified object """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        class_id = args[1]
        storage.reload()
        obj_dict = storage.all()
        try:
            eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        key = class_name + "." + class_id
        try:
            del obj_dict[key]
        except KeyError:
            print("** no instance found **")
        storage.save()

        # new = args.partition(" ")
        # c_name = new[0]
        # c_id = new[2]
        # if c_id and ' ' in c_id:
        #     c_id = c_id.partition(' ')[0]

        # if not c_name:
        #     print("** class name missing **")
        #     return

        # if c_name not in HBNBCommand.classes:
        #     print("** class doesn't exist **")
        #     return

        # if not c_id:
        #     print("** instance id missing **")
        #     return

        # key = c_name + "." + c_id

        # try:
        #     del(storage.all()[key])
        #     storage.save()
        # except KeyError:
        #     print("** no instance found **")

    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        args = args.split(" ")
        obj_list = []
        objects = storage.all(args[0])
        try:
            if args[0] != "":
                models.classes[args[0]]
        except (KeyError, NameError):
            print("** class doesn't exist **")
            return
        try:
            for key, val in objects.items():
                obj_list.append(val)
        except:
            pass
        print(obj_list)
        # args = args.split(" ")
        # obj_list = []
        # objects = storage.all(args[0])
        # try:
        #     if args[0] != "":
        #         models.classes[args[0]]
        # except (KeyError, NameError):
        #     print("** class doesn't exist **")
        #     return
        # try:
        #     for key, val in objects.items():
        #         obj_list.append(str(val))
        # except:
        #     pass
        # print(obj_list)

    def help_all(self):
        """ Help information for the all command """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """Count current number of class instances"""
        obj_list = []
        storage.reload()
        objects = storage.all()
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print("** class doesn't exist **")
            return
        for key, val in objects.items():
            if len(args) != 0:
                if type(val) is eval(args):
                    obj_list.append(val)
            else:
                obj_list.append(val)
        print(len(obj_list))
        # count = 0
        # for k, v in storage._FileStorage__objects.items():
        #     if args == k.split('.')[0]:
        #         count += 1
        # print(count)

    def help_count(self):
        """ """
        print("Usage: count <class_name>")

    def do_update(self, args):
        """ Updates a certain object with new info """
        storage.reload()
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        obj_dict = storage.all()
        try:
            obj_value = obj_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            attr_type = type(getattr(obj_value, args[2]))
            args[3] = attr_type(args[3])
        except AttributeError:
            pass
        setattr(obj_value, args[2], args[3])
        obj_value.save()

    #     c_name = c_id = att_name = att_val = kwargs = ''

    #     # isolate cls from id/args, ex: (<cls>, delim, <id/args>)
    #     args = args.partition(" ")
    #     if args[0]:
    #         c_name = args[0]
    #     else:  # class name not present
    #         print("** class name missing **")
    #         return
    #     if c_name not in HBNBCommand.classes:  # class name invalid
    #         print("** class doesn't exist **")
    #         return

    #     # isolate id from args
    #     args = args[2].partition(" ")
    #     if args[0]:
    #         c_id = args[0]
    #     else:  # id not present
    #         print("** instance id missing **")
    #         return

    #     # generate key from class and id
    #     key = c_name + "." + c_id

    #     # determine if key is present
    #     if key not in storage.all():
    #         print("** no instance found **")
    #         return

    #     # first determine if kwargs or args
    #     if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
    #         kwargs = eval(args[2])
    #         args = []  # reformat kwargs into list, ex: [<name>, <value>, ...]
    #         for k, v in kwargs.items():
    #             args.append(k)
    #             args.append(v)
    #     else:  # isolate args
    #         args = args[2]
    #         if args and args[0] == '\"':  # check for quoted arg
    #             second_quote = args.find('\"', 1)
    #             att_name = args[1:second_quote]
    #             args = args[second_quote + 1:]

    #         args = args.partition(' ')

    #         # if att_name was not quoted arg
    #         if not att_name and args[0] != ' ':
    #             att_name = args[0]
    #         # check for quoted val arg
    #         if args[2] and args[2][0] == '\"':
    #             att_val = args[2][1:args[2].find('\"', 1)]

    #         # if att_val was not quoted arg
    #         if not att_val and args[2]:
    #             att_val = args[2].partition(' ')[0]

    #         args = [att_name, att_val]

    #     # retrieve dictionary of current objects
    #     new_dict = storage.all()[key]

    #     # iterate through attr names and values
    #     for i, att_name in enumerate(args):
    #         # block only runs on even iterations
    #         if (i % 2 == 0):
    #             att_val = args[i + 1]  # following item is value
    #             if not att_name:  # check for att_name
    #                 print("** attribute name missing **")
    #                 return
    #             if not att_val:  # check for att_value
    #                 print("** value missing **")
    #                 return
    #             # type cast as necessary
    #             if att_name in HBNBCommand.types:
    #                 att_val = HBNBCommand.types[att_name](att_val)

    #             # update dictionary with name, value pair
    #             new_dict.__dict__.update({att_name: att_val})

    #     new_dict.save()  # save updates to file

    # def help_update(self):
    #     """ Help information for the update class """
    #     print("Updates an object with new information")
    #     print("Usage: update <className> <id> <attName> <attVal>\n")

    def default(self, args):
        '''
            Catches all the function names that are not expicitly defined.
        '''
        functions = {"all": self.do_all, "update": self.do_update,
                     "show": self.do_show, "count": self.do_count,
                     "destroy": self.do_destroy, "update": self.do_update}
        args = (args.replace("(", ".").replace(")", ".")
                .replace('"', "").replace(",", "").split("."))

        try:
            cmd_arg = args[0] + " " + args[2]
            func = functions[args[1]]
            func(cmd_arg)
        except:
            print("*** Unknown syntax:", args[0])

if __name__ == "__main__":
    HBNBCommand().cmdloop()