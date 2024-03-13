ArrayList<Individuals> herd = new ArrayList<Individuals>();
int N = 10;

class Individual {
  PVector direction;
  float dist_min, dist_max; // want a kind of thresholded gaussian here
  float strength;
  float mass;

  PVector global_goal;
  PVector location;

  public Individual(PVector location, float dmin, float dmax, float strength, float mass) {
    this.location = location;
    this.dist_min = dmin;
    this.dist_max = dmax;
    this.strength = strength;
    this.mass = mass;
  }

  public void draw() {
    circle(location.x, location.y, mass);
  }

  public void update() {

  }
  
  public void setGoal(PVector goal) { this.global_goal = goal; }
}

void setup() {
  size(400, 400);

  for (int i = 0; i < N; i++) {
    herd.add(new Individual(new PVector(random(400), random(400)), 10, 20, 1, 20));
  }
}

void draw() {
  for (Individual i : herd) {
    i.update();
    i.draw();
  }
}
