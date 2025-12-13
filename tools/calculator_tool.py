from utils.calculator import Calculator
from typing import List
from langchain.tools import tool

class CalculatorTool:
    def __init__(self):
        self.calculator = Calculator()
        self.calculator_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Setup all tools for the calculator tool"""
        import re
        def extract_number(value: str) -> float:
            match = re.search(r"[\d.]+", value.replace(",", ""))
            return float(match.group()) if match else 0.0

        @tool
        def estimate_total_hotel_cost(price_per_night: str, total_days: float) -> float:
            """Calculate total hotel cost"""
            price = extract_number(price_per_night)
            return price * float(total_days)
        
        @tool
        def calculate_total_expense(costs: list) -> float:
            """Calculate total expense of the trip"""
            numeric_costs = []
            for cost in costs:
                if isinstance(cost, dict):
                    numeric_costs.append(float(cost.get('value', cost.get('amount', 0))))
                elif isinstance(cost, (int, float)):
                    numeric_costs.append(float(cost))
                elif isinstance(cost, str):
                    numeric_costs.append(float(cost))
            return self.calculator.calculate_total(*numeric_costs)
        
        @tool
        def calculate_daily_expense_budget(total_cost: float, days: int) -> float:
            """Calculate daily expense"""
            return self.calculator.calculate_daily_budget(total_cost, days)
        
        return [estimate_total_hotel_cost, calculate_total_expense, calculate_daily_expense_budget]