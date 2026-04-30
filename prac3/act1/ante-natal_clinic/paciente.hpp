#ifndef PACIENTE_HPP_
#define PACIENTE_HPP_

#include <eosim/core/bevent.hpp>
#include <eosim/core/entity.hpp>
#include <string>

//Identificador del evento de llegada
const std::string llegadaP = "LlegadaPaciente";

class LlegadaPaciente: public eosim::core::BEvent{
public:
    //Primero defino el constructor
    LlegadaPaciente(eosim::core::Model& model);
    //Luego defino el destructor
    ~LlegadaPaciente();
    //Rutina del evento
    void eventRoutine(eosim::core::Entity* who);
};

//identificador del evento de salida
const std::string salidaP = "SalidaPaciente";

class SalidaPaciente: public eosim::core::BEvent{
public:
    //Primero defino el constructor
    SalidaPaciente(eosim::core::Model& model);
    //Luego defino el destructor
    ~SalidaPaciente();
    //Rutina del evento
    void eventRoutine(eosim::core::Entity* who);
};

#endif // PACIENTE_HPP_
