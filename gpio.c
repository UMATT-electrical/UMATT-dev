/**
 * GPIO_C
 * @author K Gledson
 * @version 2021-01-21
 * Functions needed to communicate with the General-Purpose Input/Output Expander (GPIO XPNDR) chips
 */

///////////////////////////////////////////////////////////////////////////////////////// included files (get rid of these later)
#include "stdint.h" //library not found on my computer.
#include "gpio.h"
///////////////////////////////////////////////////////////////////////////////////////// functions
void initGPIO(uint8_t CS){
    /* Initializes the GPIO over SPI.
     * Assigns register A as all input and register B as all output.
     * @param CS	selects the chip to communicate with
     */
    uint16_t input = (GPIO_OPCODE_WRITE<<16)+(GPIO_SELECT_DIRA<<8)+ALL_INPUT;			//opcode to make all pins inputs
    uint16_t output = (GPIO_OPCODE_WRITE<<16)+(GPIO_SELECT_DIRB<<8)+ALL_OUTPUT;			//opcode to make all pins outputs
    struct Message messageA = msgMkr(input,24);											//assign all input message for SPI
    struct Message messageB = msgMkr(output,24);										//assign all output message for SPI
    writeSPI(CS,messageA);                                                              //Write Port A configuration over SPI
    writeSPI(CS,messageB);                                                              //Write Port B configuration over SPI
}//initGPIO

void writeGPIO(uint8_t CS, uint16_t bank, uint8_t byte){
	/* @param CS	selects the chip to communicate with
	 * @param bank	selects the side of the GPIO to write to (A or B)
	 * @param byte	the state written to the GPIO pin (HIGH or LOW)
	 */
    uint16_t operation = (GPIO_OPCODE_WRITE<<16)+(bank<<8)+byte;
    struct Message message = msgMkr(operation,24);
    writeSPI(CS,message);
}//writeGPIO


uint16_t readGPIO(uint8_t CS, uint8_t bank){
	/* Reads and returns the data on one side of the GPIO.
	 * @param CS	selects the chip to communicate with
	 * @param bank	selects the side of the GPIO to read (A or B)
	 */
    uint16_t operation = (GPIO_OPCODE_READ<<8)+bank;
    struct Message message = msgMkr(operation, 16);
    writeSPI(CS, message);
    return readSPI(CS,BANK_SIZE); //can the size of this be trimmed to 8 bits?
}//readGPIO


