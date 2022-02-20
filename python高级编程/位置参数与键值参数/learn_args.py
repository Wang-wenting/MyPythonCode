# Blog: https://www.cnblogs.com/cwind/p/8996000.html


def fun(a, b, c):
    print(a, b, c)


fun(1, 2, 3)
fun(1, *[2, 3])
fun(*(1, 2, 3))
#  *-------------------------------------------------------------------------*


class Model(object):
    def __init__(self, name):
        self.name = name

    def save(self, force_update=False, force_insert=False):
        if force_update and force_insert:
             raise ValueError("Cannot perform both operations")
        if force_update:
            print("Updated an existing record")
        if force_insert:
            print("Created a new record")


class ChildModel(Model):
    def save(self, *args, **kwargs):
        if self.name=='abcd':
            super(ChildModel, self).save(*args, **kwargs)
        else:
            return None


if __name__ == '__main__':
    c = ChildModel('abcd')
    c.save(True, False)
    c.save(False, True)
    c.save(force_update=True, force_insert=False)


