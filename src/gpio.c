/**
 * GPIO_C
 * @author K Gledson
 * @version 2021-01-21
 * Functions needed to communicate with the General-Purpose Input/Output Expander (GPIO XPNDR) chips
 */

#include "gpio.h"

void initGPIO(void){
    /* Initializes the GPIOs over SPI.     */
	initGPIO1();
	initGPIO2();
	initGPIO3();
	initGPIO4();
}//initGPIO

void initIOCON(uint8_t CS){
	uint32_t config = (GPIO_OPCODE_WRITE<<16)+(GPIO_SELECT_IOCON<<8)+ALL_OUTPUT;		//ensure IOCON register is configured correctly
	message_32b configMsg = msgMkr(config,24);
	writeSPI(CS, configMsg);
}

void initGPIO1(void){
	uint32_t portA = (GPIO_OPCODE_WRITE<<16)+(GPIO_SELECT_DIRA<<8)+ALL_INPUT;			//opcode to make A0-7 inputs
	uint32_t portB = (GPIO_OPCODE_WRITE<<16)+(GPIO_SELECT_DIRB<<8)+ALL_OUTPUT;			//opcode to make B0-7 outputs
	message_32b messageA = msgMkr(portA,24);											//assign all input message for SPI
	message_32b messageB = msgMkr(portB,24);											//assign all output message for SPI
	initIOCON(GPIO1_CS);
	writeSPI(GPIO1_CS,messageA);                                                        //Write Port A configuration over SPI
	writeSPI(GPIO1_CS,messageB);                                                        //Write Port B configuration over SPI
}

void initGPIO2(void){
	uint32_t portA = (GPIO_OPCODE_WRITE<<16)+(GPIO_SELECT_DIRA<<8)+ALL_INPUT;			//opcode to make A0-7 inputs
	uint32_t portB = (GPIO_OPCODE_WRITE<<16)+(GPIO_SELECT_DIRB<<8)+ALL_INPUT;			//opcode to make B0-7 inputs
	message_32b messageA = msgMkr(portA,24);											//assign all input message for SPI
	message_32b messageB = msgMkr(portB,24);											//assign all output message for SPI
	initIOCON(GPIO2_CS);
	writeSPI(GPIO2_CS,messageA);                                                        //Write Port A configuration over SPI
	writeSPI(GPIO2_CS,messageB);                                                        //Write Port B configuration over SPI
}

void initGPIO3(void){
	uint32_t portB = (GPIO_OPCODE_WRITE<<16)+(GPIO_SELECT_DIRB<<8)+ALL_INPUT;			//opcode to make B0-7 input
	message_32b messageB = msgMkr(portB,24);											//assign all input message for SPI
	initIOCON(GPIO3_CS);
	writeSPI(GPIO3_CS,messageB);                                                        //Write Port B configuration over SPI
}

void initGPIO4(void){
	uint32_t portA = (GPIO_OPCODE_WRITE<<16)+(GPIO_SELECT_DIRA<<8)+0b00111111;			//A0-5 inputs, A6-7 outputs
	uint32_t portB = (GPIO_OPCODE_WRITE<<16)+(GPIO_SELECT_DIRB<<8)+ALL_INPUT;			//B0-7 all inputs
	message_32b messageA = msgMkr(portA,24);
	message_32b messageB = msgMkr(portB,24);
	initIOCON(GPIO4_CS);
	writeSPI(GPIO4_CS,messageA);                                                        //Write Port A configuration over SPI
	writeSPI(GPIO4_CS,messageB);                                                        //Write Port B configuration over SPI
}

void writeGPIO(uint8_t CS, uint16_t bank, uint8_t byte){
	/* @param CS	selects the chip to communicate with
	 * @param bank	selects the side of the GPIO to write to (A or B)
	 * @param byte	the state written to the GPIO pin (HIGH or LOW)
	 */
    uint32_t operation = (GPIO_OPCODE_WRITE<<16)+(bank<<8)+byte;
    message_32b message = msgMkr(operation,24);
    writeSPI(CS,message);
}//writeGPIO


uint16_t readGPIO(uint8_t CS, uint8_t bank){
	/* Reads and returns the data on one side of the GPIO.
	 * @param CS	selects the chip to communicate with
	 * @param bank	selects the side of the GPIO to read (A or B)
	 */
    uint16_t operation = (GPIO_OPCODE_READ<<8)+bank;
    message_32b message = msgMkr(operation, 16);
    writeSPI(CS, message);
    return readSPI(CS,BANK_SIZE); //can the size of this be trimmed to 8 bits?
}//readGPIO


