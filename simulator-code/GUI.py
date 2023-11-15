from tkinter import *
from tkinter import ttk
import os
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename

program_name = "AMIGOS MIPS SIMULATOR"


class GUI(Tk):  # Graphic User Interface

    def __init__(self):
        super().__init__()

        self.title(program_name)
        self.state('zoomed')

        i = PhotoImage(file=r'icon.png')
        self.iconphoto(False, i)
        self.UPDATE_PERIOD = 100
        self.updateId = None

        # --------------------------------------------------------------------------------

        self.notebook = ttk.Notebook(self)
        self.notebook.place(x=1, y=40)

        # --------------------------------------------------------------------------------

        self.frame = Frame(self.notebook, bd=1, relief=GROOVE)
        # self.frame.place(x=1, y=40)

        self.tFrame = Frame(self.notebook, bd=1, relief=GROOVE)

        self.labelframe = LabelFrame(self.tFrame, height=100, bd=1, bg="lightblue", text="Number of Instructions")
        self.labelframe.pack(fill=X, side=TOP)

        self.t = Text(self.labelframe, bg="#d9f4fc",
                      height=4, width=94,
                      padx=4,
                      highlightthickness=0,
                      takefocus=0,
                      bd=0, font=("", 12),
                      )
        self.t.place(x=10, y=0)

        self.labelframe2 = LabelFrame(self.tFrame, height=90, bg="pink", text="Number of Stalls")
        self.labelframe2.pack(fill=X, side=TOP)

        self.t2 = Text(self.labelframe2, bg="#fce6e6",
                       height=3, width=94,
                       padx=4,
                       highlightthickness=0,
                       takefocus=0,
                       bd=0, font=("", 13),
                       )
        self.t2.place(x=10, y=0)

        self.labelframe3 = LabelFrame(self.tFrame, bg="lightgreen", text="Stalls at : ")
        self.labelframe3.pack(fill="both", expand="yes")

        self.yScroll = Scrollbar(self.labelframe3, width=13)
        self.yScroll.pack(side=RIGHT, fill=Y)

        self.t3 = Text(self.labelframe3, bg="#e6fcec",
                       height=11, width=94,
                       padx=4,
                       highlightthickness=0,
                       takefocus=0,
                       bd=0,
                       yscrollcommand=self.yScroll.set,
                       font=("", 12),
                       )
        self.t3.place(x=10, y=0)
        self.yScroll.config(command=self.t3.yview)

        # ---------------------------------------------------------------------------------
        self.ctFrame = Frame(self.notebook, bd=1, relief=GROOVE)

        self.clabelframe = LabelFrame(self.ctFrame, height=90,  bg="lightblue", text="stalls")
        self.clabelframe.pack(fill=X, side=TOP)

        self.ct = Text(self.clabelframe, bg="#d9f4fc",
                      height=6, width=94,
                      padx=4,
                      highlightthickness=0,
                      takefocus=0,
                      bd=0, font=("", 12),
                      )
        self.ct.pack(fill =BOTH , expand = True)

        self.clabelframe2 = LabelFrame(self.ctFrame, height=90, bg="pink", text="cache missrate")
        self.clabelframe2.pack(fill=X, side=TOP)

        self.ct2 = Text(self.clabelframe2, bg="#fce6e6",
                       height=7, width=94,
                       padx=4,
                       highlightthickness=0,
                       takefocus=0,
                       bd=0, font=("", 12),
                       )
        self.ct2.pack(fill =BOTH , expand = True)

        self.clabelframe3 = LabelFrame(self.ctFrame, bg="lightgreen", text="Instructions per Cycle")
        self.clabelframe3.pack(fill=X, side=TOP)


        self.ct3 = Text(self.clabelframe3, bg="#e6fcec",
                       height=7, width=94,
                       padx=4,
                       highlightthickness=0,
                       takefocus=0,
                       bd=0,
                       font=("", 12),
                       )
        self.ct3.pack(fill =BOTH , expand = True)




        # ----------------------------------------------------------------------------------

        self.notebook.add(self.frame, text="editor")
        self.notebook.add(self.tFrame, text="Pipeline")
        self.notebook.add(self.ctFrame, text="Cache")

        # ---------------------------------------------------------------------------------

        self.frame2 = Frame(self, bd=1, relief=GROOVE)
        self.frame2.place(x=1, y=482)

        self.frame3 = Frame(self, bd=1, relief=FLAT)
        self.frame3.place(x=884, y=40)

        self.style = ttk.Style()

        self.style.configure("Treeview",
                             foreground="black",
                             rowheight=25,
                             fieldbackground="white"
                             )

        self.style.map('Treeview',
                       background=[('selected', 'green')])
        self.style.configure("Treeview.Heading",
                             background="black")

        # --------------------------------------------------------------------------
        self.scroll = ttk.Scrollbar(self.frame3)
        self.scroll.pack(side=RIGHT, fill=Y)

        self.tree = ttk.Treeview(self.frame3, yscrollcommand=self.scroll.set, selectmode="none", height=23)
        self.tree.pack(side=LEFT)
        self.scroll.configure(command=self.tree.yview)
        self.tree['columns'] = ("Registers", "Value")
        self.tree['show'] = 'headings'
        # format Our Columns

        self.tree.column("Registers", anchor='w', width=160, stretch=NO)
        self.tree.column("Value", anchor='w', width=200)

        # headings
        self.tree.heading("Registers", text="Registers")
        self.tree.heading("Value", text="Value")

        def disableEvent(event):
            return "break"

        self.tree.bind("<Button-1>", disableEvent)

        self.list1 = ["r0", "at", "v0", "v1", "a0", "a1", "a2", "a3", "t0", "t1",
                      "t2", "t3", "t4", "t5", "t6", "t7", "t8", "t9", "s0", "s1",
                      "s2", "s3", "s4", "s5", "s6", "s7", "s8", "k0", "k1", "gp", "sp", "ra"]
        self.list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.tree.tag_configure('odd', background="#F2F2F2")
        self.tree.tag_configure('even', background="#E6E6E6")
        self.tree.tag_configure('s', background="#bbf0fa")
        global ct
        ct = 0

        for i in range(0, 32):
            if ct % 2 == 0:
                self.tree.insert(parent='', index='end', iid=ct, text="", values=(self.list1[i], self.list2[i]),
                                 tags='even')
                ct += 1
            else:
                self.tree.insert(parent='', index='end', iid=ct, text="", values=(self.list1[i], self.list2[i]),
                                 tags='odd')
                ct += 1

        def stop():
            pass

        # ----------------------------------------------------------------------

        class HoverButton(Button):
            def __init__(self, master, **kw):
                Button.__init__(self, master=master, **kw)
                self.defaultBackground = self["background"]
                self.bind("<Enter>", self.on_enter)
                self.bind("<Leave>", self.on_leave)

            def on_enter(self, e):
                self['background'] = self['activebackground']

            def on_leave(self, e):
                self['background'] = self.defaultBackground

        class CreateToolTip(object):
            """
            create a tooltip for a given widget
            """

            def __init__(self, widget, text='widget info'):
                self.waittime = 400
                self.wraplength = 180
                self.widget = widget
                self.text = text
                self.widget.bind("<Enter>", self.enter)
                self.widget.bind("<Leave>", self.leave)
                self.widget.bind("<ButtonPress>", self.leave)
                self.id = None
                self.tw = None
                self.widget.defaultbackground = self.widget['background']

            def enter(self, event=None):
                self.widget['background'] = self.widget['activebackground']
                self.schedule()

            def leave(self, event=None):
                self.widget['background'] = self.widget.defaultBackground
                self.unschedule()
                self.hidetip()

            def schedule(self):
                self.unschedule()
                self.id = self.widget.after(self.waittime, self.showtip)

            def unschedule(self):
                id = self.id
                self.id = None
                if id:
                    self.widget.after_cancel(id)

            def showtip(self, event=None):
                x = y = 0
                x, y, cx, cy = self.widget.bbox("insert")
                x += self.widget.winfo_rootx() + 25
                y += self.widget.winfo_rooty() + 20
                # creates a toplevel window
                self.tw = Toplevel(self.widget)
                # Leaves only the label and removes the app window
                self.tw.wm_overrideredirect(True)
                self.tw.wm_geometry("+%d+%d" % (x, y))
                label = Label(self.tw, text=self.text, justify='left', relief='solid', borderwidth=1,
                              wraplength=self.wraplength)
                label.pack(ipadx=1)

            def hidetip(self):
                tw = self.tw
                self.tw = None
                if tw:
                    tw.destroy()

        # -------------------------------------------------
        def Clear():
            self.output.delete(1.0, END)

        self.output_label = ttk.Label(self.frame2, text='Console  : ')
        self.output_label.pack(side=TOP, anchor='w')

        self.output_button = HoverButton(self.frame2, text=" Clear ", relief=GROOVE, activebackground="lightblue",
                                         command=Clear)
        self.output_button.pack(side=LEFT)
        CreateToolTip(self.output_button, "Clear")

        self.yScrollbar = Scrollbar(self.frame2, orient=VERTICAL)
        self.yScrollbar.pack(fill='y', side=RIGHT)

        self.output = Text(self.frame2,
                           height=7, width=90,
                           padx=4,
                           highlightthickness=0,
                           takefocus=0,
                           bd=0, font=("", 13),
                           yscrollcommand=self.yScrollbar.set,
                           )
        self.output.bind("<Key>", lambda e: "break")
        self.output.pack()
        self.yScrollbar.config(command=self.output.yview)
        self.output.config(state='normal')

        self.file_label = ttk.Label(self.frame, text='Edit Your File Here')
        self.file_label.pack(side=TOP, anchor='n')

        self.cursor_label = ttk.Label(self.frame, text='Line: 1 | Column: 1')
        self.cursor_label.pack(side=BOTTOM, anchor='e')

        self.xscrollbar = Scrollbar(self.frame, orient=HORIZONTAL)
        self.xscrollbar.pack(side=BOTTOM, fill='x')

        # The widgets vertical scrollbar
        self.vScrollbar = Scrollbar(self.frame, orient=VERTICAL)
        self.vScrollbar.pack(fill='y', side=RIGHT)

        self.lnText = Text(self.frame,
                           height=19, width=4,
                           padx=4,
                           highlightthickness=0,
                           takefocus=1,
                           bd=0,
                           font=("", 13),
                           background='lightgrey',
                           foreground='black',
                           state='disabled'
                           )
        self.lnText.pack(side=LEFT, fill='y')

        self.text = Text(self.frame,
                         height=19, width=90, state='disabled',
                         wrap=NONE,
                         bd=0,
                         padx=4,
                         font=("", 13),
                         undo=True,
                         background='#FAFAFA',
                         yscrollcommand=self.vScrollbar.set,
                         xscrollcommand=self.xscrollbar.set
                         )
        self.text.pack(side=LEFT, expand=1)

        self.text.tag_configure("current_line", background="#e9e9e9")

        self.vScrollbar.config(command=self.text.yview)
        self.xscrollbar.config(command=self.text.xview)

        def highlight_current_line(interval=100):
            self.text.tag_remove("current_line", 1.0, "end")
            try:
                self.text.get(SEL_FIRST, SEL_LAST)
            except TclError:
                self.text.tag_add("current_line", "insert linestart", "insert lineend+1c")

            self.after(interval, highlight_current_line)

        highlight_current_line()

        def exit_editor(event=None):
            if messagebox.askokcancel("Exit", "Are you sure you want to Quit?"):
                self.destroy()

        # -----------------------------------------------------------------------------------------

        # EDIT MENU
        def cut():
            self.text.event_generate("<<Cut>>")
            return "break"

        def copy():
            self.text.event_generate("<<Copy>>")
            return "break"

        def paste():
            self.text.event_generate("<<Paste>>")
            return "break"

        def undo():
            self.text.event_generate("<<Undo>>")
            return "break"

        def redo(event=None):
            self.text.event_generate("<<Redo>>")
            return "break"

        def selectall(event=None):
            self.text.tag_add('sel', '1.0', 'end')
            return "break"

        def find_text(event=None):
            search_toplevel = Toplevel(self)
            search_toplevel.title('Find Text')
            search_toplevel.transient(self)
            search_toplevel.resizable(False, False)
            Label(search_toplevel, text="Find All:").grid(row=0, column=0, sticky='e')
            search_entry_widget = Entry(search_toplevel, width=25)
            search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')
            search_entry_widget.focus_set()
            ignore_case_value = IntVar()
            Checkbutton(search_toplevel, text='Ignore Case', variable=ignore_case_value).grid(row=1, column=1,
                                                                                              sticky='e', padx=2,
                                                                                              pady=2)
            Button(search_toplevel, text="Find All", underline=0,
                   command=lambda: search_output(
                       search_entry_widget.get(), ignore_case_value.get(),
                       self.text, search_toplevel, search_entry_widget)
                   ).grid(row=0, column=2, sticky='e' + 'w', padx=2, pady=2)

            def close_search_window():
                self.text.tag_remove('match', '1.0', END)
                search_toplevel.destroy()

            search_toplevel.protocol('WM_DELETE_WINDOW', close_search_window)
            return "break"

        def search_output(needle, if_ignore_case, content_text, search_toplevel, search_box):
            content_text.tag_remove('match', '1.0', END)
            matches_found = 0
            if needle:
                start_pos = '1.0'
                while True:
                    start_pos = content_text.search(needle, start_pos, nocase=if_ignore_case, stopindex=END)
                    if not start_pos:
                        break

                    end_pos = '{} + {}c'.format(start_pos, len(needle))
                    content_text.tag_add('match', start_pos, end_pos)
                    matches_found += 1
                    start_pos = end_pos
                content_text.tag_config('match', background='yellow', foreground='blue')
            search_box.focus_set()
            search_toplevel.title('{} matches found'.format(matches_found))

        # -----------------------------------------------------------------------------------------
        def update_cursor(event=None):
            row, col = self.text.index(INSERT).split('.')
            line_num, col_num = str(int(row)), str(int(col) + 1)  # col starts at 0
            infotext = "Line: {0} | Column: {1}".format(line_num, col_num)
            self.cursor_label.config(text=infotext)

        # -----------------------------------------------------------------------------------------

        self.shortcut_bar = Frame(self, height=25, bd=1, relief=GROOVE)
        self.shortcut_bar.pack(side=TOP, expand='no', fill=X)

        self.b1_icon = PhotoImage(file=r'new_file.png')
        self.b1 = HoverButton(self.shortcut_bar, relief=FLAT, image=self.b1_icon, command=self.new_file,
                              activebackground="lightblue")
        self.b1.pack(side=LEFT)
        CreateToolTip(self.b1, "New File")

        self.b2_icon = PhotoImage(file=r'open_file.png')
        self.b2 = HoverButton(self.shortcut_bar, relief=FLAT, image=self.b2_icon, command=self.open_file,
                              activebackground="lightblue")
        self.b2.pack(side=LEFT)
        CreateToolTip(self.b2, "Open File")

        self.b3_icon = PhotoImage(file=r'save.png')
        self.b3 = HoverButton(self.shortcut_bar, relief=FLAT, image=self.b3_icon, command=self.save,
                              activebackground="lightblue")
        self.b3.pack(side=LEFT)
        CreateToolTip(self.b3, "Save")

        self.b4_icon = PhotoImage(file=r'cut.png')
        self.b4 = HoverButton(self.shortcut_bar, relief=FLAT, image=self.b4_icon, command=cut,
                              activebackground="lightblue")
        self.b4.pack(side=LEFT)
        CreateToolTip(self.b4, "Cut")

        self.b5_icon = PhotoImage(file=r'copy.png')
        self.b5 = HoverButton(self.shortcut_bar, relief=FLAT, image=self.b5_icon, command=copy,
                              activebackground="lightblue")
        self.b5.pack(side=LEFT)
        CreateToolTip(self.b5, "Copy")

        self.b6_icon = PhotoImage(file=r'paste.png')
        self.b6 = HoverButton(self.shortcut_bar, relief=FLAT, image=self.b6_icon, command=paste,
                              activebackground="lightblue")
        self.b6.pack(side=LEFT)
        CreateToolTip(self.b6, "Paste")

        self.b7_icon = PhotoImage(file=r'undo.png')
        self.b7 = HoverButton(self.shortcut_bar, relief=FLAT, image=self.b7_icon, command=undo,
                              activebackground="lightblue")
        self.b7.pack(side=LEFT)
        CreateToolTip(self.b7, "Undo")

        self.b8_icon = PhotoImage(file=r'redo.png')
        self.b8 = HoverButton(self.shortcut_bar, relief=FLAT, image=self.b8_icon, command=redo,
                              activebackground="lightblue")
        self.b8.pack(side=LEFT)
        CreateToolTip(self.b8, "Redo")

        self.b9_icon = PhotoImage(file=r'find.png')
        self.b9 = HoverButton(self.shortcut_bar, relief=FLAT, image=self.b9_icon, command=find_text,
                              activebackground="lightblue")
        self.b9.pack(side=LEFT)
        CreateToolTip(self.b9, "Search")

        self.b10_icon = PhotoImage(file=r'play.png')
        self.b10 = HoverButton(self.shortcut_bar, relief=FLAT, image=self.b10_icon,
                               activebackground="lightblue")
        self.b10.pack(side=LEFT)
        CreateToolTip(self.b10, "Run")

        self.b11_icon = PhotoImage(file=r'stop.png')
        self.b11 = HoverButton(self.shortcut_bar, relief=FLAT, image=self.b11_icon, command=stop,
                               activebackground="lightblue")
        self.b11.pack(side=LEFT)
        CreateToolTip(self.b11, "Stop")

        # --------------------------------------------------------------------------------------------------------------

        self.menubar = Menu()
        file_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='New', accelerator='Ctrl+N', compound='left', image=self.b1_icon, underline=0,
                              command=self.new_file)
        file_menu.add_command(label='Load File', accelerator='Ctrl+O', compound='left', image=self.b2_icon, underline=0,
                              command=self.open_file)
        file_menu.add_command(label='Save', accelerator='Ctrl+S', compound='left', image=self.b3_icon, underline=0,
                              command=self.save)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', accelerator='Alt+F4', compound='left', underline=0, command=exit_editor)

        edit_menu = Menu(self.menubar, tearoff=0)
        edit_menu.add_command(label='Cut', accelerator='Ctrl+X', compound='left', image=self.b4_icon, underline=0,
                              command=cut)
        edit_menu.add_command(label='Copy', accelerator='Ctrl+C', compound='left', image=self.b5_icon, underline=0,
                              command=copy)
        edit_menu.add_command(label='Paste', accelerator='Ctrl+V', compound='left', image=self.b6_icon, underline=0,
                              command=paste)
        edit_menu.add_separator()
        edit_menu.add_command(label='Undo', accelerator='Ctrl + Z', compound='left', image=self.b7_icon, underline=0,
                              command=undo)
        edit_menu.add_command(label='Redo', accelerator='Ctrl+Y', compound='left', image=self.b8_icon, underline=0,
                              command=redo)
        edit_menu.add_separator()
        edit_menu.add_command(label='Find', accelerator='Ctrl+F', compound='left', image=self.b9_icon, underline=0,
                              command=find_text)
        edit_menu.add_separator()
        edit_menu.add_command(label='Select All', accelerator='Ctrl+A', compound='left', underline=0, command=selectall)
        self.menubar.add_cascade(label='Edit', menu=edit_menu)

        self.forwarding =  BooleanVar()
        data_menu = Menu(self.menubar, tearoff=0)
        data_menu.add_checkbutton(label="Data Forwarding", onvalue=1, offvalue=0, variable=self.forwarding)
        self.menubar.add_cascade(label='Data Forwarding', menu=data_menu)


        self.assoc = IntVar()
        assoc_menu= Menu(self.menubar, tearoff=0)
        assoc_menu.add_radiobutton(label="1",variable=self.assoc, value=1)
        assoc_menu.add_radiobutton(label="2",variable=self.assoc, value=2)
        assoc_menu.add_radiobutton(label="3",variable=self.assoc, value=3)
        self.menubar.add_cascade(label="assocoativity",menu=assoc_menu)
        self.assoc.set(2)

        self.IndexBits = IntVar()
        IndexBits_menu = Menu(self.menubar, tearoff=0)
        IndexBits_menu.add_radiobutton(label="1",variable=self.IndexBits, value=1)
        IndexBits_menu.add_radiobutton(label="2",variable=self.IndexBits, value=2)
        IndexBits_menu.add_radiobutton(label="4",variable=self.IndexBits, value=4)
        self.menubar.add_cascade(label="Number of IndexBits", menu=IndexBits_menu)
        self.IndexBits.set(2)

        self.config(menu=self.menubar)

        def my_popup(e):
            popup_menu.tk_popup(e.x_root, e.y_root)

        popup_menu = Menu(self.text, tearoff=0)
        popup_menu.add_command(label='Cut', accelerator='Ctrl+X', compound='left', underline=0, command=cut)
        popup_menu.add_command(label='Copy', accelerator='Ctrl+C', compound='left', underline=0, command=copy)
        popup_menu.add_command(label='Paste', accelerator='Ctrl+V', compound='left', underline=0, command=paste)
        popup_menu.add_command(label='Undo', accelerator='Ctrl + Z', compound='left', underline=0, command=undo)
        popup_menu.add_command(label='Redo', accelerator='Ctrl+Y', compound='left', underline=0, command=redo)
        popup_menu.add_command(label='Find', accelerator='Ctrl+F', compound='left', underline=0,
                               command=find_text)
        popup_menu.add_command(label='Select All', accelerator='Ctrl+A', compound='left', underline=0,
                               command=selectall)
        popup_menu.add_separator()
        popup_menu.add_command(label='Exit', accelerator='Alt+F4', compound='left', underline=0, command=exit_editor)

        self.text.bind("<Button-3>", my_popup)

        # end of Edit Menu

        def getLineNumbers():
            x = 0
            line = '0'
            col = ''
            ln = ''

            nl = '\n'
            lineMask = '    %s\n'
            indexMask = '@0,%d'

            for i in range(0, self.text.winfo_height()):

                ll, cc = self.text.index(indexMask % i).split('.')

                if line == ll:
                    if col != cc:
                        col = cc
                        ln += nl
                else:
                    line, col = ll, cc
                    ln += (lineMask % line)[-5:]

            return ln

        def updateLineNumbers():
            tt = self.lnText
            ln = getLineNumbers()
            lineNumbers = ln
            tt.config(state='normal')
            tt.delete('1.0', END)
            tt.insert('1.0', lineNumbers)
            tt.config(state='disabled')
            update_cursor()

        def updateAllLineNumbers():
            updateLineNumbers()
            self.updateId = self.text.after(
                self.UPDATE_PERIOD,
                updateAllLineNumbers)

        if self.updateId is None:
            updateAllLineNumbers()

        self.protocol('WM_DELETE_WINDOW', exit_editor)

        # handling binding
        self.text.bind('<Control-N>', self.new_file)
        self.text.bind('<Control-n>', self.new_file)
        self.text.bind('<Control-O>', self.open_file)
        self.text.bind('<Control-o>', self.open_file)
        self.text.bind('<Control-S>', self.save)
        self.text.bind('<Control-s>', self.save)
        self.text.bind('<Control-Y>', redo)
        self.text.bind('<Control-y>', redo)
        self.text.bind('<Control-Z>', undo)
        self.text.bind('<Control-z>', undo)
        self.text.bind('<Control-A>', selectall)
        self.text.bind('<Control-a>', selectall)
        self.text.bind('<Control-F>', find_text)
        self.text.bind('<Control-f>', find_text)

    def link_with_main(self, m):
        self.m = m
        self.b10.configure(command=self.m.run)

    def load(self):
        for i in range(0, 32):
            if i % 2 == 0:
                self.tree.item(i, text="", values=(self.list1[i], self.list2[i]), tag='even')
            else:
                self.tree.item(i, text="", values=(self.list1[i], self.list2[i]), tag='eodd')

    def new_file(self):

        self.load()
        self.notebook.select(self.frame)
        t = self.text
        t.config(state='normal')
        self.file_label.config(text="Untitled")
        global file_name
        file_name = None
        self.text.delete(1.0, END)

    def open_file(self):
        self.load()
        self.notebook.select(self.frame)
        t = self.text

        input_file_name = askopenfilename(defaultextension=".asm",
                                          filetypes=[("Assembly Files", "*.s"),
                                                     ("Assembly Files", "*.asm")])
        if input_file_name:
            t.config(state='normal')
            global file_name
            file_name = input_file_name
            # root.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME))
            self.file_label.config(text=os.path.basename(file_name))
            self.text.delete(1.0, END)
            with open(file_name) as _file:
                self.text.insert(INSERT, _file.read())
            lines = self.text.get("1.0", END).splitlines()
            ln_count = 0.0
            for line in lines:
                ln_count += 1.0
            self.text.delete(ln_count, END)

    def write_to_file(self, file_name):
        try:
            content = self.text.get(1.0, 'end')
            with open(file_name, 'w') as the_file:
                the_file.write(content)
        except IOError:
            pass

    def save_as(self):
        input_file_name = asksaveasfilename(defaultextension=".asm")
        if input_file_name:
            global file_name
            file_name = input_file_name
            self.write_to_file(file_name)
            self.title('{} - {}'.format(os.path.basename(file_name), "AMIGOS MIPS SIMULATOR"))
            self.file_label.config(text=os.path.basename(file_name))
        return "break"

    def save(self):
        global file_name
        if not file_name:
            self.save_as()
        if file_name:
            self.write_to_file(file_name)
        return "break"


if __name__ == '__main__':
    gui = GUI
    gui.mainloop()
