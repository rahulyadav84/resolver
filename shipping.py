import iso6346


class ShippingContainer:
    container_num = 100001

    WIDTH_FT = 10
    HEIGHT_FT = 20

    @classmethod
    def _get_next_num(cls):
        cls.container_num += 1
        return cls.container_num

    @staticmethod
    def _get_iso6346_num(owner_code, container_num):
        return iso6346.create(owner_code=owner_code, serial=str(container_num).zfill(6))

    def __init__(self, owner, length_ft, contents):
        self.owner = owner
        self.contents = contents
        self.length_ft = length_ft
        self.num = self._get_iso6346_num(owner_code=owner,
                                         container_num=ShippingContainer._get_next_num()
                                         )

    @classmethod
    def create_with_items(cls, owner, items):
        return cls(owner, list(items))

    @staticmethod
    def create_with_item(owner, items):
        return ShippingContainer(owner, list(items))

    @property
    def vol_ft(self):
        self._calc_val_ft()

    def _calc_vol_ft(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft


class RefrigeratorShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4

    FRIDGE_VOL_FT = 100

    @classmethod
    def get_max_celsius(cls):
        return cls.MAX_CELSIUS

    @staticmethod
    def _get_iso6346_num(owner_code, container_num):
        return iso6346.create(owner_code=owner_code, serial=str(container_num).zfill(6), category='R')

    def __init__(self, owner, celsius, contents, length_ft):
        super().__init__(owner, length_ft, contents)
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, celsius):
        self._set_celsius(celsius)

    @property
    def fahrenheit(self):
        return (self.celsius * 9 / 5) + 32

    @fahrenheit.setter
    def fahrenheit(self, temp):
        self.celsius = (temp - 32) * 5 / 9

    @property
    def vol_ft(self):
        return super().vol_ft - self.FRIDGE_VOL_FT

    def _set_celsius(self, celsius):
        if celsius > self.MAX_CELSIUS:
            raise ValueError("Too hot for container")
        self._celsius = celsius

    def _calc_vol_ft(self):
        return super()._calc_vol_ft() - self.FRIDGE_VOL_FT


class HeatedRefrigeratorShippingContainer(RefrigeratorShippingContainer):
    MIN_CELSIUS = -20

    def __init(self, owner_code, contents, length_ft, celsius):
        super().__init__(owner_code=owner_code, celsius=celsius, contents=contents, length_ft=length_ft)

    def _set_celsius(self, celsius):
        if celsius < self.MIN_CELSIUS:
            raise ValueError("Temperature too low")
        super()._set_celsius(celsius)

    def __repr__(self):
        return 'HeatedRefrigeratorShippingContainer(temperature_celsius{},length_ft{})'.format(length_ft=self.length_ft,
                                                                                               temperature_celsius=
                                                                                               self.celsius)
