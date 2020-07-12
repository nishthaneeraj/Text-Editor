# so this is text editor..........
# and this is my first software
# so first i import modules
import tkinter as tk
from tkinter import ttk
from tkinter import  font, colorchooser, filedialog, messagebox
import os
# starter code
main_win = tk.Tk()
main_win.geometry('1200x800')
main_win.title('Visual Text Editor')
main_win.wm_iconbitmap('icon.ico')

############### main menu ###################
main_menu = tk.Menu()
# file icons
new_icon = tk.PhotoImage(file='icons2/new.png')
open_icon = tk.PhotoImage(file='icons2/open.png')
save_icon = tk.PhotoImage(file='icons2/save.png')
save_as_icon = tk.PhotoImage(file='icons2/save_as.png')
exit_icon = tk.PhotoImage(file='icons2/exit.png')
file_menu = tk.Menu(main_menu,tearoff=False)

# edit icons
cut_icon = tk.PhotoImage(file='icons2/cut.png')
copy_icon = tk.PhotoImage(file='icons2/copy.png')
paste_icon = tk.PhotoImage(file='icons2/paste.png')
clear_all_icon = tk.PhotoImage(file='icons2/clear_all.png')
find_icon = tk.PhotoImage(file='icons2/find.png')
edit_menu = tk.Menu(main_menu,tearoff=False)

# view icons
tool_bar_icon = tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons2/status_bar.png')
view_menu = tk.Menu(main_menu,tearoff=False)

# color theme icons
light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')
color_theme_menu = tk.Menu(main_menu,tearoff=False)

theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

color_dict = {
    'Light Default ' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' :('#ededed', '#6b9dc2')
}


# cascade

main_menu.add_cascade(label='File', menu=file_menu )
main_menu.add_cascade(label='Edit', menu=edit_menu )
main_menu.add_cascade(label='View', menu=view_menu )
main_menu.add_cascade(label='Color Themes', menu=color_theme_menu )

############### End main menu ###################
############### tool bar ###################
## ******* font box***********##
toolbar = tk.LabelFrame(main_win)
toolbar.pack(side=tk.TOP, fill=tk.X)
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(toolbar , width=30 , textvariable=font_family ,state='readonly'  )
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0 , column=0 , padx=5)

#********* size box **************#

size_var = tk.IntVar()
font_size = ttk.Combobox(toolbar , width=14, textvariable=size_var, state='readonly')
font_size['values'] = tuple(range(8,80))
font_size.current(4)
font_size.grid(row=0, column=1, padx=5)

# ********* bold button**************

bold_icon = tk.PhotoImage(file='icons2/bold.png')
bold_btn = ttk.Button(toolbar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

# ********* italic button**************

italic_icon = tk.PhotoImage(file='icons2/italic.png')
italic_btn = ttk.Button(toolbar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

# ********* underline button**************

underline_icon = tk.PhotoImage(file='icons2/underline.png')
underline_btn = ttk.Button(toolbar, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)

# ********* color_choose button**************

font_color_icon = tk.PhotoImage(file='icons2/font_color.png')
font_color_btn = ttk.Button(toolbar, image=font_color_icon)
font_color_btn.grid(row=0, column=5, padx=5)

# ********* aligh left button**************

align_left_icon = tk.PhotoImage(file='icons2/align_left.png')
align_left_btn = ttk.Button(toolbar, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

# ********* aligh center button**************

align_center_icon = tk.PhotoImage(file='icons2/align_center.png')
align_center_btn = ttk.Button(toolbar, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=5)

# ********* aligh right button**************

align_right_icon = tk.PhotoImage(file='icons2/align_right.png')
align_right_btn = ttk.Button(toolbar, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)

############### End tool bar ###################

############### text editor ###################

text_editor = tk.Text(main_win)
text_editor.config(wrap='word', relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_win)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# font family and font size functionality

current_font_family = 'Arial'
current_font_size = 12

# font family

def change_font(main_win):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family , current_font_size))

# font size

def change_fontsize(main_win):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family , current_font_size))

font_box.bind("<<ComboboxSelected>>" , change_font)
font_size.bind("<<ComboboxSelected>>" , change_fontsize)

#************ button functionality************

# ************** @ Bold Button ***********
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'] )
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size , 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size , 'normal'))

bold_btn.configure(command=change_bold)


# ********* @ italic button functionality**************
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'] )
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size , 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family, current_font_size , 'normal'))

italic_btn.configure(command=change_italic)

# **************** @ underline button functionality********************
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'] )
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size ,'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size , 'normal'))

underline_btn.configure(command=change_underline)

# ************ @ font color functionality*******************
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])


font_color_btn.configure(command=change_font_color)

# ************ align functionality *************
# ***************align left functionality*************
def align_left():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')

align_left_btn.configure(command=align_left)
# ***************align center functionality*************
def align_center():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

align_center_btn.configure(command=align_center)
# ***************align right functionality*************
def align_right():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')

align_right_btn.configure(command=align_right)

text_editor.configure(font=('Arial',12))

############### End text editor ###################

############### status bar ###################

statusbar = ttk.Label(main_win, text='Status Bar')
statusbar.pack(side=tk.BOTTOM)

