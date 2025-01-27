#ifndef MYLIBRARY_H
#define MYLIBRARY_H

#include <SoftwareSerial.h>

class ServoMotores {
  private:
    int rxPin;  // Pin RX del SoftwareSerial
    int txPin;  // Pin TX del SoftwareSerial
    SoftwareSerial* softSerial;  // Puntero al objeto SoftwareSerial

  public:
    ServoMotores(int rx, int tx);  // Constructor para inicializar los pines

    // Función para esperar "OK"
    void wait_serial_return_ok();

    // Funciones para la mano
    void AbrirManoI();
    void CerrarManoI();
    void RotarManoI();

    void RotarManoD();
    void CerrarManoD();
    void AbrirManoD();

    // Funciones para el codo
    void SubirCodoI();
    void BajarCodoI();
    void RotarCodoI();

    void SubirCodoD();
    void BajarCodoD();
    void RotarCodoD();

    // Funciones para el hombro
    void FrontalHombroI();
    void BajarHombroI();
    void IzquierdoHombro();

    void DerechoHombro();
    void FrontalHombroD();
    void BajarHombroD();
};

#endif
