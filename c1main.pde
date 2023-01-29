int itemlengt;
Backpack simon;

class Item {
  String name;
  int weight;
  int value;
}

void setup() {
    String[] lines =  loadStrings("data/data.txt");
  itemlengt = lines.length;

  Item[] Items = new Item[lines.length];

  for (int i = 0; i < lines.length; i++) {
    String[] words = split(lines[i], " ");
    Item ting = new Item();
    ting.name = words[0];
    ting.weight = int(words[1]);
    ting.value = int(words[2]);
    Items[i] = ting;
  }

  for (int i = 0; i < Items.length; i++) {
    println(Items[i].name + " " + Items[i].weight + " " + Items[i].value);
  }
  
  items_setup();
  //pop_setup();

  simon = Backpack();
}

void draw() {
}


class Backpack {
  float maxWeight;
  float currentWeight;
  float currentCost;
  Item[] itemsInBackpack;


  Backpack() {
    this.maxWeight = 5000;
    this.currentWeight = 0;
    this.currentCost = 0;
    this.itemsInBackpack = new Item[0];
  }

  //void addItem(Item newItem) {
  //  if (currentWeight + newItem.weight <= maxWeight) {
  //    currentWeight += newItem.weight;
  //    currentCost += newItem.value;
  //    append(itemsInBackpack, newItem);
  //  }
}
