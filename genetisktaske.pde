String[] lines =  loadStrings(data/data.txt);
println(lines.length);

class Obejct {
    String name;
    int weight;
    int value;
}

Object[] indehold = new Object[lines.length];

for(int i = 0; i < lines.length; i++) {
    String[] words = split(lines[i], " ");
    Object[i].name = words[0];
    Object[i].weight = int(words[1]);
    Object[i].value = int(words[2]);
}

class Rygsæk {
    float fitness;

    void fitness () {
        int score = 0;
        for (int i = 0; i < 10; i++) {
            
        }
    }
}