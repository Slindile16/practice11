import pytest
from main import (
    even_odd_tracker,
    temperature_filter,
    calculate_order_total,
    process_scores,
    organize_products,
    sequence_growth,
)

class TestMockExamVariants:
    

    # ========================================================================
    # QUESTION 1 TESTS: even_odd_tracker
    # ========================================================================

    def test_even_odd_tracker_mixed_large_small(self):
        assert even_odd_tracker([0, -1, 99, 100]) == ["Even", "Odd", "Odd", "Even"]

    def test_even_odd_tracker_repeated_numbers(self):
        assert even_odd_tracker([2, 2, 3, 3]) == ["Even", "Even", "Odd", "Odd"]

    def test_even_odd_tracker_all_zero(self):
        assert even_odd_tracker([0, 0, 0]) == ["Even", "Even", "Even"]

    def test_even_odd_tracker_large_negative_numbers(self):
        assert even_odd_tracker([-100, -101, -102]) == ["Even", "Odd", "Even"]

    def test_even_odd_tracker_alternating_pattern(self):
        assert even_odd_tracker([1, 2, 3, 4, 5, 6]) == ["Odd", "Even", "Odd", "Even", "Odd", "Even"]

    # ========================================================================
    # QUESTION 2 TESTS: temperature_filter
    # ========================================================================

    def test_temperature_filter_inside_range(self):
        assert temperature_filter([18, 19, 23, 25]) == [18, 19, 23, 25]

    def test_temperature_filter_outside_extreme(self):
        assert temperature_filter([-60, -51, 61, 62]) == []

    def test_temperature_filter_mixed_valid_invalid(self):
        assert temperature_filter([-55, 18, 20, 30, 61]) == [18, 20]

    def test_temperature_filter_boundary_values(self):
        assert temperature_filter([17, 18, 25, 26]) == [18, 25]

    def test_temperature_filter_single_invalid(self):
        assert temperature_filter([61]) == []

    # ========================================================================
    # QUESTION 3 TESTS: calculate_order_total
    # ========================================================================


    def test_calculate_order_total_exactly_minimum(self):
        assert calculate_order_total(10, 4) == 50  # 10+40=50 → stays


    def test_calculate_order_total_no_bonus(self):
        assert calculate_order_total(10, 4) == 50  # no bonus for <5

    def test_calculate_order_total_large_price_quantity(self):
        assert calculate_order_total(100, 20) == 10 + 2000 + 20  # 2030

    # ========================================================================
    # QUESTION 4 TESTS: process_scores
    # ========================================================================

    def test_process_scores_all_high(self):
        assert process_scores([80, 90, 100]) == "All scores processed"

    def test_process_scores_score_below_middle(self):
        assert process_scores([60, 50, 39, 80]) == "Stopped early at score 39"

    def test_process_scores_score_below_first(self):
        assert process_scores([35, 60, 70]) == "Stopped early at score 35"

    def test_process_scores_score_below_last(self):
        assert process_scores([50, 60, 38]) == "Stopped early at score 38"

    def test_process_scores_multiple_below(self):
        assert process_scores([45, 30, 25, 20]) == "Stopped early at score 30"

    # ========================================================================
    # QUESTION 5 TESTS: organize_products
    # ========================================================================

    def test_organize_products_multiple_categories(self):
        items = [
            {"name": "Soda", "category": "Drinks"},
            {"name": "Juice", "category": "Drinks"},
            {"name": "Chocolate", "category": "Snacks"},
            {"name": "Chips", "category": "Snacks"},
        ]
        expected = {"Drinks": ["Soda", "Juice"], "Snacks": ["Chocolate", "Chips"]}
        assert organize_products(items) == expected

    def test_organize_products_single_category(self):
        items = [{"name": "Egg", "category": "Dairy"}, {"name": "Milk", "category": "Dairy"}]
        expected = {"Dairy": ["Egg", "Milk"]}
        assert organize_products(items) == expected

    def test_organize_products_unique_categories(self):
        items = [
            {"name": "Apple", "category": "Fruit"},
            {"name": "Carrot", "category": "Vegetable"},
            {"name": "Beef", "category": "Meat"},
        ]
        expected = {"Fruit": ["Apple"], "Vegetable": ["Carrot"], "Meat": ["Beef"]}
        assert organize_products(items) == expected

    def test_organize_products_repeated_names_different_category(self):
        items = [
            {"name": "Milk", "category": "Dairy"},
            {"name": "Milk", "category": "Beverages"},
        ]
        expected = {"Dairy": ["Milk"], "Beverages": ["Milk"]}
        assert organize_products(items) == expected

    def test_organize_products_empty_list(self):
        assert organize_products([]) == {}

    # ========================================================================
    # QUESTION 6 TESTS: sequence_growth
    # ========================================================================

    def test_sequence_growth_multiple_gaps(self):
        assert sequence_growth([1, 3, 2, 4, 5, 1, 2]) == 3  # [2,4,5]

    def test_sequence_growth_decreasing_then_increasing(self):
        assert sequence_growth([5, 4, 3, 1, 2, 3, 4]) == 4  # [1,2,3,4]

    def test_sequence_growth_all_equal(self):
        assert sequence_growth([2, 2, 2, 2]) == 1

    def test_sequence_growth_alternating_up_down(self):
        assert sequence_growth([1, 2, 1, 2, 1, 2, 1]) == 2

    def test_sequence_growth_negative_and_positive_mixed(self):
        assert sequence_growth([-5, -4, -3, 0, 1, -2, -1, 0, 1, 2]) == 5  # longest [-5..1]
