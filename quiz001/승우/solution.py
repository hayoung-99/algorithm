from typing import List

from pydantic import BaseModel
from numpy import argmin


class Param(BaseModel):
    full_length: int
    number_of_sector: int
    fuel_size: int
    path: List[int]


def parse_input(path: str):
    with open(path, "r") as file:
        text = [line.replace("\n", "").split(" ") for line in file.readlines()]
    data = [[int(n) for n in t] for t in text]
    head = data.pop(0)
    [full_length, number_of_sector, fuel_size] = head
    landing_fuel_values = data.pop(number_of_sector)
    landing_fuel = lambda i: landing_fuel_values[i - 1]
    sky_path = data.pop()
    return (
        Param(
            full_length=full_length,
            number_of_sector=number_of_sector,
            fuel_size=fuel_size,
            path=sky_path,
        ),
        landing_fuel,
        data,
    )


def get_min_distance(distance_map: List[List[int]], _from: int, _to: int):
    copied_map = list(distance_map)
    limited_distance = copied_map[_from - 1][_to - 1]
    distance = 0
    s = _from
    while distance < limited_distance:
        copied_map[s - 1][s - 1] = 1000000
        e = argmin(copied_map[s - 1]) + 1
        distance += copied_map[s - 1][e - 1]
        if e == _to:
            return distance
        s = e
    return limited_distance


def get_max_sector(param: Param, landing_fuel):

    return


def test_1():
    input_1 = "../input1.txt"
    param, landing_fuel, distance_map = parse_input(input_1)
    path = param.path
    start = 1
    print(get_min_distance(distance_map, 1, 3))


test_1()
