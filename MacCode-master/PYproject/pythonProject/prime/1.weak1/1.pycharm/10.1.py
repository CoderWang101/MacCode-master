class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f"家具名称:{self.name}\t->\t放置家具所需面积:{self.area}"


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area  # 初始面积(家具可占用面积)
        self.item_list = []  # 放置家具列表

    def __str__(self):
        return "户型:{},总面积:{}[剩余:{},家具:{}]".format(
            self.house_type, self.area, self.free_area, self.item_list)

    def add_item(self, item: HouseItem):
        if self.free_area > item.area:
            print("{}放置成功".format(item.name))
            self.item_list.append(item.name)
            self.free_area -= item.area
        else:
            print("空间不足")


if __name__ == '__main__':
    bed = HouseItem("bed", 4)
    chest = HouseItem("chest", 10)
    table = HouseItem("table", 20)
    print(bed)

    house = House("三室一厅", 100)
    house.add_item(bed)
    house.add_item(chest)
    print(house)
