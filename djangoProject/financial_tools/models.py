# financial_tools/models.py

from django.db import models
from decimal import Decimal

class BudgetingTool(models.Model):
    title = models.CharField(max_length=100)
    planned_budget = models.DecimalField(max_digits=12, decimal_places=2)
    actual_budget = models.DecimalField(max_digits=12, decimal_places=2)

    @property
    def deviation(self):
        return self.actual_budget - self.planned_budget

    @property
    def deviation_percent(self):
        if self.planned_budget:
            return (self.deviation / self.planned_budget) * 100
        return Decimal("0.0")

class CashFlowForecast(models.Model):
    title = models.CharField(max_length=100)
    inflow = models.DecimalField(max_digits=12, decimal_places=2)
    outflow = models.DecimalField(max_digits=12, decimal_places=2)

    @property
    def net_cash_flow(self):
        return self.inflow - self.outflow

    @property
    def status(self):
        return "مثبت" if self.net_cash_flow >= 0 else "منفی"



class BreakEvenAnalysis(models.Model):
    title = models.CharField(max_length=100)
    fixed_cost = models.DecimalField(max_digits=12, decimal_places=2)
    variable_cost_per_unit = models.DecimalField(max_digits=12, decimal_places=2)
    price_per_unit = models.DecimalField(max_digits=12, decimal_places=2)

    @property
    def break_even_units(self):
        margin = self.price_per_unit - self.variable_cost_per_unit
        return self.fixed_cost / margin if margin > 0 else Decimal("0.0")


class ROITool(models.Model):
    title = models.CharField(max_length=100)
    gain = models.DecimalField(max_digits=12, decimal_places=2)
    cost = models.DecimalField(max_digits=12, decimal_places=2)

    @property
    def roi(self):
        return ((self.gain - self.cost) / self.cost) * 100 if self.cost else Decimal("0.0")

    @property
    def payback_period(self):
        return self.cost / self.gain if self.gain else None


class ValuationModel(models.Model):
    title = models.CharField(max_length=100)
    cash_flow = models.DecimalField(max_digits=12, decimal_places=2)
    discount_rate = models.FloatField()
    multiple = models.FloatField()

    @property
    def dcf_value(self):
        return self.cash_flow / Decimal(self.discount_rate) if self.discount_rate else Decimal("0.0")

    @property
    def multiple_value(self):
        return self.cash_flow * Decimal(self.multiple)
