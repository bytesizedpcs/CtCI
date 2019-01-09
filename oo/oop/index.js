function Person(name, age, wealth) {
  this.name = name;
  this.age = age;
  this.wealth = wealth;
}

function Car(make, year, color, gasLevel) {
  this.make = make;
  this.year = year;
  this.color = color;
  this.gasLevel = gasLevel;
}

Car.prototype.worth = function() {
  return this.year - 20000;
}

Car.prototype.run = function () {
  if (this.gasLevel) {
    console.log('vroom vroom');
    this.gasLevel -= 1;
  } else {
    throw new Error('Car has no gas');
  }
}

Car.prototype.status = function() {

  console.log(`${this.gasLevel}`);

  if (this.gasLevel <= 0) {
    console.log('You need gas!');
    return false;
  } else {
    return true;
  }

}

const Worker = Object.create(Person);
console.log(typeof Worker);

const car = new Car('Bugatti', 2019, 'Red', 40);
const bum = new Car('Honda', 1980, 'brown', 0);

if (car.status()) car.run();
if (bum.status()) bum.run();

console.log(car.worth());

