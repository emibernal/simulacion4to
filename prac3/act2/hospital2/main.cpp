#include <eosim/dist/mt19937.hpp>
#include <eosim/core/experiment.hpp>
#include "hospitalsimple.hpp"
#include "constantes.hpp"

#include <iostream>
#include <fstream>

const unsigned int repeticiones = 4;

int main () {
	std::string s;
    using namespace eosim::core;

    //Calculo del factor de utilizacion
    double factorUtilizacion = (1.0/tasaArribos * tiempoEstadia) / cantCamas;
    //Lo imprimo
    std::cout << "Factor de utilizacion: " << factorUtilizacion << "\n\n";

    //repito el experimento una cierta cantidad de veces
    for (int i = 0; i < repeticiones; i++) {
        HospitalSimple m(cantCamas, tasaArribos, tiempoEstadia);
        Experiment e;
        std::cout << "Arranco ...\n";
        m.connectToExp(&e);
        e.setSeed((unsigned long) i + 129);
        e.run(10000); //Experimento con 10000
        std::cout << "Termine ...\n\n\n";
		m.lCola.print(0);
		std::cout << '\n';
		m.tEspera.print(0);
		std::cin >> s;
    }
}

