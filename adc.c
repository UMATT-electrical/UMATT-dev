/**
 * ADC_C
 * @author K Gledson
 * @version 2021-01-21
 * Functions needed to communicate with the Analog to Digital Converter (ADC)
 */

///////////////////////////////////////////////////////////////////////////////////////// included files (get rid of these later)
#include "stdint.h" //library not found on my computer.
#include "adc.h"
#include "definitions.h"
///////////////////////////////////////////////////////////////////////////////////////// functions

uint16_t readADC(uint8_t channel){
	/* reads and returns the data from the ADC channel
	 * @param channel	the ADC channel to read
	 */
    struct Message message = msgMkr(channel, OPCODE_SIZE+1); 	//ADC requires leading zero for transmission
    writeSPI(ADC_CS, message);									//Request transmission from ADC
    return readSPI(ADC_CS,RESOLUTION);							//Return ADC transmission
}//readGPIO
