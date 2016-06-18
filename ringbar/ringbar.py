#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime as dt
from collections import defaultdict, OrderedDict


def make_time_step(start_dt, end_dt, bin_width):
    time_step_list = []
    step_dt = dt.datetime(start_dt.year,
                          start_dt.month,
                          start_dt.day,
                          start_dt.hour)
    while step_dt < end_dt:
        time_step_list.append(step_dt)
        step_dt += dt.timedelta(minutes=bin_width)
    return time_step_list


def make_print_line(line_list, time_step_list, bin_width):
    print_progress_dict = OrderedDict()
    for batch_name, duration in line_list.items():
        print_progress = ""
        for bin_dt in time_step_list:
            l_start = duration["start"]
            l_end = duration["end"]
            bin_td = dt.timedelta(minutes=bin_width)

            if bin_dt + bin_td <= l_start:
                print_progress += "."
            elif l_end < bin_dt:
                print_progress += "."
            elif bin_dt <= l_end < bin_dt + bin_td:
                print_progress += ">"
            else:
                print_progress += "="

        print_progress_dict[batch_name] = "|" + print_progress + "|"
    return print_progress_dict


def make_print_scale(time_step_list, bin_width):
    print_label_day = ""
    print_label_hour = ""
    current_h = ""
    progress_length = 0

    for i, s in enumerate(time_step_list):
        h = s.hour

        if i == 0:
            print_label_day += s.strftime('%Y/%m/%d')
        elif h == 0 and current_h != h:
            print_label_day += " " * (progress_length - 10)
            print_label_day += s.strftime('%Y/%m/%d')
            progress_length = 0
        else:
            pass

        if current_h != h:
            if h < 10:
                progress_string = str(h) + " " * int((60 / bin_width) - 1)
                print_label_hour += progress_string
                progress_length += len(progress_string)
            else:
                progress_string = str(h) + " " * int((60 / bin_width) - 2)
                print_label_hour += progress_string
                progress_length += len(progress_string)
        current_h = h
    return (print_label_day, print_label_hour)


class RingBar():

    def __init__(self,
                 print_start_time,
                 print_end_time,
                 datetime_format="%Y/%m/%d %H:%M:%S",
                 bin_width=15):
        self.bin_width = bin_width
        self.datetime_format = datetime_format
        self.print_start_time = dt.datetime.strptime(
            print_start_time, self.datetime_format)
        self.print_end_time = dt.datetime.strptime(
            print_end_time, self.datetime_format)
        self.time_step_list = make_time_step(self.print_start_time,
                                             self.print_end_time,
                                             self.bin_width)
        self.line_data = OrderedDict()

    def add(self, title, line_time):
        if len(line_time) == 2:
            t_start = dt.datetime.strptime(line_time[0], self.datetime_format)
            t_end = dt.datetime.strptime(line_time[1], self.datetime_format)
        elif len(line_time) == 1:
            t_start = dt.datetime.strptime(line_time[0], self.datetime_format)
            t_end = dt.datetime.today()
        self.line_data[title] = {"start": t_start, "end": t_end}

    def add_list(self, line_time_list):
        for line in line_time_list:
            title = line[0]
            line_time = line[1]
            self.add(title, line_time)

    def show(self):
        print_progress_dict = make_print_line(self.line_data,
                                              self.time_step_list,
                                              self.bin_width)
        print_label_day, print_label_hour = make_print_scale(self.time_step_list,
                                                             self.bin_width)

        output_list = []
        if print_progress_dict:
            print_label_width = max([len(s)
                                     for s in print_progress_dict.keys()]) + 1
        else:
            print_label_width = 1

        output_list.append(" " * print_label_width +
                           " " + print_label_day + " ")
        output_list.append(" " * print_label_width +
                           " " + print_label_hour + " ")

        for title, progress in print_progress_dict.items():
            output_title = title.rjust(print_label_width, ' ')
            output_list.append(output_title + progress)

        for line in output_list:
            print(line)
