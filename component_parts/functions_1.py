import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "build_pc_1.settings")
import django

django.setup()
from component_parts.models import Case, PlayerAction


# from django.db import models

def tdp_is_dissipated(player_action_model):
    return player_action_model.cooling.dissipated_tdp > player_action_model.cpu.tdp


def no_empty_fields(player_action_model):
    to_check = [player_action_model.power_supply, player_action_model.cooling, player_action_model.ram,
                player_action_model.mother_board, player_action_model.cpu,
                player_action_model.hdd, player_action_model.video_card]
    for p in to_check:
        if p is None:
            return False
    return True


def budget_is_correct(player_action_model):
    player_components = [player_action_model.power_supply, player_action_model.cooling, player_action_model.ram,
                         player_action_model.mother_board, player_action_model.cpu,
                         player_action_model.hdd, player_action_model.video_card]
    component_prices = []
    budget = player_action_model.budget
    for component in player_components:
        component_prices.append(component.price)
    result_price = 0.0
    for p in component_prices:
        result_price += p
    return result_price <= budget


def power_supply_is_correct(player_action_model):
    components_to_check = [player_action_model.cooling, player_action_model.ram, player_action_model.mother_board,
                           player_action_model.cpu,
                           player_action_model.hdd, player_action_model.ssd, player_action_model.video_card]
    summary_power = 0.0
    for c in components_to_check:
        summary_power += c.power
    print(summary_power)
    return summary_power <= player_action_model.power_supply.power


# Cooling supports several sockets which must be inputted as string, separated by blank space in database
# and then splitted to list in def sockets_are_suitable


def sockets_are_suitable(player_action_model):
    cooling_sockets = player_action_model.cooling.supported_socket.split(', ')
    cooling_fits = False
    for socket in cooling_sockets:
        if player_action_model.cpu.socket == socket:
            cooling_fits = True
    return (player_action_model.mother_board.graphics_card_socket == player_action_model.video_card.socket) \
           & (player_action_model.mother_board.cpu_socket == player_action_model.cpu.socket) \
           & cooling_fits


def general_check_details(player_action_model):
    result = ''
    if not no_empty_fields(player_action_model):
        return 'Ошибка: Присутствуют пустые поля. Не все компоненты выбраны.'
    elif budget_is_correct(player_action_model) & power_supply_is_correct(player_action_model) \
            & sockets_are_suitable(player_action_model):
        return 'Кейс выполнен верно. Поздравляем!'
    if not budget_is_correct(player_action_model):
        result += "\n" + 'Ошибка: Вы превысили бюджет сборки!'
    if not power_supply_is_correct(player_action_model):
        result += "\n" + 'Ошибка: Неправильно подобран блок питания!'
    if not sockets_are_suitable(player_action_model):
        result += "\n" + 'Ошибка: несовпадение сокетов!'
    if not tdp_is_dissipated(player_action_model):
        result += "\n" + 'Ошибка: неверно подобрано охлаждение!'
    return result + "\n" + "Обнаружены ошибки"


def general_check_logical(player_action_model):
    result = False
    if no_empty_fields(player_action_model):
        return budget_is_correct(player_action_model) \
           & power_supply_is_correct(player_action_model) \
            & sockets_are_suitable(player_action_model)
    return result


