from tools.card_queries import (
    get_all_cards,
    get_card_by_id,
    get_card_by_name,
    get_price_history_by_card_id,
    get_price_history_by_card_name,
    get_latest_price_for_card_by_id,
    get_latest_price_for_card_by_name,
    analyze_price_trend_by_card_id,
    analyze_price_trend_by_name
)

card_tools = [
    get_all_cards,
    get_card_by_id,
    get_card_by_name,
    get_price_history_by_card_id,
    get_price_history_by_card_name,
    get_latest_price_for_card_by_id,
    get_latest_price_for_card_by_name,
    analyze_price_trend_by_card_id,
    analyze_price_trend_by_name
]