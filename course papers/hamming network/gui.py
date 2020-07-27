
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageGrab

from tempfile import TemporaryDirectory

import image_load as il
from hm_algorithm import hamming_network_digits


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.grid(row=2, column=0)

        # цифры, образец
        self.digits = il.load_digits()

        # отступ между картинками и кнопками
        self.span0 = Label(text='                    ')
        self.span0.grid(row=0, column=1)

        # отступ между картинками пользователя и распознанной
        self.span3 = Label(text='                    ')
        self.span3.grid(row=1, column=0)

        # -----| распознанное изображение, начало |-----
        # текст над изображением
        self.rec_text = Label(self, text='Распознанное изображение')
        self.rec_text.grid(row=0, column=0)

        # изображение
        load = Image.open('digits/nothing.jpg')
        render = ImageTk.PhotoImage(load)
        self.img = Label(self, image=render)
        self.img.image = render
        self.img.grid(row=1, column=0)
        # -----| распознанное изображение, конец |-----

        # -----| холст, начало |-----
        # canvas label
        self.canvas_label = Label(self.master)
        self.canvas_label.grid(row=0, column=0)

        # холст
        self.canv = Canvas(self.canvas_label, width=256, height=256, bg='white')
        self.canv.grid(row=1, column=0)

        # текст над холстом
        self.canv_text = Label(self.canvas_label, text='Ваше изображение')
        self.canv_text.grid(row=0, column=0)

        # фиксирование действий мыши внутри холста
        self.canv.bind('<B1-Motion>', self.mouse_click)
        self.canv.bind('<Button-1>', self.mouse_click)
        # -----| холст, конец |-----

        # -----| кнопки, начало |-----
        # buttons label
        self.buttons_label = Label(self.master)
        self.buttons_label.grid(row=0, column=2)

        # отступ
        self.span4 = Label(self.buttons_label, text='                    ')
        self.span4.grid(row=0, column=0)

        # кнопки настройки перо/ластик
        self.pen_conf_buttons = Label(self.buttons_label)
        self.pen_conf_buttons.grid(row=1, column=0)
        self.pen_style = 1  # активирована ручка
        # ластик
        self.eraser_mode = Button(self.pen_conf_buttons, text='ластик', command=self.pen_eraser_on, bg='light gray')
        self.eraser_mode.grid(row=1, column=1)
        # перо
        self.pen_mode = Button(self.pen_conf_buttons, text='ручка', command=self.pen_pen_on, bg='white')
        self.pen_mode.grid(row=1, column=0)

        # очистка холста
        self.clear_canvas = Button(self.buttons_label, text='очистить рисунок', command=self.clr_canv)
        self.clear_canvas.grid(row=2, column=0)

        # загрузка изображения на холст
        self.laod_img_to_canvas = Button(self.buttons_label, text='загрузить изображение', command=self.ld_img_tcnvs)
        self.laod_img_to_canvas.grid(row=3, column=0)

        # отступ
        self.span1 = Label(self.buttons_label, text='                    ')
        self.span1.grid(row=4, column=0)

        # распознвание изображения
        self.recognition = Button(self.buttons_label, text='распознать изображение', command=self.rcgn_img)
        self.recognition.grid(row=5, column=0)

        # отступ
        self.span2 = Label(self.buttons_label, text='                    ')
        self.span2.grid(row=6, column=1)

        # выход
        self.exit = Button(self.buttons_label, text='выйти', command=self.ext)
        self.exit.grid(row=7, column=0)
        # -----| кнопки, конец |-----

    def mouse_click(self, event):
        x, y = event.x, event.y
        if self.pen_style:
            self.canv.create_oval(x-9, y-9, x+9, y+9, fill='black', outline='black')
        else:
            self.canv.create_oval(x-9, y-9, x+9, y+9, fill='white', outline='white')

    def clr_canv(self):
        self.canv.create_rectangle(0, 0, 257, 257, fill='white', outline='white')
        load = Image.open('digits/nothing.jpg')
        render = ImageTk.PhotoImage(load)
        self.img = Label(self, image=render)
        self.img.image = render
        self.img.grid(row=1, column=0)

    def ld_img_tcnvs(self):
        try:
            file_path = filedialog.askopenfilename()
            img_ld_tcanv = Image.open(file_path)
            tcnv_img = ImageTk.PhotoImage(img_ld_tcanv)
            self.canv.create_image(128, 128, image=tcnv_img)
            self.canv.image = tcnv_img
        except AttributeError:
            pass

    def rcgn_img(self):
        # сохранение картинки
        x = self.canv.winfo_rootx()
        y = self.canv.winfo_rooty()
        with TemporaryDirectory() as d:  # создание временной директории, d - путь
            pict = ImageGrab.grab(bbox=(x, y, x + 256, y + 256))  # глобальные коорд-ы холста
            img_path = d + r'/img1.jpg'
            pict.save(img_path)
            res = hamming_network_digits(img_path, self.digits)  # результаты распознования
        # загрузка результата как изображения
        try:
            res = int(res)
            load = Image.open('digits/{0}.jpg'.format(res))
        except ValueError:
            load = Image.open('digits/cant_reg.jpg'.format(res))
        render = ImageTk.PhotoImage(load)
        self.img = Label(self, image=render)
        self.img.image = render
        self.img.grid(row=1, column=0)

    def pen_eraser_on(self):
        self.eraser_mode.config(bg='white')
        self.pen_mode.config(bg='light gray')
        self.pen_style = 0

    def pen_pen_on(self):
        self.eraser_mode.config(bg='light gray')
        self.pen_mode.config(bg='white')
        self.pen_style = 1

    def ext(self):
        root.destroy()


root = Tk()
app = Window(root)
root.wm_title("Hamming network")
root.geometry("540x600")
root.mainloop()
