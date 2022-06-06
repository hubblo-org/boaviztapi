import boaviztapi.utils.roundit as rd
from boaviztapi.model.component.component import Component, NumberSignificantFigures
from boaviztapi.dto.component import PowerSupply


class ComponentPowerSupply(Component):

    DEFAULT_POWER_SUPPLY_WEIGHT = 2.99

    IMPACT_FACTOR = {
        'gwp': {
            'impact': 24.30
        },
        'pe': {
            'impact': 352.00
        },
        'adp': {
            'impact': 8.30E-03
        }
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__weight = self.DEFAULT_POWER_SUPPLY_WEIGHT

        for attr, val in kwargs.items():
            if val is not None:
                self.__setattr__(attr, val)

    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, value: float) -> None:
        self.__weight = value

    def impact_manufacture_gwp(self) -> NumberSignificantFigures:
        return self.__impact_manufacture('gwp')

    def __impact_manufacture(self, impact_type: str) -> NumberSignificantFigures:
        power_supply_impact = self.IMPACT_FACTOR[impact_type]['impact']
        impact = self.__compute_impact_manufacture(power_supply_impact)
        sign_figures = rd.min_significant_figures(power_supply_impact)
        return impact, sign_figures

    def __compute_impact_manufacture(self, power_supply_impact: float) -> float:
        return self.weight * power_supply_impact

    def impact_manufacture_pe(self) -> NumberSignificantFigures:
        return self.__impact_manufacture('pe')

    def impact_manufacture_adp(self) -> NumberSignificantFigures:
        return self.__impact_manufacture('adp')

    def impact_use_gwp(self, model=None) -> NumberSignificantFigures:
        raise NotImplementedError

    def impact_use_pe(self, model=None) -> NumberSignificantFigures:
        raise NotImplementedError

    def impact_use_adp(self, model=None) -> NumberSignificantFigures:
        raise NotImplementedError

    @classmethod
    def from_dto(cls, power_supply: PowerSupply) -> 'ComponentPowerSupply':
        return cls(**power_supply.dict())