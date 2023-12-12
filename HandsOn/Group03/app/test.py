import random
import datetime
from config import DataConfig
import os
import threading
import time
from datetime import datetime, time
from ipywidgets import widgets
from functools import partial
from config import DataConfig, StyleConfig
from IPython.display import display, clear_output, HTML
from visuals.map_manager import createBaseMap
from visuals.gui_manager import create_stations_cbox, reset_cbox
from app.route import process_route

# progress_bar
progress_bar = widgets.IntProgress(
    value=0,
    min=0,
    max=100,
    description='Generating map:',
    style={'bar_color': 'pink'},
    orientation='horizontal'
)
process_route('Cuire', 'Monplaisir - Lumière', datetime.now().time(),progress_bar)

def get_wait_time(nodes=['Cuire',
  'Hénon',
  'Croix-Rousse',
  'Croix-Paquet',
  'Hôtel de Ville - Louis Pradel',
  'Cordeliers',
  'Bellecour',
  'Guillotière',
  'Saxe - Gambetta',
  'Garibaldi',
  'Sans Souci',
  'Monplaisir - Lumière'], currentTime=datetime.now()) -> int:
    """Calculates the waiting time at the start of the journey
    or if we have to change lines

    Args:
        nodes : list with all the stations in our journey
        currentHour : the time when the journey starts

    Returns:
        int: wainting time in minutes
    """

    junctions = DataConfig.JUNCTIONS.value.keys()
    
    wait_time = 0
    max_check = len(nodes) - 1

    for i, station in enumerate(nodes):
        if i == 0:
            wait_time += get_line_wait_time(station, currentTime)
        elif i != max_check:
             previous_station = nodes[i-1]
             next_station = nodes[i+1]
             if station in junctions and changed_line(previous_station, next_station):
                wait_time = wait_time + get_line_wait_time(station, currentTime)
    print(wait_time)
    return wait_time


def get_line_wait_time(station, currentTime):
    normalSchedule_Start = time(hour=5, minute=0, second=0)
    normalSchedule_End = time(hour=20, minute=0, second=0)
    lines = DataConfig.LINES.value

    if DataConfig.USE_SEED.value:
        seed_value = 42
        random.seed(seed_value)

    wait_time = 0
    # we are during normal schedule
    if normalSchedule_Start.hour <= currentTime.hour <= normalSchedule_End.hour:
        if station in lines["A"]:
            wait_time = random.randint(1,6)
        elif station in lines["B"]:
            wait_time = random.randint(1,7)
        elif station in lines["C"]:
            wait_time = random.randint(1,11)
        elif station in lines["D"]:
            wait_time = random.randint(1,9)
    # we are out of schedule
    else:
        wait_time = random.randint(1,11)
    
    return wait_time

def changed_line(previous_station, next_station) -> bool:
    """We check if two stations are on the same line

    Args:
        previous_station : name of the previous station
        next_station : name of the next station

    Returns:
        bool: True if we changed stations
    """

    lines = DataConfig.LINES.value
    lineKeys = list(lines.keys())
    i = 0 
    changed = False

    while not changed and i < len(lineKeys):
        print(f"{lineKeys[i]} - {previous_station} - {next_station}")
        if (previous_station in lines[lineKeys[i]]) and not(next_station in lines[lineKeys[i]]):
            print("TRUE")
            changed = True
        else:
            print("False")
            changed = False 
        i += 1
    return changed

get_wait_time()