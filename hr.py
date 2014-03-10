__author__ = 'Laura'

import os
import re
import json
from walk import Walk
import pylab as pl
import numpy as np


def get_settings(settings_file_name):
    with open(settings_file_name, 'rb') as settings_file:
        return json.load(settings_file)


def month_ordering(text):
    """
    Provides an integer for a recognized month, or zero if not.
    Digits are translated as digits.
    """
    months = ['Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']
    calendar = {month: order for month, order in zip(months, xrange(1, len(months) + 1))}
    return int(text) if text.isdigit() else calendar.get(text, 0)


def natural_keys(text):
    """
    Use my_list.sort(key=natural_keys) to sort a list that puts months in the right order
    """
    return [month_ordering(character) for character in re.split('(\d+)', text)]


def get_file_list(track_type, hr_folder_path):
    files = []
    for root, dirs, file_list in os.walk(hr_folder_path):
        for item in file_list:
            if re.search(track_type + '.*csv', item):
                files.append(item)
    files.sort(key=natural_keys)
    return files

def plot_time_data(hr_folder, files):
    for file_num, file_name in enumerate(files):
        file_path = os.path.join(hr_folder, file_name)
        new_walk = Walk(file_path)
        if file_num <= num_files / 2:
            pl.subplot(2, 1, 1)
        else:
            pl.subplot(2, 1, 2)
        pl.plot(new_walk.hr, label=new_walk.name)
        pl.ylabel('Heart Rate (bpm)')
        pl.xlabel('Time (data points)')
    pl.subplot(2, 1, 1)
    pl.legend(loc=5)
    pl.subplot(2, 1, 2)
    pl.legend(loc=5)
    pl.show()

def plot_max_min(hr_folder, files):
    maxes = []
    mins = []
    means = []
    for file_num, file_name in enumerate(files):
        file_path = os.path.join(hr_folder, file_name)
        new_walk = Walk(file_path)
        max_hr = np.max(new_walk.hr)
        mean_hr = np.mean(new_walk.hr)
        min_hr = np.min(new_walk.hr)
        maxes.append(max_hr)
        mins.append(min_hr)
        means.append(mean_hr)

    pl.plot(maxes, label='Max HR')
    pl.plot(means, label='Mean HR')
    pl.plot(mins, label='Min HR')
    pl.ylabel('Heart Rate (BPM)')
    pl.legend()
    pl.show()


if __name__ == '__main__':
    settings = get_settings('.settings')
    track_type = settings['type']
    hr_folder = settings['file_path']
    files = get_file_list(track_type, hr_folder)
    num_files = len(files)

    plot_time_data(hr_folder, files)
    plot_max_min(hr_folder, files)
