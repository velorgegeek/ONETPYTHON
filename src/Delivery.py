from datetime import datetime, timedelta

valid_types = ["обычный", "хрупкий", "опасный"]
base_cost = 200
perUnitDistance = 5
maxWeight = 50
maxDistance = 5000
invalidResponse = -1,"0000-00-00"


def calculate_delivery_cost(weight: float, distance: int, package_type: str, is_express: bool = False) -> tuple:
    """
    Расчет стоимости и параметров доставки посылки.
    Возвращает: (стоимость_в_рублях, дата_доставки)
    В случае критических ошибок или неверных параметров возвращает (-1, "0000-00-00").
    """

    if weight < 0.1 or weight > maxWeight or distance < 1 or distance > maxDistance:
        return invalidResponse

    if package_type not in valid_types:
        return invalidResponse

    # Базовые тарифные сетки
    distance_cost = distance * perUnitDistance
    total_cost = base_cost + distance_cost

    # Рассчитываем весовые коэффициенты
    if weight > 5.0 and weight < 20.0:
        total_cost *= 1.2
    elif weight >= 20.0:
        total_cost *= 1.5

    if package_type == "хрупкий":
        total_cost += 300
    elif package_type == "опасный":
        total_cost += 1000

    if is_express:
        total_cost *= 0.5

    # Логика расчета времени транспортировки
    current_date = datetime.now()  # Фиксированная дата отправки

    days_needed = max(1, distance // 500)

    if is_express:
        days_needed = days_needed // 2

    delivery_date = current_date + timedelta(days=days_needed)

    return int(total_cost), delivery_date.strftime("%Y-%m-%d")
