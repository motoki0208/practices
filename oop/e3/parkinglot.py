from datetime import datetime


class Car:
    """ 車
    """

    def __init__(self, number):
        self.number = number

    def enter(self, parking_lot):
        parking_lot.dispatch(self)

    def depart(self, parking_lot):
        parking_lot.make_car_depart(self)


class ParkingSpace:
    """ 駐車場内の個々の駐車スペース
    """

    def __init__(self, number: int):
        self.number = number
        self.is_free = True

    def entered(self):
        self.is_free = False
        return

    @property
    def can_entry(self):
        return self.is_free


class ParkingHistory:
    """ 入出場記録
    """

    def __init__(self, car: Car, parking_space: ParkingSpace):
        self.car = car
        self.parking_space = parking_space
        self.entry_time = datetime.now()
        self.departure_time = datetime.max  # 生成時(つまり未出場の状態)はdatetime.max()が設定される

    def record_departure(self):
        """ 出場時間を記録する
        """
        self.departure_time = datetime.now()
        return

    @property
    def not_departed(self):
        """ 出場記録がない場合はTrueを返す
        """
        return self.departure_time == datetime.max


class ParkingLot:
    """ 駐車場
    """

    def __init__(
        self,
        parking_spaces,
        # adjustment_logic
    ):
        self.parking_spaces = parking_spaces
        self.parking_histories = []
        # self.adjustment_logic = adjustment_logic  TODO: 請求ロジックを持たせる

    def dispatch(self, car: Car):
        """ 車を空いている場所に駐車させる
        """
        for space in self.parking_spaces:
            if space.can_entry:
                self.make_car_entry(car, space)
                return

        # 空いている駐車場がない場合はその旨を表示
        print("駐車場は満車です")

    def make_car_entry(self, car: Car, space: ParkingSpace):
        """ 車を駐車スペースに駐車させる
        """
        space.entered()
        history = ParkingHistory(car=car, parking_space=space)
        self.parking_histories.append(history)
        print(f"車({car.number})がスペース{space.number}に停車しました 時間: {history.entry_time}")

    def make_car_depart(self, car: Car):
        """ 車を出場させる
        """
        histories = list(
            filter(lambda x: x.car == car and x.not_departed, self.parking_histories)
        )
        if not histories:
            raise Exception("入場記録不整合: この車の入場記録がありません %s", car.number)

        if len(histories) > 1:
            raise Exception("入場記録不整合: この車の未出場の入場記録が複数存在します %s", car.number)

        history = histories[0]
        self.adjust(
            # history=history
        )
        history.record_departure()
        space = history.parking_space
        space.is_free = True
        print(f"車({car.number})がスペース{space.number}から出車しました 時間: {history.departure_time}")

    def adjust(
        self,
        # history: ParkingHistory
    ):
        # TODO: 請求処理を実装
        print("料金を2,000円請求します")
        return
