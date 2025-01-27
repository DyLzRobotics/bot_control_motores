#include "ServoMotores.h"

// Constructor
ServoMotores::ServoMotores(int rx, int tx) {
    rxPin = rx;
    txPin = tx;
    softSerial = new SoftwareSerial(rxPin, txPin);  // Crear objeto SoftwareSerial
    softSerial->begin(9600);  // Inicializar comunicación a 9600 bps
}

// Método para esperar a "OK" en la comunicación serial
void ServoMotores::wait_serial_return_ok() {
    int num = 0;
    char c[16];
    while (1) {
        while (softSerial->available() > 0) {
            c[num] = softSerial->read();
            num++;
            if (num >= 15)
                num = 0;
        }
        if (c[num - 2] == 'O' && c[num - 1] == 'K')
            break;
    }
}

// Métodos para la Mano Derecha
void ServoMotores::AbrirManoD() {
    softSerial->print("#1PT\r\n"); // Motor 1
    softSerial->print("#2PT\r\n"); // Motor 2
    softSerial->print("#3PT\r\n"); // Motor 3
    softSerial->print("#4PT\r\n"); // Motor 4
    softSerial->print("#5PT\r\n"); // Motor 5
    softSerial->print("#6PT\r\n"); // Motor 6
    wait_serial_return_ok();
}

void ServoMotores::CerrarManoD() {
    softSerial->print("#1PT\r\n");
    softSerial->print("#2PT\r\n");
    softSerial->print("#3PT\r\n");
    softSerial->print("#4PT\r\n");
    softSerial->print("#5PT\r\n");
    softSerial->print("#6PT\r\n");
    wait_serial_return_ok();
}

void ServoMotores::RotarManoD() {
    softSerial->print("#7PT\r\n"); // Motor 7
    wait_serial_return_ok();
}

// Métodos para la Mano Izquierda
void ServoMotores::AbrirManoI() {
    softSerial->print("#29PT\r\n"); // Motor 29
    softSerial->print("#30PT\r\n"); // Motor 30
    softSerial->print("#31PT\r\n"); // Motor 31
    softSerial->print("#32PT\r\n"); // Motor 32
    softSerial->print("#28PT\r\n"); // Motor 28
    softSerial->print("#27PT\r\n"); // Motor 27
    wait_serial_return_ok();
}

void ServoMotores::CerrarManoI() {
    softSerial->print("#29PT\r\n");
    softSerial->print("#30PT\r\n");
    softSerial->print("#31PT\r\n");
    softSerial->print("#32PT\r\n");
    softSerial->print("#28PT\r\n");
    softSerial->print("#27PT\r\n");
    wait_serial_return_ok();
}

void ServoMotores::RotarManoI() {
    softSerial->print("#26PT\r\n"); // Motor 26
    wait_serial_return_ok();
}

// Métodos para el Codo Derecho
void ServoMotores::SubirCodoD() {
    softSerial->print("#8PT\r\n"); // Motor 8
    wait_serial_return_ok();
}

void ServoMotores::BajarCodoD() {
    softSerial->print("#8PT\r\n"); // Motor 8
    wait_serial_return_ok();
}

void ServoMotores::RotarCodoD() {
    softSerial->print("#9PT\r\n"); // Motor 9
    wait_serial_return_ok();
}

// Métodos para el Codo Izquierdo
void ServoMotores::SubirCodoI() {
    softSerial->print("#25PT\r\n"); // Motor 25
    wait_serial_return_ok();
}

void ServoMotores::BajarCodoI() {
    softSerial->print("#25PT\r\n");
    wait_serial_return_ok();
}

void ServoMotores::RotarCodoI() {
    softSerial->print("#24PT\r\n"); // Motor 24
    wait_serial_return_ok();
}

// Métodos para el Hombro Derecho
void ServoMotores::FrontalHombroD() {
    softSerial->print("#11PT\r\n"); // Motor 11
    wait_serial_return_ok();
}

void ServoMotores::BajarHombroD() {
    softSerial->print("#11PT\r\n");
    wait_serial_return_ok();
}

void ServoMotores::DerechoHombro() {
    softSerial->print("#10PT\r\n"); // Motor 10
    wait_serial_return_ok();
}

// Métodos para el Hombro Izquierdo
void ServoMotores::FrontalHombroI() {
    softSerial->print("#22PT\r\n"); // Motor 22
    wait_serial_return_ok();
}

void ServoMotores::BajarHombroI() {
    softSerial->print("#22PT\r\n");
    wait_serial_return_ok();
}

void ServoMotores::IzquierdoHombro() {
    softSerial->print("#22PT\r\n");
    wait_serial_return_ok();
}
