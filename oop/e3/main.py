from parkinglot import Car, ParkingLot, ParkingSpace


def main():
    cars = [
        Car(number=1111),
        Car(number=1112),
        Car(number=1113),
        Car(number=1114),
        Car(number=1115),
        Car(number=1116),
        Car(number=1117),
        Car(number=1118),
        Car(number=1119),
    ]
    parking_lot = ParkingLot(
        parking_spaces=[
            ParkingSpace(number=1),
            ParkingSpace(number=2),
            ParkingSpace(number=3),
            ParkingSpace(number=4),
            ParkingSpace(number=5),
            ParkingSpace(number=6),
            ParkingSpace(number=7),
            ParkingSpace(number=8),
        ]
    )

    for car in cars:
        car.enter(parking_lot)

    for car in cars[:-1]:
        car.depart(parking_lot)


if __name__ == "__main__":
    main()
