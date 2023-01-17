from typing import List

import sys


class Param:
    full_length: int
    number_of_sector: int
    fuel_size: int
    path: List[int]

    def __init__(
        self, full_length: int, number_of_sector: int, fuel_size: int, path: List[int]
    ) -> None:
        self.full_length = full_length
        self.number_of_sector = number_of_sector
        self.fuel_size = fuel_size
        self.path = path


class Result:
    consume_fuel: int
    own_flight_length: int

    def __init__(self, consume_fuel: int, own_flight_length: int) -> None:
        self.consume_fuel = consume_fuel
        self.own_flight_length = own_flight_length


def parse_input():
    a, b, c = list(map(int, input().split()))
    d = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(b + 2)]
    data = [[a, b, c], *d]
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
        min_index = min(
            [(i, v) for i, v in enumerate(copied_map[s - 1])], key=lambda x: x[1]
        )[0]
        e = min_index + 1
        distance += copied_map[s - 1][e - 1]
        if e == _to:
            return distance
        s = e
    return limited_distance


def get_consume_fuel_size(
    param: Param, distance_map: List[List[int]], landing_fuel, start: int, end: int
):
    start_path = param.path[start]
    start_landing_fuel = landing_fuel(start_path - 1)
    own_path = param.path[:start] + param.path[end:]
    s = 1
    flight_fuel = 0
    for e in own_path:
        flight_fuel += distance_map[s - 1][e - 1]
        s = e
    return Result(
        own_flight_length=len(own_path), consume_fuel=start_landing_fuel + flight_fuel
    )


def get_best_flight(param: Param, distance_map: List[List[int]], landing_fuel):
    case_values = [
        get_consume_fuel_size(param, distance_map, landing_fuel, i, j)
        for i in range(1, param.full_length)
        for j in range(i + 1, param.full_length)
    ]
    valid_flight = [c for c in case_values if c.consume_fuel <= param.fuel_size]
    if not valid_flight:
        return -1
    best_result = min(
        valid_flight,
        key=lambda x: (-x.own_flight_length, x.consume_fuel),
    )
    return param.full_length - best_result.own_flight_length, best_result.consume_fuel


def solution():
    param, landing_fuel, distance_map = parse_input()
    result = get_best_flight(param, distance_map, landing_fuel)
    print(result)
    return result


solution()
