# Assignment 1 for COMP2091
# Task 5: A Pivoting Die
# Written by Kun Zhang
# Aug 14, 2015
# ---------------------------------------------------------------
# import time
# ---------------------------------------------------------------
# get and check input
def get_input():
    while True:
        try:
            num = int(input('Enter the desired goal cell number: ')) # if input cannot be converted to int
        except ValueError:
            print('Incorrect value, try again')
            continue
        if num <= 0:                    # if input is less than 1
            print('Incorrect value, try again')
            continue
        else:
            break
    return num

# ---------------------------------------------------------------
# define Die class
class Die(object):

    def __init__(self):
        self.top = 3                    # status
        self.front = 2
        self.right = 1
        self.pos = 1
        self.direction = 'right'        # current direction
        self.move = self.pivot_right      # current move
        self.side = 1       # current side length
        self.cd = 1         # change direction flag

    def __str__(self):
        return 'top = %d\nfront = %d\nright = %d\npos = %d\ndirection = %s'\
               %(self.top,self.front, self.right,self.pos, self.direction)

    def update(self, pos):  # update new status
        while self.pos < pos:       # roll to pos
            for _ in range(2):      # roll twice with same side length
                self.roll(pos)
                if self.pos >= pos:
                    break
            self.side += 1

    def roll(self, p):
        t_side = 0
        while t_side < self.side:      # move side length times
            self.move()
            if self.pos >= p:
                break
            t_side += 1
        self.change_direction()         # change direction at the end

    def pivot_right(self):
        self.right, self.top = self.top, self.opposite(self.right)
        self.direction = 'right'
#        print('Right')
        self.pos += 1

    def pivot_left(self):
        self.right, self.top = self.opposite(self.top), self.right
        self.direction = 'left'
#        print('Left')
        self.pos += 1

    def pivot_forward(self):
        self.top, self.front = self.opposite(self.front), self.top
        self.direction = 'forward'   #down
#        print('Forward')
        self.pos += 1

    def pivot_backward(self):
        self.top, self.front = self.front, self.opposite(self.top)
        self.direction = 'backward'    #up
 #       print('Backward')
        self.pos += 1

    def opposite(self,n):   # find the opposite side of face
        dic = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
        return dic[n]

    def change_direction(self):     # change direction by knowing current direction
        dir = {'right': self.pivot_forward, 'forward': self.pivot_left, 'left': self.pivot_backward,\
               "backward": self.pivot_right}
        self.move = dir[self.direction]

    def answer_print(self):
        print('On cell {}, {} is at the top, {} at the front, and {} on the right.'.format(\
            self.pos, self.top, self.front, self.right))

# ---------------------------------------------------------------
if __name__ == "__main__":
    d = Die()
    position = get_input()
    d.update(position)
    d.answer_print()