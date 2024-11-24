#include <iostream>
#include <random>
#include <fstream>

// Проверка находится ли точка в пересечении
bool isInCircles(double x, double y) {
    return (std::pow(x - 1, 2) + std::pow(y - 1, 2) <= 1) &&
           (std::pow(x - 1.5, 2) + std::pow(y - 2, 2) <= 5.0 / 4.0) &&
           (std::pow(x - 2, 2) + std::pow(y - 1.5, 2) <= 5.0 / 4.0);
}
// Расчет площади перекрытия
double monteCarlo(int N, double xMin, double xMax, double yMin, double yMax) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> disX(xMin, xMax);
    std::uniform_real_distribution<> disY(yMin, yMax);

    int M = 0;
    for (int i = 0; i < N; ++i) {
        double x = disX(gen);
        double y = disY(gen);
        if (isInCircles(x, y)) {
            ++M;
        }
    }

    double areaRec = (xMax - xMin) * (yMax - yMin);
    return static_cast<double>(M) / N * areaRec;
}

int main() {
    std::ofstream dataFile("../results.csv");
    dataFile << "N,Approximation,Error\n";

    const double exactArea = 0.25 * M_PI + 1.25 * asin(0.8) - 1;
    const double xMin = 0;
    const double xMax = 3;
    const double yMin = 0;
    const double yMax = 3;

    for (int N = 100; N <= 100000; N += 500) {
        double approx = monteCarlo(N, xMin, xMax, yMin, yMax);
        double error = abs(approx - exactArea) / exactArea * 100.0;
        dataFile << N << "," << approx << "," << error << "\n";
        std::cout << "N: " << N << ", Approximation: " << approx << ", Error: " << error << "%\n";
    }

    dataFile.close();
    return 0;
}
