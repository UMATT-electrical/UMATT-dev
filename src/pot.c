/**
 * POT_C
 * @author K Gledson
 * @version 2021-01-21
 * Functions needed to communicate with the Digital Potentiometer (POT) chips
 */

#include "pot.h"

void writePot(uint8_t value){
	/* Writes data to the potentiometer
	 * @param value	new data for the potentiometer
	 */
    uint16_t operation = (POT_OPCODE_WRITE<<12)+(POT_SELECT_0<<8)+value;
    message_32b message = msgMkr(operation,16);
    writeSPI(POT_CS,message);
}//writePot

void setPot(uint8_t value){
	/* Changes the voltage output of the potentiometer
	 * @param value	determines the voltage to set the potentiometer
	 */
    value = getMax(0, getMin(1,1-value)); //get normalized voltage (idk why this is how it's determined)
    writePot(value);
}

uint8_t getMax (uint8_t value1, uint8_t value2){
    uint8_t max = value2;
    if (value1 > value2){
        max = value1;
    }//if
    return max;
}//getMax

uint8_t getMin(uint8_t value1, uint8_t value2){
	uint8_t min = value2;
	if (value1 < value2){
		min = value1;
	}//if
	return min;
}//getMin
