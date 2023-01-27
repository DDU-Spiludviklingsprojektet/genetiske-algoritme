void setup() {

class Item {
    String name;
    int weight;
    int value;
  }

  String[] lines =  loadStrings("data/data.txt");

  ArrayList<Item> Items = new ArrayList<Item>();

  for (int i = 0; i < lines.length; i++) {
      String[] words = split(lines[i], " ");
      Item ting = new Item();
      ting.name = words[0];
      ting.weight = int(words[1]);
      ting.value = int(words[2]);
      Items.add(ting);
  }

class Backpack {
  float maxWeight;
  float currentWeight;
  float currentCost;
  ArrayList<Item> itemsInBackpack;

  Backpack() {
    this.maxWeight = 5000;
    this.currentWeight = 0;
    this.currentCost = 0;
    this.itemsInBackpack = new ArrayList<Item>();
  }

  void addItem(Item newItem) {
    if (currentWeight + newItem.weight <= maxWeight) {
      itemsInBackpack.add(newItem);
      currentWeight += newItem.weight;
      currentCost += newItem.value;
    }
  }
}

class Population1 {
  int populationSize = 200;
  ArrayList<Backpack> backpacks;
  
  Population(int populationSize) {
    this.populationSize = populationSize;
    backpacks = new ArrayList<Backpack>(populationSize);
    for (int i = 0; i < populationSize; i++) {
      backpacks.add(new Backpack());
    }
  }

  void generateRandomPopulation(ArrayList[] items) {
    for (int i = 0; i < populationSize; i++) {
      for (int j = 0; j < items.length; j++) {
        if (random(1) < 0.5) {
          backpacks(i).addItem.itemsInBackpack(items[j]);
          //backpacks[i].addItem(items[j]);
        }
      }
    }
  }
}

generateRandomPopulation(Items);

}

void draw() {
}
  Backpack[] population = new Backpack(200);

