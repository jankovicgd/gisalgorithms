from point import *

class kd_tree:
    def __init__(self, r=None):
        if r is None:
            r = kd_node()
        self.root = r
        self.h = 0

    def add_point(self, p):
        lvl = self.root.add_point(p)
        if self.h < lvl:
            self.h = lvl

    def __str__(self):
        return str(self.root)



class kd_node:

    def __init__(self, p=None, r=None, l=None, lvl=0):
        self.p = p
        self.r = r
        self.l = l
        self.lvl = lvl

    def add_point(self, p):
        assert isinstance(p, Point)
        if self.lvl % 2 == 0: # we are at an even level
            if p.x <= self.p.x:
                if self.l is None:
                    new_lvl = self.lvl+1
                    self.l = kd_node(p=p, lvl=new_lvl)
                    return new_lvl
                else:
                    return self.l.add_point(p)

            else:
                if self.r is None:
                    new_lvl = self.lvl + 1
                    self.r = kd_node(p=p, lvl=new_lvl)
                    return new_lvl
                else:
                    return self.r.add_point(p)

        else: # odd level
            if p.y <= self.p.y:
                if self.l is None:
                    new_lvl = self.lvl + 1
                    self.l = kd_node(p=p, lvl=new_lvl)
                    return new_lvl
                else:
                    return self.l.add_point(p)

            else:
                if self.r is None:
                    new_lvl = self.lvl + 1
                    self.r = kd_node(p=p, lvl=new_lvl)
                    return new_lvl
                else:
                    return self.r.add_point(p)


    def __str__(self, tab_num=0):

        ret_str = ""
        if self.l is not None:
            ret_str += "L: " + str(self.l)

        ret_str += str(self.p) + " lvl = " + str(self.lvl) + " "

        if self.r is not None:
            ret_str += "R: " + str(self.r)

        return  ret_str