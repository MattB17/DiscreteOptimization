#include <vector>
#include <string>
#include <iostream>
#include <sstream>

std::string solver(std::string &input_data) {
  std::stringstream input_stream(input_data);

  int item_count, capacity;
  input_stream >> item_count >> capacity;

  std::vector<int> values(item_count);
  std::vector<int> weights(item_count);
  for (size_t i = 0; i < item_count; i++) {
    input_stream >> values[i] >> weights[i];
  }

  int total_value = 0;
  std::vector<int> taken(item_count);
  for (size_t i = 0; i < item_count; i++) {
    if (weights[i] <= capacity) {
      total_value += values[i];
      capacity -= weights[i];
      taken[i] = 1;
    } else {
      taken[i] = 0;
    }
  }

  std::stringstream solution;
  solution << total_value << " " << 0 << "\n";
  if (item_count > 0) {
    for (size_t i = 0; i < item_count - 1; i++) {
      solution << taken[i] << " ";
    }
    solution << taken[item_count - 1] << "\n";
  }
  return solution.str();
}

int main() {
  std::string input_data = "4 11\n8 4\n10 5\n15 8\n4 3\n";
  std::cout << solver(input_data);
  return 0;
}
