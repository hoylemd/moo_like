from ship import Ship

from time import sleep


def main():
    ship = Ship('Enterprise', 100, 150, 30, 75, 25)

    while ship._active:
        ship.take_damage(32)
        print ship.status_report()
        sleep(1)


if __name__ == '__main__':
    main()
