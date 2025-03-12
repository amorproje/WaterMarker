import random
from tkinter import *
from tkinter import filedialog,messagebox
from PIL import Image,ImageFilter,ImageTk

from PIL import ImageFont
from PIL import ImageDraw

window = Tk()
window.title("WATERMARKER")
window.geometry("650x650")



main_pic_file = None
main_logo_file = None

#"""FUNCTIONS"""


def upload_main():
    global main_pic_file
    main_pic_file = filedialog.askopenfilename(filetypes=[("png","*.png"),("jpg","*.jpg"),("All Files","*.*")])
    print(main_pic_file)
    main_pic_file = Image.open(main_pic_file)
    #change main pic

    resize = main_pic_file.resize(size=(250,140))
    global image,canvas_image
    image = ImageTk.PhotoImage(resize)
    canvas_image.create_image(100, 100, image=image)

    #add uploaded label

    global instruction
    instruction.destroy()
    instruction = Label(text="uploaded succesfully.",fg="green")
    instruction.grid(row=1, column=1)


def upload_logo():
    global v
    if v.get() == 1:

        global main_logo_file
        main_logo_file = filedialog.askopenfilename(filetypes=[("png", "*.png"), ("jpg", "*.jpg"), ("All Files", "*.*")])
        main_logo_file = Image.open(main_logo_file)



        #changing logo
        resize = main_logo_file.resize(size=(100,100))
        global image_logo,canvas_logo


        image_logo = ImageTk.PhotoImage(resize)
        canvas_logo.create_image(100, 100, image=image_logo)

        #changing lable
        logo_uploaded_label = Label(text="uploaded succesfully.",fg="green")
        logo_uploaded_label.grid(row=4,column=1)
    else:
        messagebox.showerror(title="input is empty",message="choose between adding text or logo")


def add_text():
    global v
    global main_pic_file,txt_entrie
    #if text radio button pressed
    if v.get() == 2:
        main_pic_file = main_pic_file.convert("RGBA")
        transparent_bg = Image.new("RGBA", main_pic_file.size, (0, 0, 0, 0))

        draw = ImageDraw.Draw(transparent_bg)

        font = ImageFont.truetype("arial.ttf", size=int(font_entrie.get()), )

        text_color = (255, 255, 255, int(opacity_entry.get()))


        if v_two.get() == 1:
            loc = (int(main_pic_file.size[0] / 7), int(main_pic_file.size[1] / 8))
            draw.text(loc, txt_entrie.get(), font=font, fill=text_color)
            main_pic_file = Image.alpha_composite(main_pic_file, transparent_bg)

        elif v_two.get() == 2:
            loc = (int(main_pic_file.size[0] / 3) + int(main_pic_file.size[0] / 6), int(main_pic_file.size[1] / 8))
            draw.text(loc, txt_entrie.get(), font=font, fill=text_color)
            main_pic_file = Image.alpha_composite(main_pic_file, transparent_bg)

        elif v_two.get() == 3:
            loc = (int(main_pic_file.size[0] / 2) + int(main_pic_file.size[0] / 3), int(main_pic_file.size[1] /8))
            draw.text(loc, txt_entrie.get(), font=font, fill=text_color)
            main_pic_file = Image.alpha_composite(main_pic_file, transparent_bg)

        elif v_two.get() == 4:
            loc = (int(main_pic_file.size[0] / 7), int(main_pic_file.size[1] / 2))
            draw.text(loc, txt_entrie.get(), font=font, fill=text_color)
            main_pic_file = Image.alpha_composite(main_pic_file, transparent_bg)

        elif v_two.get() == 5:
            loc = (int(main_pic_file.size[0] / 3) + int(main_pic_file.size[0] / 6), int(main_pic_file.size[1] / 2))
            draw.text(loc, txt_entrie.get(), font=font, fill=text_color)
            main_pic_file = Image.alpha_composite(main_pic_file, transparent_bg)

        elif v_two.get() == 6:
            loc = (int(main_pic_file.size[0] / 2) + int(main_pic_file.size[0] / 3), int(main_pic_file.size[1] / 2))
            draw.text(loc, txt_entrie.get(), font=font, fill=text_color)
            main_pic_file = Image.alpha_composite(main_pic_file, transparent_bg)

        elif v_two.get() == 7:
            loc = (int(main_pic_file.size[0] / 7), int(main_pic_file.size[1] / 2) + int(main_pic_file.size[1] / 3))
            draw.text(loc, txt_entrie.get(), font=font, fill=text_color)
            main_pic_file = Image.alpha_composite(main_pic_file, transparent_bg)

        elif v_two.get() == 8:
            loc = (int(main_pic_file.size[0] / 3) + int(main_pic_file.size[0] / 6), int(main_pic_file.size[1] / 2) + int(main_pic_file.size[1] / 3))
            draw.text(loc, txt_entrie.get(), font=font, fill=text_color)
            main_pic_file = Image.alpha_composite(main_pic_file, transparent_bg)

        elif v_two.get() == 9:
            loc = (int(main_pic_file.size[0] / 2) + int(main_pic_file.size[0] / 3), int(main_pic_file.size[1] / 2) + int(main_pic_file.size[1] / 3))
            draw.text(loc, txt_entrie.get(), font=font, fill=text_color)
            main_pic_file = Image.alpha_composite(main_pic_file, transparent_bg)

        else:
            messagebox.showwarning(message="choose watermark place !")

