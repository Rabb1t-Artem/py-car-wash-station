class Car:
    def __init__(
        self, comfort_class: int, clean_mark: int, brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: int,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
        ) / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rating: float) -> None:
        total_rating = self.average_rating * self.count_of_ratings + new_rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)


bmw = Car(3, 3, "BMW")
audi = Car(4, 9, "Audi")
mercedes = Car(7, 1, "Mercedes")

ws = CarWashStation(6, 8, 3.9, 11)

income = ws.serve_cars([bmw, audi, mercedes])
print(f"income={income}")  # 41.7
print(f"bmw.clean_mark={bmw.clean_mark}")  # 8
print(f"audi.clean_mark={audi.clean_mark}")  # 9
print(f"mercedes.clean_mark={mercedes.clean_mark}")  # 8

ford = Car(2, 1, "Ford")
wash_cost = ws.calculate_washing_price(ford)
print(f"wash_cost={wash_cost}")  # 9.1
print(f"ford.clean_mark={ford.clean_mark}")  # 1

ws.rate_service(5)

print(f"count_of_ratings={ws.count_of_ratings}")  # 12
print(f"average_rating={ws.average_rating}")  # 4.0
