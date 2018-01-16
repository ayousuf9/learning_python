#!/usr/bin/env python2.7

class Program():
    def __init__(self, *args, **kwargs):
        #self.lang = raw_input("What Language?: ")
        #self.version = float(input("Version?: "))
        #self.skill = raw_input("What skill level?: ")
        self.lang = 'Python'
        self.version = 2.7
        self.skill = 'Beginner'

    def upgrade(self):
        #new_version = float(input("What version?: "))
        new_version = 3.4
        print("We have updated the version for", self.lang)
        self.version = new_version

p1 = Program()
print(p1.version)
p1.upgrade()
print(p1.version)
