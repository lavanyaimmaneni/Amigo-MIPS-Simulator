from tkinter import *
from decimal import *
import math
import random


class Main:

    def __init__(self):

        self.list1 = ["r0", "at", "v0", "v1", "a0", "a1", "a2", "a3", "t0", "t1",
                      "t2", "t3", "t4", "t5", "t6", "t7", "t8", "t9", "s0", "s1",
                      "s2", "s3", "s4", "s5", "s6", "s7", "s8", "k0", "k1", "gp", "sp", "ra"]
        self.list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


    def link_with_gui(self, gui):
        self.gui = gui

    def load(self, t):
        n = len(t)
        i = 0
        flag = 0
        flag2 = 0
        check = 0
        nxt = 0
        fi = t.find('li')
        if fi > -1 and fi + 8 <= n:
            nxt = fi + 2
            if fi > 0:
                while i < fi:
                    if t[i] == ' ' and t[i] != '\t':
                        i = i + 1
                    else:
                        flag = 1
                        break
            if t[nxt] == ' ':
                check = 1
            if flag != 1 and check == 1:
                while t[nxt] == ' ':
                    nxt = nxt + 1
                if t[nxt] == '$':
                    nxt = nxt + 1
                    if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                        temp = t[nxt]
                        temp = ord(t[nxt])
                        temp1 = int(t[nxt + 1])
                        if temp == 97 and temp1 < 4:
                            idx1 = 4 + temp1
                            flag2 = 1
                        elif temp == 115 and temp1 < 9:
                            idx1 = 18 + temp1
                            flag2 = 1
                        elif temp == 116 and temp1 < 10:
                            idx1 = 8 + temp1
                            flag2 = 1
                        elif temp == 118 and temp1 < 2:
                            idx1 = 2 + temp1
                            flag2 = 1
                        else:
                            flag2 = 0
                            self.print('in line' + str(count + 1) + 'error after ' + t[nxt])
                    else:
                        self.print('error after $')
                else:
                    self.print('no registers found')
                nxt = nxt + 2
                if t[nxt] == ',':
                    nxt = nxt + 1
                    while t[nxt] == ' ':
                        nxt = nxt + 1
                    start = nxt
                    while nxt < n:
                        if ord(t[nxt]) > 47 and ord(t[nxt]) < 58:
                            flag1 = 0
                        else:
                            flag1 = 1
                            self.print('in line ' + str(count + 1) + ' expected integer after ' + t[nxt - 1])
                            break
                        nxt = nxt + 1
                    if flag1 == 0 and flag2 == 1:
                        # self.print('command accepted at line ' + str(count+1))
                        self.totalcachecalls=self.totalcachecalls+1
                        newst = t[start:n]
                        val = Decimal(newst)
                        self.list2[idx1] = val
                        self.gui.tree.item(idx1, text="", values=(self.list1[idx1], val), tag='s')
                        self.curreg1 = -1
                        self.curreg2 = -1
                        self.pipelineforaddsubload()
                        self.regwb = idx1
                else:
                    self.print('in line ' + str(count + 1) + ' expected , after register')
            else:
                self.print('in line ' + str(count + 1) + ' command not found')
        else:
            self.print('in line ' + str(count + 1) + ' instruction not found')

    def addi(self, t):
        global idx1
        n = len(t)
        i = 0
        flag = 0
        check1 = 0
        check2 = 0
        check3 = 0
        if t.find('addi') > -1 and t.find('addi') + 14 <= n:
            if t.find('addi') > 0:
                while i < t.find('addi'):
                    if t[i] != ' ':
                        flag = 1
                        break
                    i = i + 1
            if flag != 1:
                nxt = t.find('addi') + 4
                flag1 = 0
                while t[nxt] == ' ':
                    nxt = nxt + 1
                if t[nxt] == '$':
                    nxt = nxt + 1
                    if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                        temp = t[nxt]
                        temp = ord(t[nxt])
                        temp1 = int(t[nxt + 1])
                        if temp == 97 and temp1 < 5:
                            idx1 = 4 + temp1
                            check1 = 1
                        elif temp == 115 and temp1 < 9:
                            idx1 = 18 + temp1
                            check1 = 1
                        elif temp == 116 and temp1 < 9:
                            idx1 = 8 + temp1
                            check1 = 1
                        elif temp == 118 and temp1 < 3:
                            idx1 = 2 + temp1
                            check1 = 1
                        else:
                            self.print('in line ' + str(count + 1) + ' error after ' + t[nxt])
                    else:
                        self.print('in line' + str(count + 1) + ' error after 1st $')
                else:
                    self.print('in line ' + str(count + 1) + ' error after 1st comma')
                if t[nxt + 2] == ',':
                    nxt = nxt + 3
                    while t[nxt] == ' ':
                        nxt = nxt + 1
                    if t[nxt] == '$':
                        nxt = nxt + 1
                        if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(
                                t[nxt + 1]) < 10:
                            temp = t[nxt]
                            temp = ord(t[nxt])
                            temp1 = int(t[nxt + 1])
                            if temp == 97 and temp1 < 5:
                                check2 = 1
                                idx2 = 4 + temp1
                            elif temp == 115 and temp1 < 9:
                                check2 = 1
                                idx2 = 18 + temp1
                            elif temp == 116 and temp1 < 9:
                                check2 = 1
                                idx2 = 8 + temp1
                            elif temp == 118 and temp1 < 3:
                                check2 = 1
                                idx2 = 2 + temp1
                            else:
                                self.print('in line ' + str(count + 1) + ' error after ' + t[nxt])
                        else:
                            self.print('in line ' + str(count + 1) + ' error after 2nd $')
                    else:
                        self.print('in line ' + str(count + 1) + ' error after addi')
                else:
                    self.print('in line ' + str(count + 1) + ' expected , after register')
                nxt = nxt + 2
                while t[nxt] == ' ':
                    nxt = nxt + 1
                if t[nxt] == ',':
                    nxt = nxt + 1
                    while t[nxt] == ' ':
                        nxt = nxt + 1
                    start = nxt
                    while nxt < n:
                        if ord(t[nxt]) > 47 and ord(t[nxt]) < 58:
                            nxt = nxt + 1
                        else:
                            self.print('in line ' + str(count + 1) + ' expected an "integer" after 2nd comma')
                            check3 = 1
                            break
                else:
                    self.print('in line ' + str(count + 1) + ' expected "," after 2nd register')
                if check1 == 1 and check2 == 1 and check3 == 0:
                    newst = t[start:n]
                    val = Decimal(newst)
                    regwb = idx1
                    self.list2[idx1] = self.list2[idx2] + val
                    self.gui.tree.item(idx1, text="", values=(self.list1[idx1], self.list2[idx1]), tag='s')
                    # self.print('in line ' + str(count + 1) + ' command accepted')
                    self.totalcachecalls = self.totalcachecalls + 1
                    self.curreg1 = idx2
                    self.curreg2 = -1
                    self.pipelineforaddsubload()
                    self.regwb = idx1
            else:
                self.print('in line ' + str(count + 1) + ' error after addi')
        else:
            self.print('in line ' + str(count + 1) + ' command not found')

    def store(self, t):
        n = len(t)
        i = 0
        flag = 0
        nxt = 0
        check = 0
        fi = t.find('st')
        if fi > -1 and fi + 8 <= n:
            nxt = fi + 2
            if fi > 0:
                while i < fi:
                    if t[i] != ' ' and t[i] != '\t':
                        flag = 1
                        break
                    i = i + 1
            if t[nxt] == ' ' or '\t':
                check = 1
            if flag != 1 and check == 1:
                while t[nxt] == ' ':
                    nxt = nxt + 1
                if t[nxt] == '$':
                    nxt = nxt + 1
                    if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                        temp = t[nxt]
                        temp = ord(t[nxt])
                        temp1 = int(t[nxt + 1])
                        if temp == 97 and temp1 < 5:
                            flag2 = 1
                            idx1 = 4 + temp1
                        elif temp == 115 and temp1 < 9:
                            flag2 = 1
                            idx1 = 18 + temp1
                        elif temp == 116 and temp1 < 9:
                            flag2 = 2
                            idx1 = 8 + temp1
                        elif temp == 118 and temp1 < 3:
                            flag2 = 1
                            idx1 = 2 + temp1
                        else:
                            flag2 = 0
                        nxt = nxt + 2
                        if flag2 == 1:
                            if t[nxt] == ',':
                                nxt = nxt + 1
                                while t[nxt] == ' ':
                                    nxt = nxt + 1
                                start = nxt
                                while nxt < n:
                                    if ord(t[nxt]) > 47 and ord(t[nxt]) < 58:
                                        flag1 = 0
                                    else:
                                        flag1 = 1
                                        self.print(
                                            'in line ' + str(count + 1) + ' expected integer after ' + t[nxt - 1])
                                        break
                                    nxt = nxt + 1
                                if flag1 == 0:
                                    newst = t[start:n]
                                    val = Decimal(newst)
                                    regwb = idx1
                                    self.list2[idx1] = val
                                    self.gui.tree.item(idx1, text="", values=(self.list1[idx1], val), tag='s')
                                    # self.print('in line ' + str(count + 1) + ' command accepted at line ' + str(count))
                                    self.curreg1 = -1
                                    self.curreg2 = -1
                                    self.pipelineforaddsubload()
                                    self.regwb = idx1
                            else:
                                self.print('in line ' + str(count + 1) + ' expected , after register declaration')
                        else:
                            self.print('in line ' + str(count) + ' error in declaring registers')
                    else:
                        self.print('in line ' + ' error after 1st $')
                else:
                    self.print('expected $ after st')
            else:
                self.print('in line ' + str(count + 1) + ' command not found')
        else:
            self.print('in line ' + str(count + 1) + ' command cannot be accepted')

    def sub(self, t):
        check1 = 0
        check2 = 0
        check3 = 0
        n = len(t)
        i = 0
        flag = 0
        check = 0
        fi = t.find('sub')
        if fi > -1 and fi + 15 <= n:
            if fi > 0:
                while i < fi:
                    if t[i] != ' ' and t[i] != '\t':
                        flag = 1
                        break
                    i = i + 1
            nxt = fi + 3
            if t[nxt] == ' ' or t[nxt] == '\t':
                check = 1
            nxt = nxt + 1
            if flag != 1 and check == 1:
                flag1 = 0
                while t[nxt] == ' ':
                    nxt = nxt + 1
                if t[nxt] == '$':
                    nxt = nxt + 1
                    if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                        temp = t[nxt]
                        temp = ord(t[nxt])
                        temp1 = int(t[nxt + 1])
                        if temp == 97 and temp1 < 5:
                            check1 = 1
                            idx1 = 4 + temp1
                        elif temp == 115 and temp1 < 9:
                            check1 = 1
                            idx1 = 18 + temp1
                        elif temp == 116 and temp1 < 9:
                            check1 = 1
                            idx1 = 8 + temp1
                        elif temp == 118 and temp1 < 3:
                            check1 = 1
                            idx1 = 2 + temp1
                        else:
                            self.print('in line ' + str(count + 1) + ' error after ' + t[nxt - 1])
                    else:
                        self.print('in line ' + str(count + 1) + ' error after 1st $')
                else:
                    self.print('in line ' + str(count + 1) + ' error after command')
                nxt = nxt + 2
                if t[nxt] == ',':
                    nxt = nxt + 1
                    while t[nxt] == ' ':
                        nxt = nxt + 1
                    if t[nxt] == '$':
                        nxt = nxt + 1
                        if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                            temp = t[nxt]
                            temp = ord(t[nxt])
                            temp1 = int(t[nxt + 1])
                            if temp == 97 and temp1 < 5:
                                check2 = 1
                                idx2 = 4 + temp1
                            elif temp == 115 and temp1 < 9:
                                check2 = 1
                                idx2 = 18 + temp1
                            elif temp == 116 and temp1 < 9:
                                check2 = 1
                                idx2 = 8 + temp1
                            elif temp == 118 and temp1 < 3:
                                check2 = 1
                                idx2 = 2 + temp1
                            else:
                                self.print('n line ' + str(count + 1) + ' error after ' + t[nxt - 1])
                        else:
                            self.print('in line ' + str(count + 1) + ' error after 2nd $')
                    else:
                        self.print('in line ' + str(count + 1) + ' error after 1st comma')
                else:
                    self.print('in line ' + str(count + 1) + ' expected , after ' + t[nxt - 1])
                nxt = nxt + 2
                if t[nxt] == ',':
                    nxt = nxt + 1
                    while t[nxt] == ' ':
                        nxt = nxt + 1
                    if t[nxt] == '$':
                        nxt = nxt + 1
                        if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                            temp = t[nxt]
                            temp = ord(t[nxt])
                            temp1 = int(t[nxt + 1])
                            if temp == 97 and temp1 < 5:
                                check3 = 1
                                idx3 = 4 + temp1
                            elif temp == 115 and temp1 < 9:
                                check3 = 1
                                idx3 = 18 + temp1
                            elif temp == 116 and temp1 < 9:
                                check3 = 1
                                idx3 = 8 + temp1
                            elif temp == 118 and temp1 < 3:
                                check3 = 1
                                idx3 = 2 + temp1
                            else:
                                self.print('in line ' + str(count + 1) + ' error after ' + t[nxt])
                        else:
                            self.print('in line ' + str(count + 1) + ' error after 3rd $')
                    else:
                        self.print('in line ' + str(count + 1) + ' error after 2nd comma')
                else:
                    self.print('in line ' + str(count + 1) + ' expected , after ' + t[nxt - 1])
                if check1 == 1 and check2 == 1 and check3 == 1:
                    self.list2[idx1] = self.list2[idx2] - self.list2[idx3]
                    self.gui.tree.item(idx1, text="", values=(self.list1[idx1], self.list2[idx1]), tag='s')
                    # self.print('line ' + str(count + 1) + ' command accepted')
                    self.totalcachecalls = self.totalcachecalls + 2
                    self.curreg1 = idx2
                    self.curreg2 = idx3
                    self.pipelineforaddsubload()
                    self.regwb = idx1
            else:
                self.print('in line ' + str(count + 1) + ' command not found')
        else:
            self.print('in line ' + str(count + 1) + ' error at line-')

    def add(self, t):
        n = len(t)
        i = 0
        flag = 0
        check1 = 0
        check2 = 0
        check3 = 0
        check = 0
        fi = t.find('add')
        if fi > -1 and fi + 15 <= n:
            if fi > 0:
                while i < t.find('add'):
                    if t[i] != ' ' and t[i] != '\t':
                        flag = 1
                        break
                    i = i + 1
            nxt = fi + 3
            if t[nxt] == ' ' or t[nxt] == '\t':
                check = 1
            if flag != 1 and check == 1:
                flag1 = 0
                while t[nxt] == ' ':
                    nxt = nxt + 1
                if t[nxt] == '$':
                    nxt = nxt + 1
                    if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                        temp = t[nxt]
                        temp = ord(t[nxt])
                        temp1 = int(t[nxt + 1])
                        if temp == 97 and temp1 < 5:
                            check1 = 1
                            idx1 = 4 + temp1
                        elif temp == 115 and temp1 < 9:
                            check1 = 1
                            idx1 = 18 + temp1
                        elif temp == 116 and temp1 < 9:
                            check1 = 1
                            idx1 = 8 + temp1
                        elif temp == 118 and temp1 < 3:
                            check1 = 1
                            idx1 = 2 + temp1
                        else:
                            self.print('in line ' + str(count + 1) + ' error after ' + t[nxt])
                    else:
                        self.print('in line ' + str(count + 1) + ' error after 1st $')
                else:
                    self.print('in line' + str(count + 1) + ' error after command')
                nxt = nxt + 2
                if t[nxt] == ',':
                    nxt = nxt + 1
                    while t[nxt] == ' ':
                        nxt = nxt + 1
                    if t[nxt] == '$':
                        nxt = nxt + 1
                        if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                            temp = t[nxt]
                            temp = ord(t[nxt])
                            temp1 = int(t[nxt + 1])
                            if temp == 97 and temp1 < 5:
                                check2 = 1
                                idx2 = 4 + temp1
                            elif temp == 115 and temp1 < 9:
                                check2 = 1
                                idx2 = 18 + temp1
                            elif temp == 116 and temp1 < 9:
                                check2 = 1
                                idx2 = 8 + temp1
                            elif temp == 118 and temp1 < 3:
                                check2 = 1
                                idx2 = 2 + temp1
                            else:
                                self.print('in line ' + str(count + 1) + ' error after ' + t[nxt])
                        else:
                            self.print('in line ' + str(count + 1) + ' error after 2nd $')
                    else:
                        self.print('in line ' + str(count + 1) + ' error after 1st comma')
                else:
                    self.print('in line ' + str(count + 1) + ' expected , after ' + t[nxt - 1])
                nxt = nxt + 2
                if t[nxt] == ',':
                    nxt = nxt + 1
                    while t[nxt] == ' ':
                        nxt = nxt + 1
                    if t[nxt] == '$':
                        nxt = nxt + 1
                        if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                            temp = t[nxt]
                            temp = ord(t[nxt])
                            temp1 = int(t[nxt + 1])
                            if temp == 97 and temp1 < 5:
                                check3 = 1
                                idx3 = 4 + temp1
                            elif temp == 115 and temp1 < 9:
                                check3 = 1
                                idx3 = 18 + temp1
                            elif temp == 116 and temp1 < 9:
                                check3 = 1
                                idx3 = 8 + temp1
                            elif temp == 118 and temp1 < 3:
                                check3 = 1
                                idx3 = 2 + temp1
                            else:
                                self.print('in line ' + str(count + 1) + ' error after ' + t[nxt])
                        else:
                            self.print('in line ' + str(count + 1) + ' error after 3rd $')
                    else:
                        self.print('in line ' + str(count + 1) + ' error after 2nd comma')
                    if check1 == 1 and check2 == 1 and check3 == 1:
                        self.list2[idx1] = self.list2[idx2] + self.list2[idx3]
                        self.totalcachecalls = self.totalcachecalls + 2
                        self.curreg1 = idx2
                        self.curreg2 = idx3
                        # function will be called here
                        self.pipelineforaddsubload()
                        self.regwb = idx1
                        # self.print(str(regwb))
                        # self.print(str(curreg1))
                        # self.print(str(curreg2))
                        self.gui.tree.item(idx1, text="", values=(self.list1[idx1], self.list2[idx1]), tag='s')
                        # self.print('line ' + str(count + 1) + ' command accepted')
                else:
                    self.print(' in line ' + str(count) + 'expected , after ' + t[nxt - 1])
            else:
                self.print('in line ' + str(count + 1) + 'command not found')
        else:
            self.print('in line ' + str(count + 1) + ' command not found')

    def jump(self, t, k):
        n = len(t)
        i = 0
        flag = 0
        flag2 = 0
        flag3 = 0
        nxt = 0
        fi = t.find('j')
        if fi > -1 and fi + 3 <= n:
            nxt = fi + 1
            if fi > 0:
                while i < fi:
                    if t[i] == ' ':
                        i = i + 1
                    else:
                        flag = 1
                        break
            if t[nxt] == ' ' or t[nxt] == '\t':
                flag3 = 1
            nxt = nxt + 1
            if flag != 1 and flag3 == 1:
                while t[nxt] == ' ' or t[nxt] == '\t':
                    nxt = nxt + 1
                new = t[nxt:n]
                i = 0
                while i < len(k):
                    if k[i].find(new) > -1:
                        fin = k[i].find(new) + len(new)
                        if len(k[i]) > fin:
                            if k[i][fin] == ':':
                                flag2 = 1
                                break
                    i = i + 1
                if flag2 == 1:
                    # self.print('line ' + str(count + 1) + ' command accepted and jumped to instruction ' + str(i + 1))
                    self.curreg1=-1
                    self.curreg2=-1
                    self.branchworks=1
                    self.pipelineforbranches()
                    self.regwb=-10
                    return i - 1
                else:
                    self.print('in line ' + str(count + 1) + 'label of command not found')
            else:
                self.print('in line ' + str(count + 1) + ' command not found')
        else:
            self.print('sorry')

    def bne(self, t, k):
        n = len(t)
        i = 0
        flag = 0
        flag1 = 0
        flag2 = 0
        flag3 = 0
        check1 = 0
        check2 = 0
        check3 = 0
        nxt = 0
        n1 = len(k)
        fi = t.find('bne')
        if fi > -1 and fi + 13 <= n:
            nxt = fi + 3
            if fi > 0:
                while i < fi:
                    if t[i] == ' ' or t[i] == '\t':
                        i = i + 1
                    else:
                        flag = 1
                        break
            if t[nxt] == ' ' or t[nxt] == '\t':
                flag3 = 1
            nxt = nxt + 1
            if flag != 1 and flag3 == 1:
                while t[nxt] == ' ' or t[nxt] == '\t':
                    nxt = nxt + 1
                if t[nxt] == '$':
                    nxt = nxt + 1
                    if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                        temp = t[nxt]
                        temp = ord(t[nxt])
                        temp1 = int(t[nxt + 1])
                        if temp == 97 and temp1 < 5:
                            check1 = 1
                            idx1 = 4 + temp1
                        elif temp == 115 and temp1 < 9:
                            check1 = 1
                            idx1 = 18 + temp1
                        elif temp == 116 and temp1 < 9:
                            check1 = 1
                            idx1 = 8 + temp1
                        elif temp == 118 and temp1 < 3:
                            check1 = 1
                            idx1 = 2 + temp1
                        else:
                            self.gui.output.insert("insert", '\nin line ' + 'error after ' + t[nxt - 1])
                    else:
                        self.gui.output.insert("insert", '\nin line ' + str(count + 1) + ' error after $')
                else:
                    self.gui.output.insert("insert", '\nin line ' + str(count + 1) + ' expected $ after command')
            nxt = nxt + 2
            if t[nxt] == ',':
                nxt = nxt + 1
                while t[nxt] == ' ':
                    nxt = nxt + 1
                if t[nxt] == '$':
                    nxt = nxt + 1
                    if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                        temp = t[nxt]
                        temp = ord(t[nxt])
                        temp1 = int(t[nxt + 1])
                        if temp == 97 and temp1 < 5:
                            check2 = 1
                            idx2 = 4 + temp1
                        elif temp == 115 and temp1 < 9:
                            check2 = 1
                            idx2 = 18 + temp1
                        elif temp == 116 and temp1 < 9:
                            check2 = 1
                            idx2 = 8 + temp1
                        elif temp == 118 and temp1 < 3:
                            check2 = 1
                            idx2 = 2 + temp1
                        else:
                            self.print('in line ' + str(count + 1) + ' error after ' + t[nxt - 1])
                    else:
                        self.print('in line ' + str(count + 1) + ' error after 2nd $')
                else:
                    self.print('line ' + str(count + 1) + ' error after 1st comma')
            else:
                self.print('in line ' + str(count + 1) + ' expected , after ' + t[nxt - 1])
            nxt = nxt + 2
            if t[nxt] == ',':
                nxt = nxt + 1
                while t[nxt] == ' ' or t[nxt] == '\t':
                    nxt = nxt + 1
                new = t[nxt:n]
                i = 0
                while i < n1:
                    if k[i].find(new) > -1:
                        fin = k[i].find(new) + len(new)
                        if len(k[i]) > fin:
                            if k[i][fin] == ':' and check1 == 1 and check2 == 1:
                                flag2 = 1
                                break
                    i = i + 1
                if flag2 == 1:
                    # self.print('in line ' + str(count + 1) + ' command accepted and jumped to instruction ' + str(i + 1))
                    self.totalcachecalls = self.totalcachecalls + 2
                    self.curreg1=idx1
                    self.curreg2=idx2
                    if self.list2[idx1] != self.list2[idx2]:
                        self.branchworks=1
                        self.pipelineforbranches()
                        self.regwb = -10
                        return i - 1
                    else:
                        self.branchworks=0
                        self.pipelineforbranches()
                        self.regwb = -10
                        return count

                else:
                    self.print('in line ' + str(count + 1) + ' label of command not found')
            else:
                self.print('in line ' + str(count + 1) + ' expected , after 2nd register')
        else:
            self.print('in line ' + str(count + 1) + ' command not found')

    def slt(self, t, k):
        n = len(t)
        i = 0
        flag = 0
        flag1 = 0
        flag2 = 0
        flag3 = 0
        check1 = 0
        check2 = 0
        check3 = 0
        nxt = 0
        n1 = len(k)
        fi = t.find('slt')
        if fi > -1 and fi + 13 <= n:
            nxt = fi + 3
            if fi > 0:
                while i < fi:
                    if t[i] == ' ' or t[i] == '\t':
                        i = i + 1
                    else:
                        flag = 1
                        break
            if t[nxt] == ' ' or t[nxt] == '\t':
                flag3 = 1
            nxt = nxt + 1
            if flag != 1 and flag3 == 1:
                while t[nxt] == ' ' or t[nxt] == '\t':
                    nxt = nxt + 1
                if t[nxt] == '$':
                    nxt = nxt + 1
                    if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                        temp = t[nxt]
                        temp = ord(t[nxt])
                        temp1 = int(t[nxt + 1])
                        if temp == 97 and temp1 < 5:
                            check1 = 1
                            idx1 = 4 + temp1
                        elif temp == 115 and temp1 < 9:
                            check1 = 1
                            idx1 = 18 + temp1
                        elif temp == 116 and temp1 < 9:
                            check1 = 1
                            idx1 = 8 + temp1
                        elif temp == 118 and temp1 < 3:
                            check1 = 1
                            idx1 = 2 + temp1
                        else:
                            self.gui.output.insert("insert", '\nin line ' + 'error after ' + t[nxt - 1])
                    else:
                        self.gui.output.insert("insert", '\nin line ' + str(count + 1) + ' error after $')
                else:
                    self.gui.output.insert("insert", '\nin line ' + str(count + 1) + ' expected $ after command')
            nxt = nxt + 2
            if t[nxt] == ',':
                nxt = nxt + 1
                while t[nxt] == ' ':
                    nxt = nxt + 1
                if t[nxt] == '$':
                    nxt = nxt + 1
                    if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                        temp = t[nxt]
                        temp = ord(t[nxt])
                        temp1 = int(t[nxt + 1])
                        if temp == 97 and temp1 < 5:
                            check2 = 1
                            idx2 = 4 + temp1
                        elif temp == 115 and temp1 < 9:
                            check2 = 1
                            idx2 = 18 + temp1
                        elif temp == 116 and temp1 < 9:
                            check2 = 1
                            idx2 = 8 + temp1
                        elif temp == 118 and temp1 < 3:
                            check2 = 1
                            idx2 = 2 + temp1
                        else:
                            self.print('in line ' + str(count + 1) + ' error after ' + t[nxt - 1])
                    else:
                        self.print('in line ' + str(count + 1) + ' error after 2nd $')
                else:
                    self.print('line ' + str(count + 1) + ' error after 1st comma')
            else:
                self.print('in line ' + str(count + 1) + ' expected , after ' + t[nxt - 1])
            nxt = nxt + 2
            if t[nxt] == ',':
                nxt = nxt + 1
                while t[nxt] == ' ' or t[nxt] == '\t':
                    nxt = nxt + 1
                new = t[nxt:n]
                i = 0
                while i < n1:
                    if k[i].find(new) > -1:
                        fin = k[i].find(new) + len(new)
                        if len(k[i]) > fin:
                            if k[i][fin] == ':' and check1 == 1 and check2 == 1:
                                flag2 = 1
                                break
                    i = i + 1
                if flag2 == 1:
                    # self.print('in line ' + str(count + 1) + ' command accepted and jumped to instruction ' + str(i + 1))
                    self.totalcachecalls = self.totalcachecalls + 2
                    self.curreg1=idx1
                    self.curreg2=idx2
                    if self.list2[idx1] < self.list2[idx2]:
                        self.branchworks=1
                        self.pipelineforbranches()
                        self.regwb=-10
                        return i - 1
                    else:
                        self.branchworks=0
                        self.pipelineforbranches()
                        self.regwb=-10
                        return count
                else:
                    self.print('in line ' + str(count + 1) + ' label of command not found')
            else:
                self.print('in line ' + str(count + 1) + ' expected , after 2nd register')
        else:
            self.print('in line ' + str(count + 1) + ' command not found')

    global count
    count = 0

    def print(self, str):
        self.gui.output.insert("insert", '\n' + str)

    def print1(self, str):
        self.gui.t.insert("insert",'\n'+ str)

    def print2(self, str):
        self.gui.t2.insert("insert",'\n'+  str)

    def print3(self, str):
        self.gui.t3.insert("insert", '\n'+str)

    # --------------------------------------------------------------------------------------------------------

    def cprint1(self, str):
        self.gui.ct.insert("insert",'\n'+ str)

    def cprint2(self, str):
        self.gui.ct2.insert("insert",'\n'+  str)

    def cprint3(self, str):
        self.gui.ct3.insert("insert", '\n'+str)

    # --------------------------------------------------------------------------------------------------------

    def run(self):

        self.gui.notebook.select(self.gui.ctFrame)
        self.gui.t.delete(1.0, END)
        self.gui.t2.delete(1.0, END)
        self.gui.t3.delete(1.0, END)

        self.stallat = []
        self.noofstalls = []
        self.county1 = 0
        self.regwb = -10
        self.clock = 0
        self.curreg1 = -1
        self.curreg2 = -1
        self.datafor = self.gui.forwarding.get()
        self.county2 = 1
        self.county3 = 2
        self.county4 = 3
        self.county5 = 4
        self.county = 0
        self.stall = 0
        self.nornistcount=0
        self.branchinstcount=0
        self.branchworks=0
        self.cachemiss=0
        self.totalcachecalls=0
        self.noofindexbits=self.gui.IndexBits.get()
        self.noofoffsetbits=3
        self.assocoativity=self.gui.assoc.get()
        self.isload=0
        self.L2=math.pow(2,self.noofindexbits)*self.assocoativity
        self.address=0
        self.L1cache=[0,0,0,0]
        self.L2cache=[]
        iii=0
        while iii<self.L2 :
            self.L2cache.append(0)
            iii=iii+1

        # self.print('\n---------running--------------\n')
        self.gui.save()

        self.gui.load()

        for i in range(0, 32):
            self.list2[i] = 0

        self.linstr = self.gui.text.get("1.0", END).splitlines()
        linstr = self.gui.text.get("1.0", END).splitlines()

        gth = len(linstr)
        global count
        count = 0
       

        # self.print("--------------Running--------------------\n")

        while count < gth:
            if linstr[count].find('li') > -1:
                self.load(linstr[count])
            elif linstr[count].find('sub') > -1:
                self.sub(linstr[count])
            elif linstr[count].find('addi') > -1:
                self.addi(linstr[count])
            elif linstr[count].find('add') > -1:
                self.add(linstr[count])
            elif linstr[count].find('j') > -1:
                count = self.jump(linstr[count], linstr)
            elif linstr[count].find('bne') > -1:
                count = self.bne(linstr[count], linstr)
            elif linstr[count].find('slt') > -1:
                count = self.slt(linstr[count], linstr)
            elif linstr[count].find('lw') > -1 :
                self.loadword(linstr[count])
            elif linstr[count] == '':
                pass
            elif linstr[count][len(linstr[count]) - 1] == ':':
                pass
                # self.gui.output.insert("insert", '\nline ' + str(count + 1) + ' command accepted')
            elif linstr[count].find('.') > -1:
                ctr = 0
                while ctr < linstr[count].find('.'):
                    if linstr[count][ctr] == ' ' or linstr[count][ctr] == '\t':
                        pass
                    else:
                        self.gui.output.insert('insert', 'in line ' + str(count + 1) + ' instruction not found ')
                        break
                    ctr = ctr + 1
            elif linstr[count].find('#') > -1:
                ctr = 0
                while ctr < linstr[count].find('#'):
                    if linstr[count][ctr] == ' ' or linstr[count][ctr] == '\t':
                        pass
                    else:
                        self.gui.output.insert('insert', 'in line ' + str(count + 1) + ' instrucion not found')
                        break
                    ctr = ctr + 1
            elif linstr[count].find('st') > -1:
                self.store(linstr[count])
            else:
                self.gui.output.insert("insert", '\ninstruction not found at line ' + str(count + 1))
            count = count + 1

            # self.print("\n--------------Terminated----------------\n")

        # self.print('\n---------terminated-----------\n')
        self.print1('Total number of instructions executed are '+str(self.nornistcount))
        self.print1('The time taken to execute is ' + str(self.clock)+' cycles')
        cpi=self.clock/self.nornistcount
        self.print1('CPI= '+str(cpi))
        self.print2('the no of stalls are ' + str(self.stall))
        self.printthestalls()
        self.cprint1('The no of stalls are :  '+str(self.stall))
        ppppp=self.cachemiss/self.totalcachecalls
        self.cprint2('Cache Miss Rate = '+str(ppppp))
        self.cprint3('Cycles Per Instruction (CPI) = '+str(cpi))

    def pipelineforaddsubload(self):
        if self.isload==0 :
            memstages=1
        else:
            memstages=self.cache(self.address)

        if self.datafor == 0:
            self.county1 = self.county1 + 1
            if self.curreg2 == self.regwb or self.curreg1 == self.regwb:
                self.county2 = self.county5
                nost = self.county2 - self.county1 - 2
                self.stall = self.stall + nost
            else:
                self.county2 = self.county2 + 1
                nost = self.county2 - self.county1 - 1
                self.stall = self.stall + nost
        else:
            self.county1 = self.county1 + 1
            if self.curreg2 == self.regwb or self.curreg1 == self.regwb:
                self.county2 = self.county4
                nost = self.county2 - self.county1 - 2
                self.stall = self.stall + nost
            else:
                self.county2 = self.county2 + 1
                nost = self.county2 - self.county1 - 1
                self.stall = self.stall + nost
        self.county3 = self.county2 + 1
        if self.county3 >= self.county4 :
            self.county4=self.county3+memstages
        else :
            self.county4=self.county4+memstages
            nost=self.county4-self.county3-1
            self.stall=self.stall+nost
        self.county5 = self.county4 + 1
        if self.clock < self.county5:
            self.clock = self.county5
        if nost > 0:
            self.stallat.append(count + 1)
            self.noofstalls.append(nost)
        self.nornistcount=self.nornistcount+1
        #self.print3('done for add')
    def pipelineforbranches(self):
        if self.datafor == 0:
            self.county1 = self.county1 + 1
            if self.curreg2 == self.regwb or self.curreg1 == self.regwb:
                self.county2 = self.county5
                nost = self.county2 - self.county1 - 2
                self.stall = self.stall + nost
            else:
                self.county2 = self.county2 + 1
                nost = self.county2 - self.county1 - 1
                self.stall = self.stall + nost
        else:
            self.county1 = self.county1 + 1
            if self.curreg2 == self.regwb or self.curreg1 == self.regwb:
                self.county2 = self.county4
                nost = self.county2 - self.county1 - 2
                self.stall = self.stall + nost
            else:
                self.county2 = self.county2 + 1
                nost = self.county2 - self.county1 - 1
                self.stall = self.stall + nost
        self.county3 = self.county2 + 1
        self.county4 = self.county3 + 1
        self.county5 = self.county4 + 1
        if self.branchworks==1 :
            self.county1=self.county2
            self.county2=self.county2+1
        else :
            self.county1=self.county1+1
            if self.county1==self.county2 :
                self.county2=self.county2+1
        if self.clock < self.county5:
            self.clock = self.county5
        if nost > 0:
            self.stallat.append(count + 1)
            self.noofstalls.append(nost)

        self.stallat.append(count+2)
        self.noofstalls.append(1)
        self.stall=self.stall+1
        self.nornistcount=self.nornistcount+1
        #self.print3('done')


    def printthestalls(self):
        lissize = len(self.noofstalls)
        ppq = 0
        while ppq < lissize:
            self.print3('there are ' + str(self.noofstalls[ppq]) + ' stalls in instruction ' + str(self.stallat[ppq])  )
            ppq = ppq + 1
    def cache(self,address) :
        if self.L1cache.count(address) > 0 :
            return 2
        elif self.L2cache.count(address) > 0 :
            indd=self.L2cache.index(address)
            indd1=random.randint(0,4)
            self.L2cache[indd]=self.L1cache[indd1]
            self.L1cache[indd1]=address
            return 6
        else :
            self.cachemiss=self.cachemiss+1
            indd=random.randint(0,4)
            if self.L1cache[indd] == 0 :
                self.L1cache[indd]=address
            else :
                indd1=self.L1cache[indd]
                self.L1cache[indd]=address
                indd=random.randint(0,self.L2)
                self.L2cache[indd]=indd1
            return 106
    def loadword(self,t):
     lengtt=len(t)
     flag1=0
     flag3=0
     if t.find('lw')>-1 and lengtt >=13:
        k=t.find('lw')
        nxt=k
        if k >0 :
         while i<k :
            if t[i] !=' ' or t[i]!='\t' :
                flag=1
            i=i+1
        if flag1==0 :
         nxt=nxt+2
         if t[nxt]==' ' :
            nxt=nxt+1
            while t[nxt]==' ' :
                nxt=nxt+1
            if t[nxt] == '$':
                    nxt = nxt + 1
                    if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                        temp = t[nxt]
                        temp = ord(t[nxt])
                        temp1 = int(t[nxt + 1])
                        if temp == 97 and temp1 < 4:
                            idx1 = 4 + temp1
                            flag2 = 1
                        elif temp == 115 and temp1 < 9:
                            idx1 = 18 + temp1
                            flag2 = 1
                        elif temp == 116 and temp1 < 10:
                            idx1 = 8 + temp1
                            flag2 = 1
                        elif temp == 118 and temp1 < 2:
                            idx1 = 2 + temp1
                            flag2 = 1
                        else:
                            flag2 = 0
                            #self.print('in line' + str(count + 1) + 'error after ' + t[nxt])
                    else:
                        print('error after $')
            else:
                    print('no registers found')
            nxt = nxt + 2
            while t[nxt]==' ' :
                nxt=nxt+1
            if t[nxt]==',' :
                nxt=nxt+1
                while t[nxt]==' ':
                    nxt=nxt+1
                while t[nxt]!='(':
                        if ord(t[nxt])>47 and ord(t[nxt])<58 :
                            st=nxt
                            nxt=nxt+1
                        else :
                            flag3=1
                            break
                lttt=nxt-st
                jj=0
                numb=0
                while jj<lttt :
                    ctt1=ord(t[st+jj])-48
                    if lttt>1 :
                        ppp=jj
                        while ppp<lttt-1 :
                            ctt1=ctt1*10
                            ppp=ppp+1
                    numb=numb+ctt1
                    jj=jj+1
                print('the number if'+str(numb))
                nxt=nxt+1
                if t[nxt] == '$':
                    nxt = nxt + 1
                    if (t[nxt] == 's' or t[nxt] == 't' or t[nxt] == 'a' or t[nxt] == 'v') and int(t[nxt + 1]) < 10:
                        temp = t[nxt]
                        temp = ord(t[nxt])
                        temp1 = int(t[nxt + 1])
                        if temp == 97 and temp1 < 4:
                            idx1 = 4 + temp1
                            flag4 = 1
                        elif temp == 115 and temp1 < 9:
                            idx1 = 18 + temp1
                            flag4 = 1
                        elif temp == 116 and temp1 < 10:
                            idx1 = 8 + temp1
                            flag4 = 1
                        elif temp == 118 and temp1 < 2:
                            idx1 = 2 + temp1
                            flag4 = 1
                        else:
                            flag4 = 0
                            #self.print('in line' + str(count + 1) + 'error after ' + t[nxt])
                    else:
                        print('error after $')
                else:
                    print('no registers found')
                nxt = nxt + 2
                if t[nxt]==')' :
                    if flag1==0 and flag2==1 and flag3==0 and flag4==1 :
                        #print('command accepted')
                        self.address=(numb*4)+144
                        self.isload=1
                        self.totalcachecalls=self.totalcachecalls+1
                        self.pipelineforaddsubload()
                        self.isload=0
                else :
                    print('in line '+str(count+1)+' no ending statement')
            else :
                print('in line '+str(count+1)+' expected comma')
         else :
            print('in line '+str(count+1)+' space should be given')
        else :
          self.print('in line '+str(count+1)+' command not found')
     else :
      self.print('in line '+ str(count+1)+ ' command not found')