# ********* status bar functionality*******************
text_changed = False
def count(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        statusbar.config(text=f'Characters : {characters}  Words:{words}')
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>" , count)
############### End status bar  ###################

############### main menu functionality   ###################

# file menu functionality************
# variable

url = ''

# @ new Command functionality
def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)

# file_menu_command

file_menu.add_command(label='New',image=new_icon, compound=tk.LEFT , accelerator='Ctrl+N' , command=new_file)

# *********** @ open functionality ************

def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File' , '*.txt'),('All Files', '*.*')))
    try:
        with open(url , 'r') as rf:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, rf.read())

    except FileNotFoundError :
        return
    except:
        return

    main_win.title(os.path.basename(url))


file_menu.add_command(label='Open',image=open_icon, compound=tk.LEFT , accelerator='Ctrl+O', command=open_file)
# *********** @ save functionality ************
def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.End))
            with open(url, 'w', encoding='utf=8') as fr:
                fr.write(content)

        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt' , filetypes=(('Text File' , '*.txt'),('All Files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close

    except:
        return


file_menu.add_command(label='Save',image=save_icon, compound=tk.LEFT , accelerator='Ctrl+S', command=save_file)

# ************* @ save as functionality****************
def save_as_file(event=None):
    try:
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt' , filetypes=(('Text File' , '*.txt'),('All Files', '*.*')))
        content = text_editor.get(1.0, tk.END)
        url.write(content)
        url.close
    except:
        return

file_menu.add_command(label='Save As',image=save_as_icon, compound=tk.LEFT , accelerator='Ctrl+Alt+N', command=save_as_file)

# ************* @ exit functionality****************
def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_win.destroy()
                else:
                    content2 = text_editor.get(1.0, tk.END)
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt' , filetypes=(('Text File' , '*.txt'),('All Files', '*.*')))
                    url.write(content2)
                    url.close
                    main_win.destroy()
            elif mbox is False:
                 main_win.destroy()
        else:
            main_win.destroy()
    except:
        return


file_menu.add_command(label='Exit',image=exit_icon, compound=tk.LEFT , accelerator='Ctrl+Q', command=exit_func)

# edit_menu_command
#***************** @ find functionality **********************
def find_func(event=None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break 
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')
    
    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

    # frame
    find_frame =ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    # labels
    find_label = ttk.Label(find_frame, text='Find : ')
    replace_label = ttk.Label(find_frame, text='Replace : ')

    # entry box
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    # button
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text='Replace', command=replace)

    # label grid
    find_label.grid(row=0, column=0 , padx=4, pady=4)
    replace_label.grid(row=1, column=0 , padx=4, pady=4)

    # entry box grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    # button grid
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()

edit_menu.add_command(label='Cut',image=cut_icon, compound=tk.LEFT , accelerator='Ctrl+X', command=lambda:text_editor.event_generate('<Control x>'))
edit_menu.add_command(label='Copy',image=copy_icon, compound=tk.LEFT , accelerator='Ctrl+C', command=lambda:text_editor.event_generate('<Control c>'))
edit_menu.add_command(label='Paste',image=paste_icon, compound=tk.LEFT , accelerator='Ctrl+V', command=lambda:text_editor.event_generate('<Control v>'))
edit_menu.add_command(label='Clear All',image=clear_all_icon, compound=tk.LEFT , accelerator='Ctrl+Alt+X', command=lambda:text_editor.delete(1.0, tk.END))
edit_menu.add_command(label='Find',image=find_icon, compound=tk.LEFT , accelerator='Ctrl+F', command=find_func)

# view_menu_command

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        toolbar.pack_forget()
        show_toolbar = False 
    else :
        text_editor.pack_forget()
        statusbar.pack_forget()
        toolbar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        statusbar.pack(side=tk.BOTTOM)
        show_toolbar = True 


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        statusbar.pack_forget()
        show_statusbar = False 
    else :
        statusbar.pack(side=tk.BOTTOM)
        show_statusbar = True 


view_menu.add_checkbutton(label='Tool Bar', onvalue=True, offvalue=False,variable=show_toolbar, image=tool_bar_icon, compound=tk.LEFT, command=hide_toolbar)
view_menu.add_checkbutton(label='Status Bar',onvalue=True, offvalue=False,variable=show_statusbar, image=status_bar_icon, compound=tk.LEFT, command= hide_statusbar)

#color_theme_menu_command
def change_theme():
    choosen_theme= theme_choice.get()
    color_tuple= color_dict.get(choosen_theme)
    fg_color, bg_color = color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)
count = 0
for i in color_dict:
    color_theme_menu.add_radiobutton(label=i, image=color_icons[count], compound=tk.LEFT , variable = theme_choice,command=change_theme)
    count+=1

############### End main menu functionality  ###################
main_win.config(menu=main_menu)

# ****** @ bind shortcut keys ******
main_win.bind("<Control-n>", new_file)
main_win.bind("<Control-o>", open_file)
main_win.bind("<Control-s>", save_file)
main_win.bind("<Control-Alt-s>", save_as_file)
main_win.bind("<Control-q>", exit_func)
main_win.bind("<Control-f>",find_func)

main_win.mainloop()
