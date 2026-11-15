
__declspec(dllexport) int add(int a, int b) {
    return a + b;
}

__declspec(dllexport) void square_numbers(int* numbers, int length) {
    for (int i = 0; i < length; i++) {
        numbers[i] = numbers[i] * numbers[i];
    }
}
