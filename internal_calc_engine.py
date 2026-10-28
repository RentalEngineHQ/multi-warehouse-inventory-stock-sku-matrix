# RentalEngine HQ - Core Operational Calculation Array Matrix
def calculate_system_metrics(stock_on_hand, unit_cost, safety_threshold):
    total_asset_value = float(stock_on_hand) * float(unit_cost)
    reorder_alert_status = 1 if float(stock_on_hand) <= float(safety_threshold) else 0
    return total_asset_value, reorder_alert_status
