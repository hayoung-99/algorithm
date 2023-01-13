from typing import List

from pydantic import BaseModel


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


def get_min_distanc(distance_map: List[List[int]], start: int, end: int):
    start_map = distance_map[start - 1]
    simple_start_to_end = start_map[end - 1]
    return


def test_1():
    input_1 = "../input1.txt"
    param, landing_fuel, distance_map = parse_input(input_1)
    path = param.path
    start = 1
