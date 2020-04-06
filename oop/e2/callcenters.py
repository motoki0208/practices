from operators import Operator, Manager, Director


class Call:
    def __init__(self, id, level):
        self.id = id
        self.level = level

    def __str__(self):
        return f"問い合わせ{self.id}(難易度: {self.level.name})"


class CallCenter:
    def __init__(self, all_operators):
        self.operators = []
        self.managers = []
        self.directors = []

        for operator in all_operators:
            if isinstance(operator, Operator):
                self.operators.append(operator)
                continue

            if isinstance(operator, Manager):
                self.managers.append(operator)
                continue

            if isinstance(operator, Director):
                self.directors.append(operator)
                continue

            raise Exception("該当するクラスがありませんでした")

    def dispatch_call(self, call):
        for operator in self.operators:
            if operator.can_deal(call):
                operator.deal(call)
                return

        for manager in self.managers:
            if manager.can_deal(call):
                manager.deal(call)
                return

        for director in self.directors:
            if director.can_deal(call):
                director.deal(call)
                return

        print(f"現在{call}への応答ができません")


