String[] lines =  loadStrings("data/data.txt");

class Ting {
  String name;
  int weight;
  int value;
}

ArrayList<Ting> indehold = new ArrayList<Ting>();

for (int i = 0; i < lines.length; i++) {
  String[] words = split(lines[i], " ");
  Ting ting = new Ting();
  ting.name = words[0];
  ting.weight = int(words[1]);
  ting.value = int(words[2]);
  indehold.add(ting);
}


class Rygsæk {
  void rygsæk() {
    for (int i = 0; i < rindhold.length; i++) {
      rindhold[i] = random(1) < 0.5;
    }
  }


  float fitness;
  boolean[] rindhold = new boolean[lines.length];
  //int[] indehold;
  int rweight;
  int rvalue;

  void fitness () {
    int score = 0;
    if (rweight > 5000) {
      score = 0;
    } else {
      score = rvalue;
    }
    fitness = score;
  }

  void weight() {
    int score = 0;
    for (int i = 0; i < rindhold.length; i++) {
      if (rindhold[i] == true) {
        Ting part = indehold.get(i);
        score += part.weight;
      }
    }
    rweight = score;
    println(rweight);
  }

void setup () {
  for (int i = 0; i < rygsækny.length; i++) 
  {
    rygsækny[i] = new Rygsæk();
  }
}
