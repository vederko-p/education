import tkinter
import tkinter.messagebox

import numpy as np

import model_visualization as mymodel_vis


class GUI:

    def __init__(self):

        # window
        self.main_window = tkinter.Tk()
        self.main_window.title('An obstruction on the street model')
        self.main_window.geometry('792x400')
        self.main_window.configure(background='#292929')

        # span
        self.span = tkinter.Label(text='         ', bg='#292929')
        self.span.grid(row=0, column=2)

        # main
        self.main_label = tkinter.Label(
            text='Main',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 16 bold'
        )
        self.main_label.grid(row=0, column=0, columnspan=2)

        # steps
        self.entry_steps_text = tkinter.Label(
            text='Steps:',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.entry_steps_text.grid(row=1, column=0, sticky='W')

        self.entry_steps = tkinter.Entry(width=30, bg='#949494')
        self.entry_steps.grid(row=1, column=1)

        # initial_state
        self.entry_initial_state_text = tkinter.Label(
            text='Initial state:',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.entry_initial_state_text.grid(row=2, column=0, sticky='W')

        self.entry_initial_state = tkinter.Entry(width=30, bg='#949494')
        self.entry_initial_state.grid(row=2, column=1)

        # road_length
        self.entry_road_len_text = tkinter.Label(
            text='Road length:',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.entry_road_len_text.grid(row=3, column=0, sticky='W')

        self.entry_road_len = tkinter.Entry(width=30, bg='#949494')
        self.entry_road_len.grid(row=3, column=1)

        # max velocity
        self.entry_max_velocity_two_street_text = tkinter.Label(
            text='Max velocity',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 16 bold'
        )
        self.entry_max_velocity_two_street_text.grid(row=0, column=3, columnspan=2)

        # max velocity two-lane-street
        self.entry_max_velocity_two_street_text = tkinter.Label(
            text='Two-lane street:',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.entry_max_velocity_two_street_text.grid(row=1, column=3, sticky='W')

        self.entry_max_velocity_two_street = tkinter.Entry(width=5, bg='#949494')
        self.entry_max_velocity_two_street.grid(row=1, column=4)

        # max velocity conv-zone
        self.entry_max_velocity_conv_zone_text = tkinter.Label(
            text='Convergence zone:',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.entry_max_velocity_conv_zone_text.grid(row=2, column=3, sticky='W')

        self.entry_max_velocity_conv_zone = tkinter.Entry(width=5, bg='#949494')
        self.entry_max_velocity_conv_zone.grid(row=2, column=4)

        # max velocity obstr-zone
        self.entry_max_velocity_obstr_zone_text = tkinter.Label(
            text='Obstruction zone:',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.entry_max_velocity_obstr_zone_text.grid(row=3, column=3, sticky='W')

        self.entry_max_velocity_obstr_zone = tkinter.Entry(width=5, bg='#949494')
        self.entry_max_velocity_obstr_zone.grid(row=3, column=4)

        # p_brake
        self.entry_p_brake_text = tkinter.Label(
            text='Probability to brake:',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.entry_p_brake_text.grid(row=6, column=0, sticky='W')

        self.entry_p_brake = tkinter.Entry(width=30, bg='#949494')
        self.entry_p_brake.grid(row=6, column=1)

        # zones
        self.zones_label = tkinter.Label(
            text='Zones',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 16 bold'
        )
        self.zones_label.grid(row=7, column=0, columnspan=2)

        # conv-zone-coord
        self.entry_conv_zone_coord_text = tkinter.Label(
            text='Ends of convergence zones:',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.entry_conv_zone_coord_text.grid(row=8, column=0, sticky='W')

        self.entry_conv_zone_coord = tkinter.Entry(width=30, bg='#949494')
        self.entry_conv_zone_coord.grid(row=8, column=1)

        # obstr-zone-ends
        self.entry_obstr_zone_coord_text = tkinter.Label(
            text='Ends of obstruction zones:',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.entry_obstr_zone_coord_text.grid(row=9, column=0, sticky='W')

        self.entry_obstr_zone_coord = tkinter.Entry(width=30, bg='#949494')
        self.entry_obstr_zone_coord.grid(row=9, column=1)

        # additional_cars
        self.additional_cars_label = tkinter.Label(
            text='Additional cars',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 16 bold'
        )
        self.additional_cars_label.grid(row=7, column=3, columnspan=2)

        # add cars?
        self.entry_add_cars_q_text = tkinter.Label(
            text='Add additional cars?',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.entry_add_cars_q_text.grid(row=8, column=3, sticky='W')

        self.entry_add_cars_q_coord = tkinter.Entry(width=30, bg='#949494')
        self.entry_add_cars_q_coord.grid(row=8, column=4)

        # users's cars
        self.entry_user_cars_text = tkinter.Label(
            text='Your cars:',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.entry_user_cars_text.grid(row=9, column=3, sticky='W')

        self.entry_user_cars_coord = tkinter.Entry(width=30, bg='#949494')
        self.entry_user_cars_coord.grid(row=9, column=4)

        # random cars?
        self.entry_random_cars_q_text = tkinter.Label(
            text='Add random cars?',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.entry_random_cars_q_text.grid(row=10, column=3, sticky='W')

        self.entry_random_cars_q_coord = tkinter.Entry(width=30, bg='#949494')
        self.entry_random_cars_q_coord.grid(row=10, column=4)

        # span 2
        self.span_2 = tkinter.Label(text='', bg='#292929')
        self.span_2.grid(row=11, column=1)
        self.span_3 = tkinter.Label(text='', bg='#292929')
        self.span_3.grid(row=12, column=1)

        # buttons
        # user help
        self.user_help_button = tkinter.Button(
            text='?',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 18 bold',
            height=1,
            width=3,
            command=self.user_help_r
        )
        self.user_help_button.grid(row=0, column=5, sticky='NE')

        # start model
        self.start_model = tkinter.Button(
            text='Start model',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 14 bold',
            command=self.start_model
        )
        self.start_model.grid(row=13, column=1)

        # exit
        self.start_model = tkinter.Button(
            text='Exit',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 14 bold',
            command=self.main_model_exit
        )
        self.start_model.grid(row=13, column=3)

        self.main_window.mainloop()

    # methods
    def start_model(self):
        # entry_steps, entry_initial_state, entry_road_len, entry_max_velocity_two_street, entry_max_velocity_conv_zone,
        # entry_max_velocity_obstr_zone, entry_p_brake, entry_conv_zone_coord, entry_obstr_zone_coord,
        # entry_add_cars_q_coord, entry_user_cars_coord, entry_random_cars_q_coord

        # steps
        if self.entry_steps.get():
            n = int(self.entry_steps.get())
        else:
            n = 100
        # initial state - r1
        if self.entry_initial_state.get():
            r, r1 = self.entry_initial_state.get(), []
            r = r.split('|')
            for i in r:
                r1.append(i.split(','))
            for i in range(len(r1)):
                for j in range(len(r1[i])):
                    r1[i][j] = int(r1[i][j])
        else:
            r1 = []
        initial_state = np.array(r1)
        # road len
        if self.entry_road_len.get():
            road_len = int(self.entry_road_len.get())
        else:
            road_len = 100
        # max velocity
        if self.entry_max_velocity_two_street.get():
            two_lane_max_v = int(self.entry_max_velocity_two_street.get())
        else:
            two_lane_max_v = 5
        if self.entry_max_velocity_conv_zone.get():
            conv_zone_max_v = int(self.entry_max_velocity_conv_zone.get())
        else:
            conv_zone_max_v = 2
        if self.entry_max_velocity_obstr_zone.get():
            obstr_zone_max_v = int(self.entry_max_velocity_obstr_zone.get())
        else:
            obstr_zone_max_v = 3
        # p_brake
        if self.entry_p_brake.get():
            p_brake = float(self.entry_p_brake.get())
        else:
            p_brake = 0.2
        # conv zone coord
        if self.entry_conv_zone_coord.get():
            r, r1 = self.entry_conv_zone_coord.get(), []
            r = r.split('|')
            for i in r:
                r1.append(i.split(','))
            for i in range(len(r1)):
                for j in range(len(r1[i])):
                    r1[i][j] = int(r1[i][j])
        else:
            r1 = 0
        cz = r1
        # obstr zone coord
        if self.entry_obstr_zone_coord.get():
            r, r1 = self.entry_obstr_zone_coord.get(), []
            r = r.split('|')
            for i in r:
                r1.append(i.split(','))
            for i in range(len(r1)):
                for j in range(len(r1[i])):
                    r1[i][j] = int(r1[i][j])
        else:
            r1 = 0
        oz = r1
        # add cars ?
        if self.entry_add_cars_q_coord.get():
            if self.entry_add_cars_q_coord.get() == 'yes':
                add_cars_q = 1
            else:
                add_cars_q = 0
        else:
            add_cars_q = 0
        # user's cars
        if self.entry_user_cars_coord.get():
            r, r1 = self.entry_user_cars_coord.get(), []
            r = r.split('|')
            for i in r:
                r1.append(i.split(','))
            for i in range(len(r1)):
                for j in range(len(r1[i])):
                    r1[i][j] = int(r1[i][j])
            additional_cars = r1
        else:
            additional_cars = []
        # random cars
        if self.entry_random_cars_q_coord.get():
            random_cars = int(self.entry_random_cars_q_coord.get())
        else:
            random_cars = 0

        # model start
        steps = mymodel_vis.get_steps(n, initial_state, road_len, two_lane_max_v, conv_zone_max_v, obstr_zone_max_v, p_brake, cz, oz, add_cars_q, additional_cars, random_cars)
        mymodel_vis.make_animation(steps)

    def close_help(self):
        self.help_window.destroy()

    def main_model_exit(self):
        self.main_window.destroy()

    def user_help_r(self):

        # help window
        self.help_window = tkinter.Toplevel(self.main_window)
        self.help_window.title('Help')
        self.help_window.geometry('1350x600')
        self.help_window.configure(background='#292929')

        # text labels
        # main
        self.help_window_text_label_1 = tkinter.Label(
            self.help_window,
            text='Main',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 14 bold'
        )
        self.help_window_text_label_1.grid(row=0, column=0, sticky='W')

        self.help_window_text_label_2 = tkinter.Label(
            self.help_window,
            text='Steps: Принимает на вход количество шагов.',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_2.grid(row=1, column=0, sticky='W')

        self.help_window_text_label_3 = tkinter.Label(
            self.help_window,
            text='Initial state: Принимает на вход начальное состояние модели - "список" вида:',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_3.grid(row=2, column=0, sticky='W')

        self.help_window_text_label_4 = tkinter.Label(
            self.help_window,
            text='>>> lane_1, x_1, v_1 | lane_2, x_2, v_2 | ... | lane_n, x_n, v_n ,',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_4.grid(row=3, column=0, sticky='W')

        self.help_window_text_label_5 = tkinter.Label(
            self.help_window,
            text='::: lane_i - номер полосы i-ой машины;',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_5.grid(row=4, column=0, sticky='W')

        self.help_window_text_label_6 = tkinter.Label(
            self.help_window,
            text='::: x_i - позиция i-ой машины;',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_6.grid(row=5, column=0, sticky='W')

        self.help_window_text_label_7 = tkinter.Label(
            self.help_window,
            text='::: v_i - скорость i-ой машины.',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_7.grid(row=6, column=0, sticky='W')

        self.help_window_text_label_8 = tkinter.Label(
            self.help_window,
            text='Road length: Принимает на вход длину дороги.',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_8.grid(row=7, column=0, sticky='W')

        self.help_window_text_label_9 = tkinter.Label(
            self.help_window,
            text='Probability to brake: Принимает на вход вероятность дополнительного торможения.',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_9.grid(row=8, column=0, sticky='W')

        # max velocity
        self.help_window_text_label_10 = tkinter.Label(
            self.help_window,
            text='Max velocity',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 14 bold'
        )
        self.help_window_text_label_10.grid(row=0, column=2, sticky='W')

        # max velocity
        self.help_window_text_label_11 = tkinter.Label(
            self.help_window,
            text='Two-lane street: Принимает на вход максимальную скорость на свободной дороге.',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_11.grid(row=1, column=2, sticky='W')

        self.help_window_text_label_12 = tkinter.Label(
            self.help_window,
            text='Convergence zone: Принимает на вход максимальную скорость в зоне сужения.',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_12.grid(row=2, column=2, sticky='W')

        self.help_window_text_label_13 = tkinter.Label(
            self.help_window,
            text='Obstruction zone: Принимает на вход максимальную скорость на участке с препятствием.',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_13.grid(row=3, column=2, sticky='W')

        # gap
        self.gap1 = tkinter.Label(self.help_window, text='', bg='#292929',)
        self.gap1.grid(row=9, column=0)

        self.gap2 = tkinter.Label(self.help_window, text='         ', bg='#292929', )
        self.gap2.grid(row=24, column=1)

        self.gap3 = tkinter.Label(self.help_window, text='         ', bg='#292929', )
        self.gap3.grid(row=20, column=1)

        # zones
        self.help_window_text_label_14 = tkinter.Label(
            self.help_window,
            text='Zones',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 14 bold'
        )
        self.help_window_text_label_14.grid(row=10, column=0, sticky='W')

        self.help_window_text_label_15 = tkinter.Label(
            self.help_window,
            text='Ends of convergence zones: Принимает на вход границы зон сужения вида:',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_15.grid(row=11, column=0, sticky='W')

        self.help_window_text_label_16 = tkinter.Label(
            self.help_window,
            text='a, b | c, d | ... | e, f',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_16.grid(row=12, column=0, sticky='W')

        self.help_window_text_label_17 = tkinter.Label(
            self.help_window,
            text='Ends of obstruction zones: Принмает на вхо границы зон с препятсвием вида:',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_17.grid(row=13, column=0, sticky='W')

        self.help_window_text_label_18 = tkinter.Label(
            self.help_window,
            text='a, b | c, d | ... | e, f',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_18.grid(row=14, column=0, sticky='W')

        # additional cars
        self.help_window_text_label_19 = tkinter.Label(
            self.help_window,
            text='Additional cars',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 14 bold'
        )
        self.help_window_text_label_19.grid(row=5, column=2, sticky='W')

        self.help_window_text_label_19 = tkinter.Label(
            self.help_window,
            text='Add additional cars?: Принимает на вход yes/no.',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_19.grid(row=6, column=2, sticky='W')

        self.help_window_text_label_20 = tkinter.Label(
            self.help_window,
            text='Your cars?: Принимает на вход список вида:',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_20.grid(row=7, column=2, sticky='W')

        self.help_window_text_label_21 = tkinter.Label(
            self.help_window,
            text='>>> lane_1, v_1, step_1 | lane_2, v_2, step_2 | ... | lane_n, v_n, step_n ,',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_21.grid(row=8, column=2, sticky='W')

        self.help_window_text_label_22 = tkinter.Label(
            self.help_window,
            text='::: lane_i - номер полосы i-ой машины;',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_22.grid(row=9, column=2, sticky='W')

        self.help_window_text_label_23 = tkinter.Label(
            self.help_window,
            text='::: v_i - скорость i-ой машины;',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_23.grid(row=10, column=2, sticky='W')

        self.help_window_text_label_24 = tkinter.Label(
            self.help_window,
            text='::: step_i - шаг, на котором должна появиться i-ая машина.',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_24.grid(row=11, column=2, sticky='W')

        self.help_window_text_label_25 = tkinter.Label(
            self.help_window,
            text='>>> Add random cars?: Приниает на вход 0 или целое число > 0,',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_25.grid(row=12, column=2, sticky='W')

        self.help_window_text_label_26 = tkinter.Label(
            self.help_window,
            text='::: 0 - не добовлять случайные машины;',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_26.grid(row=13, column=2, sticky='W')

        self.help_window_text_label_27 = tkinter.Label(
            self.help_window,
            text='::: n > 0 - добавить n случайных машин.',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_27.grid(row=14, column=2, sticky='W')

        # buttons
        self.help_window_text_label_28 = tkinter.Label(
            self.help_window,
            text='Buttons',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 14 bold'
        )
        self.help_window_text_label_28.grid(row=21, column=0, sticky='W')

        self.help_window_text_label_29 = tkinter.Label(
            self.help_window,
            text='Start model: Запускает модель.',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_29.grid(row=22, column=0, sticky='W')

        self.help_window_text_label_30 = tkinter.Label(
            self.help_window,
            text='Exit: Закрывает окно',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 12'
        )
        self.help_window_text_label_30.grid(row=23, column=0, sticky='W')

        # close button
        self.help_window_close_button = tkinter.Button(
            self.help_window,
            text='Close',
            bg='#292929',
            fg='#ebebeb',
            font='"Franklin Gothic Medium" 14 bold',
            command=self.close_help
        )
        self.help_window_close_button.grid(row=25, column=1, sticky='W')


t = GUI()
