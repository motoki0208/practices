import random

from callcenters import CallCenter, Call
from consts import CallLevel
from operators import Operator, Manager, Director

if __name__ == "__main__":
    george = Director(name="george")
    frank = Manager(name="frank")
    ellen = Manager(name="ellen")
    dave = Operator(name="dave")
    carol = Operator(name="carol")
    bob = Operator(name="bob")
    alice = Operator(name="alice")

    operators = [george, frank, ellen, dave, carol, bob, alice]

    call_center = CallCenter(operators)
    calls = [Call(id=i, level=random.choices(list(CallLevel), weights=[60, 30, 10])[0]) for i in range(7)]
    for call in calls:
        call_center.dispatch_call(call)