def generate():
    global v,main_pic_file,main_logo_file
    #checking if main_pic created and the button pressed
    if main_pic_file != None and v.get() == 1:

        main_logo_file = main_logo_file.convert("RGBA")
        main_pic_file = main_pic_file.convert("RGBA")
        width, height = main_logo_file.size

        try:
            size = int(size_entry.get())
            if not (0 <= size <= 100):
                size = 100
        except ValueError:
            size = 100
            
        print(size)
        resized_logo = main_logo_file.resize((
            int(width * size // 100),  # New width
            int(height * size // 100)  # New height
        ))

        if v_two.get() == 1:
            main_pic_file.paste(resized_logo,(int(main_pic_file.size[0] / 7), int(main_pic_file.size[1] / 8)),resized_logo)
            main_pic_file.show()

        elif v_two.get() == 2:
            main_pic_file.paste(resized_logo,(int(main_pic_file.size[0] / 3) + int(main_pic_file.size[0] / 6), int(main_pic_file.size[1] / 8)),resized_logo)
            main_pic_file.show()

        elif v_two.get() == 3:
            main_pic_file.paste(resized_logo,(int(main_pic_file.size[0] / 2) + int(main_pic_file.size[0] / 3), int(main_pic_file.size[1] /8)),resized_logo)
            main_pic_file.show()

        elif v_two.get() == 4:
            main_pic_file.paste(resized_logo,(int(main_pic_file.size[0] / 7), int(main_pic_file.size[1] / 2)),resized_logo)
            main_pic_file.show()

        elif v_two.get() == 5:
            main_pic_file.paste(resized_logo,(int(main_pic_file.size[0] / 3) + int(main_pic_file.size[0] / 6), int(main_pic_file.size[1] / 2)),resized_logo)
            main_pic_file.show()

        elif v_two.get() == 6:
            main_pic_file.paste(resized_logo,(int(main_pic_file.size[0] / 2) + int(main_pic_file.size[0] / 3), int(main_pic_file.size[1] / 2)),resized_logo)
            main_pic_file.show()

        elif v_two.get() == 7:
            main_pic_file.paste(resized_logo,(int(main_pic_file.size[0] / 7), int(main_pic_file.size[1] / 2) + int(main_pic_file.size[1] / 3)),resized_logo)
            main_pic_file.show()

        elif v_two.get() == 8:
            main_pic_file.paste(resized_logo,(int(main_pic_file.size[0] / 3) + int(main_pic_file.size[0] / 6), int(main_pic_file.size[1] / 2) + int(main_pic_file.size[1] / 3)),resized_logo)
            main_pic_file.show()

        elif v_two.get() == 9:
            main_pic_file.paste(resized_logo,(int(main_pic_file.size[0] / 2) + int(main_pic_file.size[0] / 3), int(main_pic_file.size[1] / 2) + int(main_pic_file.size[1] / 3)),resized_logo)
            main_pic_file.show()

        else:
            messagebox.showwarning(message="choose watermark place !")

    elif main_pic_file != None and v.get() == 2:
        add_text()
        main_pic_file.show()

    else:
        messagebox.showwarning(message="upload the file/press the button first!")

def download():


    dir = filedialog.askdirectory(title="Select folder to to save your file:")
    """of course its not the wise solution for file names,just tried to prevent same files,as fast as possible"""
    #file name
    rand_list = []
    rand_num = random.randint(100,5000)
    if rand_num in rand_list:
        rand_num = random.randint(100, 5000)
    rand_list.append(rand_num)


    main_pic_file.save(f"{dir}/watermarker-{rand_num}.png")

#"""IMAGES"""
#original image
canvas_image = Canvas(height=250,width=250)
image = PhotoImage(file="project_pictures/mainpic.png")
canvas_image.create_image(100,100,image=image)
canvas_image.place(x=80,y=35)
#logo
canvas_logo = Canvas(height=200,width=200)
image_logo = PhotoImage(file="project_pictures/logo3.png")
canvas_logo.create_image(100,100,image=image_logo)
canvas_logo.place(x=80,y=240)


#"""LABELS"""

greeting = Label(text="welcome to the WaterMarker",font=10)
greeting.place(x=220,y=20)

instruction = Label(text="(upload your photo to watermark it)")
instruction.place(x=375,y=160)

instruction_2 = Label(text="after choosing your style hit GENERATE then Download it")
instruction_2.place(x=320,y=370)

font_label = Label(text="font size:")
font_label.place(x=430,y=280)

opacity_label = Label(text="opacity (0-255):")
opacity_label.place(x=390,y=300)

watermark_place = Label(text="select your watermark place,try out different position\n and resizing to find out your favour output :")
watermark_place.place(x=105,y=470)

size_label = Label(text="resize in % :")
size_label.place(x=110,y=431)

#"""BUTTONS"""

upload_btn = Button(text="upload photo",width=20,height=3,bg="blue",fg="white",command=upload_main)
upload_btn.place(x=400,y=100)

upload_logo = Button(text="upload logo",bg="blue",fg="white",command=upload_logo)
upload_logo.place(x=140,y=400)

generate_btn = Button(text="GENERATE",width=25,height=4,bg="red",fg="white",command=generate)
generate_btn.place(x=120,y=570)

download_btn = Button(text="DOWNLOAD",width=25,height=4,bg="GREEN",fg="white",command=download)
download_btn.place(x=350,y=570)

#"""RADIO BUTTONS"""
v = IntVar()

radio_logo = Radiobutton(text="watermark with logo:",variable=v,value=1,font=3)

radio_logo.place(x=100,y=250)

radio_txt = Radiobutton(text="watermark with text:",variable=v,value=2,font=3)

radio_txt.place(x=400,y=250)

"""watermark position"""
v_two = IntVar()
position_1 = Radiobutton(variable=v_two,value=1)
position_1.place(x=400,y=450)

position_2 = Radiobutton(variable=v_two,value=2)
position_2.place(x=440,y=450)

position_3 = Radiobutton(variable=v_two,value=3)
position_3.place(x=480,y=450)

position_4 = Radiobutton(variable=v_two,value=4)
position_4.place(x=400,y=480)

position_5 = Radiobutton(variable=v_two,value=5)
position_5.place(x=440,y=480)

position_6 = Radiobutton(variable=v_two,value=6)
position_6.place(x=480,y=480)

position_7 = Radiobutton(variable=v_two,value=7)
position_7.place(x=400,y=510)

position_8 = Radiobutton(variable=v_two,value=8)
position_8.place(x=440,y=510)

position_9 = Radiobutton(variable=v_two,value=9)
position_9.place(x=480,y=510)

#"""ENTRIES"""

font_entrie = Entry(width=10)
font_entrie.insert(0,'35')
font_entrie.place(x=485,y=283)


txt_entrie = Entry(width=35)
txt_entrie.place(x=375,y=320)

opacity_entry = Entry(width=10)
opacity_entry.insert(0,'35')
opacity_entry.place(x=485,y=300)


size_entry = Entry(width=7)
size_entry.insert(0,'100')
size_entry.place(x=170,y=432)
window.mainloop()
