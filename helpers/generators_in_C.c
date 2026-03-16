#include <stdio.h>
#include <stdlib.h>

// 1. Define the State Object
typedef struct {
    int current;
} NumberGenerator;

// 2. The Initialization Function
NumberGenerator* create_generator() {
    NumberGenerator* gen = malloc(sizeof(NumberGenerator));
    gen->current = 0;
    return gen;
}

// 3. The "Next" Function
int next_even(NumberGenerator* gen) {
    gen->current += 2;
    return gen->current;
}

int main() {
    // We can now have multiple independent generators!
    NumberGenerator* gen_A = create_generator();
    NumberGenerator* gen_B = create_generator();

    printf("A: %d\n", next_even(gen_A)); // Outputs: 2
    printf("B: %d\n", next_even(gen_B)); // Outputs: 2
    printf("A: %d\n", next_even(gen_A)); // Outputs: 4

    free(gen_A);
    free(gen_B);
    return 0;
}