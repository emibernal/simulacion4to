#include "paciente.hpp"
#include "hospital1.hpp"
#include <iostream>

using namespace eosim::core;

//Constructor definido en paciente.hpp
LlegadaPaciente::LlegadaPaciente(Model& model): BEvent(llegadaP, model) {}

//Destructor definido en paciente.hpp
LlegadaPaciente::~LlegadaPaciente() {}

void LlegadaPaciente::eventRoutine(Entity* who) {
    //Llega el paciente
    std::cout << "Llega un paciente en " << who->getClock() << "\n";
    //Se castea owner a una clinica
    Clinica& c = dynamic_cast<Clinica&>(owner);
    if(c.enf.isAvailable(1)){
        //Si hay recursos disponibles
        c.enf.acquire(1);
        std::cout << "un paciente esta siendo atendido por una enfermera " << c.getSimTime() << "\n";
        c.tEspera.log(c.getSimTime() - who->getClock());
        c.schedule(c.estadia.sample(), who, salidaP);
    }else{
        //Si no hay recursos disponibles
        c.lCola.log(c.cola.size());
        //Se pone al paciente recien llegado en la cola
        c.cola.push(who);
    }
    //Por ultimo se agenda el arribo del nuevo paciente
    c.schedule(c.arribos.sample(), new Entity(), paciente);
}

//Constructor definido en paciente.hpp
SalidaPaciente::SalidaPaciente(Model& model): BEvent(salidaP, model) {}

SalidaPaciente:: ~SalidaPaciente() {}

void SalidaPaciente::eventRoutine(Entity* who) {
    //Se informa la salida de un paciente
    std::cout << "un paciente se retira en " << who->getClock() << "\n";
	// se castea owner a un HospitalSimple
	Clinica& c = dynamic_cast<Clinica&>(owner);
	// se retorna la cama que el paciente ocupaba
	c.enf.returnBin(1);
	if(!c.cola.empty()){
        c.enf.acquire(1);
        std::cout << "un paciente fue aceptado en una cama " << c.getSimTime() << "\n";
        c.lCola.log(c.cola.size());
        Entity* ent = c.cola.pop();
        c.tEspera.log(c.getSimTime() - ent->getClock());
        c.schedule(c.estadia.sample(), ent, salidaP);
	}
	//Por ultimo, eliminamos al paciente del sistema
    delete who;
}
