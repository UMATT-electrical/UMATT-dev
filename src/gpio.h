#ifndef UMATT_GPIO_H_
#define UMATT_GPIO_H_

#include <stdint.h>
#include "definitions.h"
#include "spi.h"

//Specification page 15 figure 3-5
#define GPIO_OPCODE_WRITE       0b01000000
#define GPIO_OPCODE_READ        0b01000001
//Specification page 16 table 3-3 (default)
//I/O direction register controls the direction of data I/O (spec: 3.5.1)
#define GPIO_SELECT_DIRA		0x00
#define GPIO_SELECT_DIRB		0x01
//GPIO Port register reflects the value of this port (spec: 3.5.10)
#define GPIO_SELECT_PORTA		0x12
#define GPIO_SELECT_PORTB		0x13
//Pull-Up resistor configuration register (spec: 3.5.7)
#define GPIO_SELECT_GPPUA       0x0C
//Interrupt Control register (spec: 3.5.5)
#define GPIO_SELECT_IOCON		0x0A

#define GPIO_INIT_DELAY			10
//IODIR configuration (spec: 3.5.1)
#define ALL_OUTPUT				0b00000000
#define ALL_INPUT				0b11111111

#define GPPUA_ENABLE_ALL        0b11111111
#define BANK_SIZE				8

void initGPIO(void);
void initGPIO1(void);
void initGPIO2(void);
void initGPIO3(void);
void initGPIO4(void);
void initIOCON(uint8_t CS);
void writeGPIO(uint8_t CS, uint16_t bank, uint8_t byte);
uint16_t readGPIO(uint8_t CS, uint8_t bank);

#endif
